import requests
import ctypes
import re
import os

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from os.path import expanduser
from window_ui import TreeUi
from settings_ui import Ui_Settings
from url_ui import Ui_Url
from threading import Thread
from bs4 import BeautifulSoup


class App(QMainWindow):
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.ui = Ui_Url()
		self.ui.setupUi(self)
		self.init_ui()

	def init_ui(self):
		self.ui.ok_btn.clicked.connect(self.parse)

	def parse(self):
		url = self.ui.url_input.text()
		parser = Parser(url)
		tree = parser.tree
		self.window = Window(tree)
		self.window.show()
		self.hide()


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
			self.auth = self.settings.value("auth")
			self.ui.login_input.setText(self.auth[0])
			self.ui.pw_input.setText(self.auth[1])

	def save_settings(self):
		self.settings.setValue("save_path", self.save_path)
		self.settings.setValue("auth", self.auth)

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

	def get_tree_hierarchy(self, path):
		last_slice = 0
		parent = self.ui.treeWidget.invisibleRootItem()
		for i, sel in enumerate(path):
			if sel == "/":
				element = path[last_slice:i]
				toggle = QTreeWidgetItem()
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

				last_slice = i + 1  # i + "/

	def silent_download(self, file_name):
		content = get_file_content(self.tree[file_name][1], self.settings.auth)
		if not content:
			return
		with open(self.settings.save_path + "/" + file_name, "wb") as f:
			f.write(content)

	def dirs_silent_download(self, file_name):
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
					with open(self.settings.save_path + "/" + path + "/" + fn, "wb") as f:
						f.write(content)

	def download_file(self):
		item = self.ui.treeWidget.currentItem()
		file_name = item.text(0)
		if not self.settings.save_path:
			show_error("choose save_path")
			return
		if file_name in self.tree:
			Thread(target=self.silent_download, args=(file_name,)).start()
		else:
			Thread(target=self.dirs_silent_download, args=(file_name,)).start()

	def init_ui(self):
		self.ui.setting_btn.clicked.connect(lambda: self.settings.show())
		self.ui.download_btn.clicked.connect(self.download_file)

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
		print("start parser")
		html = self.get_html()
		self.tree = self.parse()

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
	ctypes.windll.user32.MessageBoxW(0, text, "Error",0)


def start():
	app = QApplication([])
	window = App()
	window.show()
	app.exec_()



if __name__ == '__main__':
	start()