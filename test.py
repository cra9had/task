from main import App
from PySide2.QtWidgets import *


class TestUi:
	def __init__(self):
		app = QApplication([])
		window = App()
		window.show()
		app.exec_()



if __name__ == '__main__':
	TestUi()
