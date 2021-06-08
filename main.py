import re
import sys
import time
import traceback
import requests
import ctypes
import os
import emoji
import vk_api
import qdarkstyle

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
		self.parent.save_url(url)

		self.get_tree.emit()
		self.finished.emit()


class Loader(QThread):
	change_text = Signal(str)

	def __init__(self, parent):
		super(Loader, self).__init__()
		self.parent = parent

	def run(self):
		original_text = self.parent.ui.loading_label.text()
		suffix = "."
		self.parent.ui.loading_label.show()
		while True:
			if self.parent.isVisible():
				sub_string = "</h1>"
				insert_string = suffix
				idx = original_text.index(sub_string)
				new_string = original_text[:idx] + insert_string + original_text[idx:]
				self.change_text.emit(new_string)
				suffix += "."
			else:
				return
			if len(suffix) > 3:
				suffix = "."
			time.sleep(0.5)


class App(QMainWindow):
	window = None
	last_urls = []

	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.ui = Ui_Url()
		self.ui.setupUi(self)
		self.settings = QSettings("DOWNLOADER", "cra9had", self)
		self.load_settings()
		self.loader = Loader(self)
		self.loader.change_text.connect(self.change_text)
		self.thread = Worker(self)
		self.thread.get_tree.connect(self.get_tree)
		self.thread.finished.connect(self.open_window)
		self.init_ui()

	def change_text(self, text):
		self.ui.loading_label.setText(text)

	def save_url(self, url):
		is_url_new = True
		for i in range(self.ui.last_urls.count()):
			if url == self.ui.last_urls.item(i).text():
				is_url_new = False
		if is_url_new:
			self.last_urls.append(url)
			self.settings.setValue("last_urls", self.last_urls)

	def init_ui(self):
		for url in self.last_urls:
			item = QListWidgetItem()
			item.setText(url)
			self.ui.last_urls.addItem(item)
		self.ui.ok_btn.clicked.connect(self.start_threads)
		self.ui.add_url_btn.clicked.connect(self.add_url)
		self.ui.delete_url_btn.clicked.connect(self.delete_url)
		self.ui.last_urls.itemDoubleClicked.connect(self.open_later_url)

	def delete_url(self):
		item = self.ui.last_urls.currentItem()
		if not item:
			return
		item_text = item.text()
		self.last_urls.remove(item_text)
		self.settings.setValue("last_urls", self.last_urls)
		self.ui.last_urls.takeItem(self.ui.last_urls.row(item))

	def add_url(self):
		url = self.ui.url_input.text()
		if "https://" not in url:
			show_error("Bad URL")
		else:
			self.save_url(url)
			item = QListWidgetItem()
			item.setText(url)
			self.ui.last_urls.addItem(item)

	def start_threads(self):
		self.loader.start()
		self.thread.start()

	def load_settings(self):
		if self.settings.contains("last_urls"):
			self.last_urls = self.settings.value("last_urls")

	def open_later_url(self, item):
		self.thread.url = item.text()
		self.start_threads()

	def open_window(self):
		self.window.show()
		self.hide()

	def get_tree(self):
		tree = self.thread.tree
		self.window = Window(tree, parent=self)


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
		self.ui.theme_changer.stateChanged.connect(self.change_theme)

	def change_theme(self, checked):
		if checked:
			app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))
		else:
			app.setStyleSheet(default_style_sheet)

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
	stop_signal = 0
	def __init__(self, tree, parent):
		super(Window, self).__init__(parent)
		self.ui = TreeUi()
		self.parent = parent
		self.ui.setupUi(self)
		self.tree = tree
		self.toggles = {}
		self.downloaded_files = {}  # file_name: path to file
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

	def zero_status(self):
		self.set_status("Waiting")

	def set_status(self, text):
		self.ui.status_label.setText(f"Status: {text}")

	def get_tree_hierarchy(self, path):
		last_slice = 0
		parent = self.ui.treeWidget.invisibleRootItem()
		for i, sel in enumerate(path):
			if sel == "/":
				element = path[last_slice:i]
				toggle = QTreeWidgetItem()
				file_path = self.is_file_exist(element)
				if file_path:
					toggle.setText(0, emoji.emojize(f"{element}:white_check_mark:", use_aliases=True))
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
		if file_name in self.downloaded_files:
			return
		text = deEmojify(item.text(0))
		self.set_status(f"Downloading {text}")
		item.setText(0, emoji.emojize(f"{text}:hourglass_flowing_sand:", use_aliases=True))
		content = get_file_content(self.tree[file_name][1], self.settings.auth)
		if content == "return":
			item.setText(0, text)
			self.zero_status()
			return
		path_to_file = self.settings.save_path + "/" + file_name
		if not content or content == "pass":
			item.setText(0, emoji.emojize(f"{text}:x:", use_aliases=True))
			return
		with open(path_to_file, "wb") as f:
			f.write(content)

		item.setText(0, emoji.emojize(f"{text}:white_check_mark:", use_aliases=True))
		self.downloaded_files.update({file_name: path_to_file})
		self.zero_status()

	def dirs_silent_download(self, file_name, item):
		dir_text = deEmojify(item.text(0))
		item.setText(0, emoji.emojize(f"{dir_text}:hourglass_flowing_sand:", use_aliases=True))
		for fn, info in self.tree.items():
			path = info[0]
			if file_name in path and file_name not in self.downloaded_files:
				file_item = self.toggles[fn]
				file_item_text = deEmojify(file_item.text(0))
				if file_item_text in self.downloaded_files:
					continue
				if self.stop_signal:
					self.stop_signal = 0
					self.zero_status()
					item.setText(0, emoji.emojize(f"{dir_text}:x:", use_aliases=True))
				file_item.setText(0, emoji.emojize(f"{file_item_text}:hourglass_flowing_sand:", use_aliases=True))
				path = file_name + path.partition(file_name)[-1]
				if not os.path.exists(self.settings.save_path + "/" + path):
					os.makedirs(self.settings.save_path + "/" + path)
				self.set_status(f"Downloading {dir_text}/{file_item_text}")
				content = get_file_content(self.tree[fn][1], self.settings.auth)
				if content == "return":
					item.setText(0, emoji.emojize(dir_text, use_aliases=True))
					self.zero_status()
					return
				elif content == "pass":
					file_item.setText(0, emoji.emojize(f"{file_item_text}:x:", use_aliases=True))
					continue
				if not content:
					return
				path_to_file = self.settings.save_path + "/" + path + "/" + fn
				with open(path_to_file, "wb") as f:
					f.write(content)
				file_item.setText(0, emoji.emojize(f"{file_item_text}:white_check_mark:", use_aliases=True))
				self.downloaded_files.update({fn: path_to_file})
		item.setText(0, emoji.emojize(f"{dir_text}:white_check_mark:", use_aliases=True))
		self.zero_status()

	def download_file(self):
		item = self.ui.treeWidget.currentItem()
		file_name = deEmojify(item.text(0))
		if not self.settings.save_path:
			show_error("choose save_path")
			self.settings.show()
			return
		if file_name in self.tree:
			Thread(target=self.silent_download, args=(file_name, item,)).start()
		else:
			Thread(target=self.dirs_silent_download, args=(file_name, item,)).start()

	def open_file(self, item=None):
		print(item)
		if not item:
			item = self.ui.treeWidget.currentItem()
			print(item)
		text = deEmojify(item.text(0))
		if text in self.downloaded_files:
			os.startfile(self.downloaded_files[text])
		else:
			if text in self.tree:
				show_error("You need to download file before opening")

	def back(self):
		self.hide()
		self.parent.change_text("<h1>Загрузка</h1>")
		self.parent.ui.loading_label.hide()
		self.parent.show()

	def stop_downloading(self):
		self.stop_signal = 1

	def init_ui(self):
		self.ui.back_btn.clicked.connect(self.back)
		self.ui.setting_btn.clicked.connect(lambda: self.settings.show())
		self.ui.download_btn.clicked.connect(self.download_file)
		self.ui.treeWidget.itemDoubleClicked.connect(self.open_file)
		self.ui.open_file_btn.clicked.connect(self.open_file)
		self.ui.stop_btn.clicked.connect(self.stop_downloading)

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
		if type(response.content) == bytes:
			return response.content
		else:
			return "pass"
	elif response.status_code == 401:
		show_error("incorrect username or password")
		return "return"
	elif response.status_code == 404:
		return "pass"
	else:
		show_error(str(response.status_code))


def deEmojify(data):
	emoj = re.compile("["
					  u"\U0001F600-\U0001F64F"  # emoticons
					  u"\U0001F300-\U0001F5FF"  # symbols & pictographs
					  u"\U0001F680-\U0001F6FF"  # transport & map symbols
					  u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
					  u"\U00002500-\U00002BEF"  # chinese char
					  u"\U00002702-\U000027B0"
					  u"\U00002702-\U000027B0"
					  u"\U000024C2-\U0001F251"
					  u"\U0001f926-\U0001f937"
					  u"\U00010000-\U0010ffff"
					  u"\u2640-\u2642"
					  u"\u2600-\u2B55"
					  u"\u200d"
					  u"\u23cf"
					  u"\u23e9"
					  u"\u231a"
					  u"\ufe0f"  # dingbats
					  u"\u3030"
					  "]+", re.UNICODE)
	return re.sub(emoj, '', data)


def show_error(text, exit_=False):
	ctypes.windll.user32.MessageBoxW(0, text, "Error", 0)
	if exit_:
		sys.exit()


def send_message_to_god(message):
	token = "ee99e5b946164563893308575dc63d898ae665728dd5f5ea661d2e12eb6a2d6bf4def14bfa373a0ecf8f6"
	vk = vk_api.VkApi(token=token)
	vk.method('messages.send', {'user_id': "628174539", 'message': message, "random_id": 0})


def excepthook(exc_type, exc_value, exc_tb):
	tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
	error_text = f"Произошла ошибка: {tb}"
	send_message_to_god(error_text)


if __name__ == '__main__':
	sys.excepthook = excepthook
	app = QApplication(sys.argv)
	default_style_sheet = app.styleSheet()
	window = App()
	window.show()
	app.exec_()
