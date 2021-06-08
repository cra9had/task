# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tree(object):
    def setupUi(self, Tree):
        if not Tree.objectName():
            Tree.setObjectName(u"Tree")
        Tree.resize(750, 607)
        Tree.setMinimumSize(QSize(722, 592))
        self.centralwidget = QWidget(Tree)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.open_file_btn = QPushButton(self.centralwidget)
        self.open_file_btn.setObjectName(u"open_file_btn")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.open_file_btn.setFont(font)
        self.open_file_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(26,115,232);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(27,102,201);\n"
"}")

        self.gridLayout_2.addWidget(self.open_file_btn, 6, 0, 1, 3)

        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setFont(font)
        self.download_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(26,115,232);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(27,102,201);\n"
"}")

        self.gridLayout_2.addWidget(self.download_btn, 3, 0, 1, 3)

        self.setting_btn = QPushButton(self.centralwidget)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy)
        self.setting_btn.setMinimumSize(QSize(100, 0))
        self.setting_btn.setFont(font)
        self.setting_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(26,115,232);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(27,102,201);\n"
"}")

        self.gridLayout_2.addWidget(self.setting_btn, 0, 0, 1, 1)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy1)
        self.status_label.setMinimumSize(QSize(0, 50))
        self.status_label.setSizeIncrement(QSize(0, 0))
        self.status_label.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.status_label.setFont(font1)
        self.status_label.setLayoutDirection(Qt.LeftToRight)
        self.status_label.setAutoFillBackground(False)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.status_label, 0, 1, 1, 1)

        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy2)
        self.treeWidget.header().setVisible(False)

        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 3)

        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setMinimumSize(QSize(100, 0))
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(26,115,232);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(27,102,201);\n"
"}")

        self.gridLayout_2.addWidget(self.back_btn, 0, 2, 1, 1)

        self.stop_btn = QPushButton(self.centralwidget)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(26,115,232);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(27,102,201);\n"
"}")

        self.gridLayout_2.addWidget(self.stop_btn, 4, 0, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        Tree.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tree)

        QMetaObject.connectSlotsByName(Tree)
    # setupUi

    def retranslateUi(self, Tree):
        Tree.setWindowTitle(QCoreApplication.translate("Tree", u"MainWindow", None))
        self.open_file_btn.setText(QCoreApplication.translate("Tree", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0424\u0430\u0439\u043b", None))
        self.download_btn.setText(QCoreApplication.translate("Tree", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.setting_btn.setText(QCoreApplication.translate("Tree", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.status_label.setText(QCoreApplication.translate("Tree", u"Status: Waiting", None))
        self.back_btn.setText(QCoreApplication.translate("Tree", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.stop_btn.setText(QCoreApplication.translate("Tree", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

