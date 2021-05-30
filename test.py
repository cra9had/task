from main import Parser, Window
from PySide2.QtWidgets import *


class TestUi:
	def __init__(self):
		self.parser = TestParser()
		app = QApplication([])
		window = Window(self.parser.tree)
		window.show()
		app.exec_()


class TestParser:
	def __init__(self):
		self.url = "https://files.sahajculture.ru/index-email.html"
		self.username = "sahaja"
		self.password = "Jai Shri Mataji"
		self.parser = Parser(self.url)
		self.tree = self.parser.tree


if __name__ == '__main__':
	TestUi()
