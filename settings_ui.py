from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(422, 300)
        self.centralwidget = QWidget(Settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 91, 41))
        self.path_lable = QLabel(self.centralwidget)
        self.path_lable.setObjectName(u"path_lable")
        self.path_lable.setGeometry(QRect(90, 30, 151, 21))
        self.path_lable.setAutoFillBackground(False)
        self.path_lable.setStyleSheet(u"background-color: white;")
        self.change_btn = QPushButton(self.centralwidget)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setGeometry(QRect(260, 30, 111, 31))
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Save path:", None))
        self.change_btn.setText(QCoreApplication.translate("Settings", u"Change", None))
