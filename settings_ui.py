# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(422, 300)
        Settings.setWindowIcon(QIcon('images/icon.ico'))   
        self.centralwidget = QWidget(Settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 91, 41))
        self.path_lable = QLabel(self.centralwidget)
        self.path_lable.setObjectName(u"path_lable")
        self.path_lable.setGeometry(QRect(90, 30, 201, 21))
        self.path_lable.setAutoFillBackground(False)
        self.path_lable.setStyleSheet(u"background-color: white;")
        self.change_btn = QPushButton(self.centralwidget)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setGeometry(QRect(300, 30, 111, 31))
        self.login_input = QLineEdit(self.centralwidget)
        self.login_input.setObjectName(u"login_input")
        self.login_input.setGeometry(QRect(110, 70, 201, 21))
        self.login_input.setStyleSheet(u".QLineEdit{\n"
"	border-style: outset;\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(81, 82, 78);\n"
"}")
        self.pw_input = QLineEdit(self.centralwidget)
        self.pw_input.setObjectName(u"pw_input")
        self.pw_input.setGeometry(QRect(110, 120, 201, 21))
        self.pw_input.setStyleSheet(u".QLineEdit{\n"
"	border-style: outset;\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(81, 82, 78);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 71, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 60, 16))
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Save path:", None))
        self.path_lable.setText("")
        self.change_btn.setText(QCoreApplication.translate("Settings", u"Change", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"Password", None))
    # retranslateUi

