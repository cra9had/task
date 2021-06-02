import time

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from url_ui import Ui_Url


class Worker(QThread):
	intReady = Signal(int)
	finished = Signal()

	def run(self):
		for i in range(1, 10):
			time.sleep(1)
			self.intReady.emit(i)
		self.finished.emit()


class Window(QMainWindow):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		thread = Worker()
		thread.finished.connect(self.slot)
		thread.intReady.connect(self.slot)
		thread.start()
		self.ui = Ui_Url()
		self.ui.setupUi(self)

	@staticmethod
	def slot(argument='finished'):
		print(argument)


if __name__ == '__main__':
	app = QApplication([])
	window = Window()
	window.show()
	app.exec_()
