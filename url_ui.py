from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Url(object):
    def setupUi(self, Url):
        if not Url.objectName():
            Url.setObjectName(u"Url")
        Url.resize(446, 171)
        self.centralwidget = QWidget(Url)
        self.centralwidget.setObjectName(u"centralwidget")
        self.url_input = QLineEdit(self.centralwidget)
        self.url_input.setObjectName(u"url_input")
        self.url_input.setGeometry(QRect(70, 100, 319, 20))
        self.ok_btn = QPushButton(self.centralwidget)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setGeometry(QRect(70, 140, 319, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 319, 81))
        self.label.setAlignment(Qt.AlignCenter)
        Url.setCentralWidget(self.centralwidget)

        self.retranslateUi(Url)

        QMetaObject.connectSlotsByName(Url)

    def retranslateUi(self, Url):
        Url.setWindowTitle(QCoreApplication.translate("Url", u"DOWNLOADER", None))
        self.ok_btn.setText(QCoreApplication.translate("Url", u"Ok", None))
        self.label.setText(QCoreApplication.translate("Url", u"<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">Enter URL:</span></p></body></html>", None))
