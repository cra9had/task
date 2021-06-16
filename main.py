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
from search_ui import Ui_Search
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
        self.hide()
        self.window.show()

    def get_tree(self):
        tree = self.thread.tree
        self.window = Window(tree, parent=self)


class Settings(QMainWindow):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.parent = parent
        self.save_path = None
        self.auth = ("", "")
        self.downloaded_files = {}
        self.settings = QSettings("DOWNLOADER", "cra9had", self)
        self.load_settings()
        self.init_ui()

    def init_ui(self):
        self.ui.change_btn.clicked.connect(self.change_path)
        self.ui.path_lable.textChanged.connect(self.remake_path)
        self.ui.login_input.textChanged.connect(self.change_auth)
        self.ui.pw_input.textChanged.connect(self.change_auth)
        self.ui.theme_changer.stateChanged.connect(self.change_theme)

    @staticmethod
    def change_theme(checked):
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
            print(self.auth[1])
            self.auth[1] = ""
            self.auth = tuple(self.auth)
            self.ui.login_input.setText(self.auth[0])
        if self.settings.contains("downloaded_files"):
            self.downloaded_files = self.settings.value("downloaded_files")

    def save_settings(self):
        self.settings.setValue("save_path", self.save_path)
        self.settings.setValue("auth", self.auth)
        self.settings.setValue("downloaded_files", self.parent.downloaded_files)

    def remake_path(self):
        self.save_path = self.ui.path_lable.text()

    def change_path(self):
        save_path = QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        if save_path:
            self.save_path = save_path
            self.ui.path_lable.setText(self.save_path)
            self.save_settings()


class Searcher(QMainWindow):
    def __init__(self, parent=None):
        super(Searcher, self).__init__(parent)
        self.parent = parent
        self.items = []
        self.current_index = 0
        self.last_text = ""
        self.ui = Ui_Search()
        self.ui.setupUi(self)

        self.init_ui()

    def find_item(self):
        text = self.ui.item_input.text()
        if not self.items:
            self.current_index = 0
            for filename, item in self.parent.toggles.items():
                if text in filename:
                    self.items.append(item)
            if not self.items:
                show_error("Не найдено")
                return

        if self.current_index == len(self.items):
            self.current_index = 0

        self.parent.ui.treeWidget.scrollToItem(self.items[self.current_index])
        self.parent.ui.treeWidget.setCurrentItem(self.items[self.current_index], 0)
        self.current_index += 1

    def text_changed(self):
        self.items = []

    def init_ui(self):
        self.ui.search_btn.clicked.connect(self.find_item)
        self.ui.item_input.textChanged.connect(self.text_changed)


class DownloadFile(QThread):
    progress_percent = Signal(int)

    def __init__(self, parent, file_name, item):
        super(DownloadFile, self).__init__()
        self.parent = parent
        self.file_name = file_name
        self.item = item

    def run(self):
        if self.file_name in self.parent.downloaded_files:
            return
        text = deEmojify(self.item.text(0))
        if self.parent.is_tree_loaded:
            self.parent.set_status(f"Скачивается {text}")
        self.item.setText(0, emoji.emojize(f"{text}:hourglass_flowing_sand:", use_aliases=True))
        response = get_file_content(self.parent.tree[self.file_name][1], self.parent.settings.auth)
        if response == "return":
            self.item.setText(0, text)
            if self.parent.is_tree_loaded:
                self.parent.zero_status()
            return
        if not response or response == "pass":
            self.item.setText(0, emoji.emojize(f"{text}:x:", use_aliases=True))
            return
        total = response.headers.get('content-length')
        if total is None:
            if self.parent.is_tree_loaded:
                self.parent.zero_status()
            return
        path_to_file = self.parent.settings.save_path + "/" + self.file_name
        with open(path_to_file, "wb") as f:
            downloaded = 0
            total = int(total)

            for data in response.iter_content(chunk_size=2048):
                if data:
                    downloaded += len(data)
                    f.write(data)
                    f.flush()
                    done = int(100 / (total / downloaded))
                    self.progress_percent.emit(done)
        self.progress_percent.emit(0)

        self.item.setText(0, emoji.emojize(f"{text}:white_check_mark:", use_aliases=True))
        self.parent.downloaded_files.update({self.file_name: path_to_file})
        self.parent.settings.save_settings()
        if self.parent.is_tree_loaded:
            self.parent.zero_status()


class DownloadDirs(QThread):
    finish = Signal()
    progress_percent = Signal(int)

    def __init__(self, parent, file_name, item):
        super(DownloadDirs, self).__init__()
        self.parent = parent
        self.file_name = file_name
        self.item = item

    def run(self):
        dir_text = deEmojify(self.item.text(0))
        self.item.setText(0, emoji.emojize(f"{dir_text}:hourglass_flowing_sand:", use_aliases=True))
        for fn, info in self.parent.tree.items():
            path = info[0]
            if self.file_name in path and self.file_name not in self.parent.downloaded_files:
                file_item = self.parent.toggles[fn]
                file_item_text = deEmojify(file_item.text(0))
                if file_item_text in self.parent.downloaded_files or file_item_text != file_item.text(0):
                    continue
                if self.parent.stop_signal:
                    self.parent.threads -= 1
                    if self.parent.threads == 0:
                        self.parent.stop_signal = 0
                    self.parent.zero_status()
                    self.item.setText(0, dir_text)
                    file_item.setText(0, file_item_text)
                    return
                file_item.setText(0, emoji.emojize(f"{file_item_text}:hourglass_flowing_sand:", use_aliases=True))
                path = self.file_name + path.partition(self.file_name)[-1]
                if not os.path.exists(self.parent.settings.save_path + "/" + path):
                    os.makedirs(self.parent.settings.save_path + "/" + path)
                self.parent.set_status(f"Скачивается {dir_text}/{file_item_text}")
                response = get_file_content(self.parent.tree[fn][1], self.parent.settings.auth)
                if response == "return":
                    self.item.setText(0, emoji.emojize(dir_text, use_aliases=True))
                    file_item.setText(0, file_item_text)
                    self.parent.zero_status()
                    return
                elif response == "pass":
                    file_item.setText(0, emoji.emojize(f"{file_item_text}:x:", use_aliases=True))
                    continue
                if not response:
                    return
                path_to_file = self.parent.settings.save_path + "/" + path + "/" + fn
                total = response.headers.get('content-length')
                if total is None:
                    if self.parent.is_tree_loaded:
                        self.parent.zero_status()
                    return

                with open(path_to_file, "wb") as f:
                    downloaded = 0
                    total = int(total)
                    for data in response.iter_content(chunk_size=1024):
                        if data:
                            downloaded += len(data)
                            f.write(data)
                            f.flush()
                            done = int(100 / (total / downloaded))
                            self.progress_percent.emit(done)

                self.progress_percent.emit(0)
                file_item.setText(0, emoji.emojize(f"{file_item_text}:white_check_mark:", use_aliases=True))
                self.parent.downloaded_files.update({fn: path_to_file})
                self.parent.settings.save_settings()
        self.item.setText(0, emoji.emojize(f"{dir_text}:white_check_mark:", use_aliases=True))
        self.parent.zero_status()
        self.finish.emit()


class Window(QMainWindow):
    stop_signal = 0
    threads = 0
    processes = []
    is_tree_loaded = False

    def __init__(self, tree, parent):
        super(Window, self).__init__(parent)
        self.ui = TreeUi()
        self.parent = parent
        self.ui.setupUi(self)
        self.tree = tree
        self.toggles = {}
        self.downloaded_files = {}  # file_name: path to file
        self.settings = Settings(self)
        self.proc_checker = Thread(target=self.check_processes, daemon=True)
        self.proc_checker.start()
        self.shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.shortcut.activated.connect(self.show_search)
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
        Thread(target=self.create_tree).start()
        self.init_ui()

    def show_search(self):
        searcher = Searcher(self)
        searcher.show()

    def is_toggle_downloaded(self, parent_item) -> bool:
        for i in range(parent_item.childCount()):
            child = parent_item.child(i)
            text = deEmojify(child.text(0))
            if text not in self.tree:
                if not self.is_toggle_downloaded(child):
                    return False
            else:
                if text not in self.settings.downloaded_files:
                    return False
        return True

    def check_processes(self):
        while True:
            for proc in self.processes:
                if not proc.is_alive():
                    self.processes.remove(proc)
            time.sleep(0.05)

    def zero_status(self):
        self.set_status("Waiting")

    def show_window(self):
        if self.windowState() != Qt.WindowMaximized:
            self.showMaximized()
            self.showNormal()
        else:
            self.showNormal()
            self.showMaximized()

        self.raise_()
        self.activateWindow()

    def set_status(self, text):
        self.ui.status_label.setText(f"Статус: {text}")

    def get_tree_hierarchy(self, path):
        last_slice = 0
        parent = self.ui.treeWidget.invisibleRootItem()
        for i, sel in enumerate(path):
            if sel == "/":
                element = path[last_slice:i]
                toggle = QTreeWidgetItem()
                if element in self.settings.downloaded_files:
                    toggle.setText(0, emoji.emojize(f"{element}:white_check_mark:", use_aliases=True))
                    self.downloaded_files.update({element: self.settings.downloaded_files[element]})
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

    def check_toggles(self):
        for toggle, item in self.toggles.items():
            if toggle not in self.tree:
                if self.is_toggle_downloaded(item):
                    item.setText(0, toggle + emoji.emojize(":white_check_mark:", use_aliases=True))

    def silent_download(self, file_name, item):
        if file_name in self.downloaded_files:
            return
        text = deEmojify(item.text(0))
        if self.is_tree_loaded:
            self.set_status(f"Скачивается {text}")
        item.setText(0, emoji.emojize(f"{text}:hourglass_flowing_sand:", use_aliases=True))
        response = get_file_content(self.tree[file_name][1], self.settings.auth)
        if response == "return":
            item.setText(0, text)
            if self.is_tree_loaded:
                self.zero_status()
            return
        if not response or response == "pass":
            item.setText(0, emoji.emojize(f"{text}:x:", use_aliases=True))
            return
        total = response.headers.get('content-length')
        if total is None:
            if self.is_tree_loaded:
                self.zero_status()
            return
        path_to_file = self.settings.save_path + "/" + file_name
        with open(path_to_file, "wb") as f:
            downloaded = 0
            total = int(total)

            for data in response.iter_content(chunk_size=2048):
                if data:
                    downloaded += len(data)
                    f.write(data)
                    f.flush()
                    done = int(100 / (total / downloaded))
                    self.progress_bar_set_value(done)
        self.progress_bar_set_value(0)

        item.setText(0, emoji.emojize(f"{text}:white_check_mark:", use_aliases=True))
        self.downloaded_files.update({file_name: path_to_file})
        self.settings.save_settings()
        if self.is_tree_loaded:
            self.zero_status()

    def progress_bar_set_value(self, value):
        if self.ui.progressBar.value() != value:
            self.ui.progressBar.setValue(value)
            QApplication.processEvents()

    def download_file(self):
        item = self.ui.treeWidget.currentItem()
        file_name = deEmojify(item.text(0))
        if not self.settings.save_path:
            show_error("Выберете путь сохранения")
            self.settings.show()
            return
        if file_name in self.tree:
            self.process = DownloadFile(self, file_name, item)
            self.process.progress_percent.connect(self.progress_bar_set_value)
            self.process.start()
        else:
            if not self.is_tree_loaded:
                show_error("дождитесь завершения загрузки дерева файлов")
                return

            self.process = DownloadDirs(self, file_name, item)
            self.process.progress_percent.connect(self.progress_bar_set_value)
            self.process.finish.connect(self.thread_finished)
            self.process.start()
            self.threads += 1

    def thread_finished(self):
        self.threads -= 1

    def open_file(self, item=None):
        if not item:
            item = self.ui.treeWidget.currentItem()
        self.is_children_download(item)
        text = deEmojify(item.text(0))
        if text in self.downloaded_files:
            os.startfile(self.downloaded_files[text])
        else:
            if text in self.tree:
                show_error("Нужно скачать файл перед его открытием")

    def back(self):
        self.hide()
        self.parent.change_text("<h1>Загрузка</h1>")
        self.parent.ui.loading_label.hide()
        self.parent.show()

    def stop_downloading(self):
        if self.threads:
            self.stop_signal = 1

    def create_tree(self):
        self.set_status("загрузка дерева файлов")
        for file_name, info in self.tree.items():
            path = info[0]
            self.get_tree_hierarchy(path + "/" + file_name + "/")
        self.is_tree_loaded = True
        thread = Thread(target=self.check_toggles, daemon=True)
        thread.start()
        thread.join()
        self.zero_status()

    def init_ui(self):
        self.ui.back_btn.clicked.connect(self.back)
        self.ui.setting_btn.clicked.connect(lambda: self.settings.show())
        self.ui.download_btn.clicked.connect(self.download_file)
        self.ui.treeWidget.itemDoubleClicked.connect(self.open_file)
        self.ui.open_file_btn.clicked.connect(self.open_file)
        self.ui.stop_btn.clicked.connect(self.stop_downloading)
        self.ui.search_btn.clicked.connect(self.show_search)


class ParsingError(Exception):
    pass


class Parser:
    def __init__(self, url):
        self.url = url
        self.host = self.get_host()
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
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise show_error(f"get {response.status_code} error during parser")


def get_file_content(url, auth):
    response = requests.get(url, auth=auth, stream=True)

    if response.status_code == 200:
        return response
    elif response.status_code == 401:
        show_error("неверный логин или пароль")
        return "return"
    elif response.status_code == 404:
        return "pass"
    else:
        show_error(str(response.status_code))


def deEmojify(data):
    emoj = "[⏳|✅|❌]"
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
