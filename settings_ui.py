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
        Settings.resize(471, 178)
        self.centralwidget = QWidget(Settings)
        self.centralwidget.setObjectName(u"centralwidget")
        self.change_btn = QPushButton(self.centralwidget)
        self.change_btn.setObjectName(u"change_btn")
        self.change_btn.setGeometry(QRect(152, 40, 101, 21))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(12)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(26,115,232);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 2px;\n"
"	border: 1px solid rgb(26,115,232);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(27,102,201);\n"
"}")
        self.login_input = QLineEdit(self.centralwidget)
        self.login_input.setObjectName(u"login_input")
        self.login_input.setGeometry(QRect(80, 100, 191, 18))
        self.login_input.setStyleSheet(u".QLineEdit{\n"
"	border-style: outset;\n"
"	border-radius: 5px;\n"
"	border: 1px solid white;\n"
"}")
        self.pw_input = QLineEdit(self.centralwidget)
        self.pw_input.setObjectName(u"pw_input")
        self.pw_input.setGeometry(QRect(80, 70, 191, 18))
        self.pw_input.setStyleSheet(u".QLineEdit{\n"
"	border-style: outset;\n"
"	border-radius: 5px;\n"
"	border: 1px solid white;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(2, 67, 71, 20))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 100, 71, 20))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.theme_changer = QCheckBox(self.centralwidget)
        self.theme_changer.setObjectName(u"theme_changer")
        self.theme_changer.setEnabled(True)
        self.theme_changer.setGeometry(QRect(10, 130, 131, 31))
        self.theme_changer.setFont(font)
        self.theme_changer.setStyleSheet(u"")
        self.path_lable = QLineEdit(self.centralwidget)
        self.path_lable.setObjectName(u"path_lable")
        self.path_lable.setGeometry(QRect(70, 10, 331, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(2, 12, 61, 20))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"MainWindow", None))
        self.change_btn.setText(QCoreApplication.translate("Settings", u"\u041f\u043e\u043c\u0435\u043d\u044f\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.theme_changer.setText(QCoreApplication.translate("Settings", u"\u0422\u0451\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.label.setText(QCoreApplication.translate("Settings", u"\u041f\u0443\u0442\u044c:", None))
    # retranslateUi

