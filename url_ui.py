from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Url(object):
    def setupUi(self, Url):
        if not Url.objectName():
            Url.setObjectName(u"Url")
        Url.setFixedSize(524, 547)
        font = QFont()
        font.setPointSize(9)
        Url.setFont(font)
        Url.setWindowIcon(QIcon("images/icon.ico"))
        self.centralwidget = QWidget(Url)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 10, 451, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.url_input = QLineEdit(self.verticalLayoutWidget)
        self.url_input.setObjectName(u"url_input")
        self.url_input.setStyleSheet(u"border-style: outset;\n"
"border-radius: 4px;\n"
"border: 1px solid black;")

        self.verticalLayout.addWidget(self.url_input)

        self.ok_btn = QPushButton(self.verticalLayoutWidget)
        self.ok_btn.setObjectName(u"ok_btn")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(12)
        self.ok_btn.setFont(font1)
        self.ok_btn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.ok_btn)

        self.last_urls = QListWidget(self.verticalLayoutWidget)
        self.last_urls.setObjectName(u"last_urls")

        self.verticalLayout.addWidget(self.last_urls)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delete_url_btn = QPushButton(self.verticalLayoutWidget)
        self.delete_url_btn.setObjectName(u"delete_url_btn")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.delete_url_btn.setFont(font2)
        self.delete_url_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 0, 4);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 2);\n"
"}")

        self.horizontalLayout.addWidget(self.delete_url_btn)

        self.add_url_btn = QPushButton(self.verticalLayoutWidget)
        self.add_url_btn.setObjectName(u"add_url_btn")
        self.add_url_btn.setFont(font2)
        self.add_url_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(95, 198, 71);\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 126, 21);\n"
"}")

        self.horizontalLayout.addWidget(self.add_url_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.loading_label = QLabel(self.centralwidget)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setEnabled(True)
        self.loading_label.setGeometry(QRect(130, 500, 251, 41))
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.hide()
        Url.setCentralWidget(self.centralwidget)

        self.retranslateUi(Url)

        QMetaObject.connectSlotsByName(Url)
    # setupUi

    def retranslateUi(self, Url):
        Url.setWindowTitle(QCoreApplication.translate("Url", u"DOWNLOADER", None))
        self.label.setText(QCoreApplication.translate("Url", u"<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 URL:</span></p></body></html>", None))
        self.ok_btn.setText(QCoreApplication.translate("Url", u"Ok", None))
        self.delete_url_btn.setText(QCoreApplication.translate("Url", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.add_url_btn.setText(QCoreApplication.translate("Url", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u043b\u043e\u0433", None))
        self.loading_label.setText(QCoreApplication.translate("Url", u"<h1>\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430</h1>", None))
    # retranslateUi

