# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Search.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.setFixedSize(363, 111)
        self.centralwidget = QWidget(Search)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 0, 302, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.search_btn = QPushButton(self.gridLayoutWidget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(12)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.search_btn, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.item_input = QLineEdit(self.gridLayoutWidget)
        self.item_input.setObjectName(u"item_input")

        self.gridLayout.addWidget(self.item_input, 1, 0, 1, 3)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(300, 10))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        Search.setCentralWidget(self.centralwidget)

        self.retranslateUi(Search)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"Search", None))
        self.search_btn.setText(QCoreApplication.translate("Search", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Search", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

