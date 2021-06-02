import sys

import requests
import ctypes
import os
import emoji

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from os.path import expanduser
from window_ui import TreeUi
from settings_ui import Ui_Settings
from url_ui import Ui_Url
from threading import Thread
from bs4 import BeautifulSoup


class Worker(QThread):
	finished = Signal()
	get_tree = Signal()
	parser = None
	url = None
	tree = None

	def __init__(self, parent):
		super(Worker, self).__init__()
		self.parent = parent

	def run(self):
		if not self.url:
			url = self.parent.ui.url_input.text()
		else:
			url = self.url
		self.parser = Parser(url)
		self.tree = self.parser.tree
		is_url_new = True
		for i in range(self.parent.ui.last_urls.count()):
			if url == self.parent.ui.last_urls.item(i).text():
				is_url_new = False
		if is_url_new:
			self.parent.last_urls.append(url)
			self.parent.settings.setValue("last_urls", self.parent.last_urls)

		self.get_tree.emit()
		self.finished.emit()


class App(QMainWindow):
	window = None
	last_urls = []

	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.ui = Ui_Url()
		self.ui.setupUi(self)
		self.settings = QSettings("DOWNLOADER", "cra9had", self)
		self.load_settings()
		self.thread = Worker(self)
		self.thread.get_tree.connect(self.get_tree)
		self.thread.finished.connect(self.open_window)
		self.init_ui()

	def init_ui(self):
		for url in self.last_urls:
			item = QListWidgetItem()
			item.setText(url)
			self.ui.last_urls.addItem(item)
		self.ui.ok_btn.clicked.connect(self.thread.start)
		self.ui.last_urls.itemDoubleClicked.connect(self.open_later_url)

	def load_settings(self):
		if self.settings.contains("last_urls"):
			self.last_urls = self.settings.value("last_urls")
		else:
			print("else")

	def open_later_url(self, item):
		self.thread.url = item.text()
		self.thread.start()

	def open_window(self):
		self.window.show()
		self.hide()

	def get_tree(self):
		tree = self.thread.tree
		self.window = Window(tree)


class Settings(QMainWindow):
	def __init__(self, parent=None):
		super(Settings, self).__init__(parent)
		self.ui = Ui_Settings()
		self.ui.setupUi(self)
		self.save_path = None
		self.auth = ("", "")
		self.settings = QSettings("DOWNLOADER", "cra9had", self)
		self.load_settings()
		self.init_ui()

	def init_ui(self):
		self.ui.change_btn.clicked.connect(self.change_path)
		self.ui.path_lable.textChanged.connect(self.remake_path)
		self.ui.login_input.textChanged.connect(self.change_auth)
		self.ui.pw_input.textChanged.connect(self.change_auth)

	def change_auth(self):
		username = self.ui.login_input.text()
		password = self.ui.pw_input.text()
		self.auth = (username, password)
		self.save_settings()

	def load_settings(self):
		if self.settings.contains("save_path"):
			self.save_path = self.settings.value("save_path", type=str)
			self.ui.path_lable.setText(self.save_path)
		if self.settings.contains("auth"):
			self.auth = list(self.settings.value("auth"))
			self.auth[1] = ""
			self.auth = tuple(self.auth)
			self.ui.login_input.setText(self.auth[0])

	def save_settings(self):
		self.settings.setValue("save_path", self.save_path)
		self.settings.setValue("auth", self.auth)

	def remake_path(self):
		self.save_path = self.ui.path_lable.text()

	def change_path(self):
		self.save_path = QFileDialog.getExistingDirectory(
			self,
			"Open a folder",
			expanduser("~"),
			QFileDialog.ShowDirsOnly
		)
		self.ui.path_lable.setText(self.save_path)
		self.save_settings()


class Window(QMainWindow):
	def __init__(self, tree, parent=None):
		super(Window, self).__init__(parent)
		self.ui = TreeUi()
		self.ui.setupUi(self)
		self.tree = tree
		self.toggles = {}
		self.downloaded_files = {} # file_name: path to file
		self.settings = Settings(self)
		self.icons = {
			".css": QIcon(r"images/document-css.png"),
			".html": QIcon(r"images/document-html.png"),
			".jpg": QIcon(r"images/document-jpg.png"),
			".js": QIcon(r"images/document-js.png"),
			".pdf": QIcon(r"images/document-pdf.png"),
			".png": QIcon(r"images/document-png.png"),
			".txt": QIcon(r"images/document-txt.png"),
			".zip": QIcon(r"images/document-jpg.png"),
			".": QIcon(r"images/document.png"),
		}
		self.init_ui()

	def is_file_exist(self, name):
		for root, dirs, files in os.walk(self.settings.save_path):
			if name in files:
				return os.path.join(root, name)

	def get_tree_hierarchy(self, path):
		last_slice = 0
		parent = self.ui.treeWidget.invisibleRootItem()
		for i, sel in enumerate(path):
			if sel == "/":
				element = path[last_slice:i]
				toggle = QTreeWidgetItem()
				file_path = self.is_file_exist(element)
				if file_path:
					toggle.setText(0, emoji.emojize(f"{element} :white_check_mark:", use_aliases=True))
					self.downloaded_files.update({element: file_path})
				else:
					toggle.setText(0, element)
				icon = QIcon("images/folder-horizontal.png")
				for key, icn in self.icons.items():
					if key in element and element in self.tree:
						icon = icn
						break
				toggle.setIcon(0, icon)
				if element not in self.toggles:
					parent.addChild(toggle)
					parent = toggle
					self.toggles.update({element: toggle})
				else:
					parent = self.toggles[element]

				last_slice = i + 1  # i + "/"

	def silent_download(self, file_name, item):
		content = get_file_content(self.tree[file_name][1], self.settings.auth)
		path_to_file = self.settings.save_path + "/" + file_name
		if not content:
			return
		with open(path_to_file, "wb") as f:
			f.write(content)

		item.setText(0, emoji.emojize(f"{item.text(0)} :white_check_mark:", use_aliases=True))
		self.downloaded_files.update({file_name: path_to_file})

	def dirs_silent_download(self, file_name, item):
		for fn, info in self.tree.items():
				path = info[0]
				if file_name in path:
					path = file_name + path.partition(file_name)[-1]
					if not os.path.exists(self.settings.save_path + "/" + path):
						os.makedirs(self.settings.save_path + "/" + path)
					content = get_file_content(self.tree[fn][1], self.settings.auth)
					if content == "pass":
						continue
					if not content:
						return
					path_to_file = self.settings.save_path + "/" + path + "/" + fn
					with open(path_to_file, "wb") as f:
						f.write(content)
					item.setText(0, emoji.emojize(f"{item.text(0)} :white_check_mark:", use_aliases=True))
					self.downloaded_files.update({fn: path_to_file})

	def download_file(self):
		item = self.ui.treeWidget.currentItem()
		file_name = item.text(0)
		if not self.settings.save_path:
			show_error("choose save_path")
			self.settings.show()
			return
		if file_name in self.tree:
			Thread(target=self.silent_download, args=(file_name, item,)).start()
		else:
			Thread(target=self.dirs_silent_download, args=(file_name, item,)).start()

	def open_file(self, item):
		if item.text(0) in self.downloaded_files:
			os.startfile(self.downloaded_files[item.text(0)])
		else:
			if item.text(0) in self.tree:
				show_error("You need to download file before opening")

	def init_ui(self):
		self.ui.setting_btn.clicked.connect(lambda: self.settings.show())
		self.ui.download_btn.clicked.connect(self.download_file)
		self.ui.treeWidget.itemDoubleClicked.connect(self.open_file)

		for file_name, info in self.tree.items():
			path = info[0]
			self.get_tree_hierarchy(path + "/" + file_name + "/")


class ParsingError(Exception):
	pass


class Parser:
	def __init__(self, url):
		self.url = url
		self.host = self.get_host()
		self.session = requests.session()
		self.tree = self.parse(self.get_html())

	def get_host(self):
		counter = 0
		for i, sel in enumerate(self.url):
			if sel == "/":
				counter += 1
			if counter == 3:
				return self.url[:i]

	@staticmethod
	def remake_path(path):
		obj = list(path)
		obj.pop(0)  # delete first /
		obj.reverse()
		for i, sel in enumerate(obj):
			if sel == "/":
				return "".join(obj[:i:-1])

	def parse(self, html):
		tree = {}
		soup = BeautifulSoup(html, "html.parser")
		page_tree = soup.find("ol", class_='tree')
		files = page_tree.find_all("li", class_="file")
		if not files:
			raise show_error("No files found")
		for file in files:
			info = file.find("a", href=True)
			path = self.remake_path(info["href"])
			href = self.host + info["href"]
			tree.update({info.getText(): [path, href]})
		return tree

	def get_html(self):
		response = self.session.get(self.url)
		if response.status_code == 200:
			return response.text
		else:
			raise show_error(f"get {response.status_code} error during parser")


def get_file_content(url, auth):
	response = requests.get(url, auth=auth)
	if response.status_code == 200:
		return response.content
	elif response.status_code == 401:
		show_error("incorrect username or password")
	elif response.status_code == 404:
		show_error(url, "\nNot Found")
		return "pass"
	else:
		show_error(str(response.status_code))


def show_error(text, exit_=False):
	ctypes.windll.user32.MessageBoxW(0, text, "Error", 0)
	if exit_:
		sys.exit()


def start():
	app = QApplication([])
	window = App()
	window.show()
	app.exec_()


if __name__ == '__main__':
	start()