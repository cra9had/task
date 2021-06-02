from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Url(object):
	def setupUi(self, Url):
		Url.setObjectName("Url")
		Url.resize(446, 417)
		self.centralwidget = QtWidgets.QWidget(Url)
		self.centralwidget.setObjectName("centralwidget")
		self.url_input = QtWidgets.QLineEdit(self.centralwidget)
		self.url_input.setGeometry(QtCore.QRect(70, 100, 319, 20))
		self.url_input.setObjectName("url_input")
		self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
		self.ok_btn.setGeometry(QtCore.QRect(70, 140, 319, 23))
		self.ok_btn.setObjectName("ok_btn")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(70, 10, 319, 81))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.last_urls = QtWidgets.QListWidget(self.centralwidget)
		self.last_urls.setGeometry(QtCore.QRect(30, 201, 391, 201))
		self.last_urls.setObjectName("last_urls")
		Url.setCentralWidget(self.centralwidget)

		self.retranslateUi(Url)
		QtCore.QMetaObject.connectSlotsByName(Url)

	def retranslateUi(self, Url):
		_translate = QtCore.QCoreApplication.translate
		Url.setWindowTitle(_translate("Url", "MainWindow"))
		self.ok_btn.setText(_translate("Url", "Ok"))
		self.label.setText(_translate("Url", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">Enter URL:</span></p></body></html>"))
