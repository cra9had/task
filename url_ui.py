from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Url(object):
    def setupUi(self, Url):
        Url.setObjectName("Url")
        Url.resize(524, 547)
        font = QtGui.QFont()
        font.setPointSize(9)
        Url.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Url)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 451, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.url_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.url_input.setStyleSheet("border-style: outset;\n"
"border-radius: 4px;\n"
"border: 1px solid white;")
        self.url_input.setObjectName("url_input")
        self.verticalLayout.addWidget(self.url_input)
        self.ok_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26,115,232);\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(27,102,201);\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn)
        self.last_urls = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.last_urls.setObjectName("last_urls")
        self.verticalLayout.addWidget(self.last_urls)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_url_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.delete_url_btn.setFont(font)
        self.delete_url_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 0, 4);\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(170, 0, 2);\n"
"}")
        self.delete_url_btn.setObjectName("delete_url_btn")
        self.horizontalLayout.addWidget(self.delete_url_btn)
        self.add_url_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.add_url_btn.setFont(font)
        self.add_url_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(95, 198, 71);\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 126, 21);\n"
"}")
        self.add_url_btn.setObjectName("add_url_btn")
        self.horizontalLayout.addWidget(self.add_url_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.loading_label = QtWidgets.QLabel(self.centralwidget)
        self.loading_label.setEnabled(True)
        self.loading_label.setGeometry(QtCore.QRect(130, 500, 251, 41))
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setObjectName("loading_label")
        self.loading_label.hide()
        Url.setCentralWidget(self.centralwidget)

        self.retranslateUi(Url)
        QtCore.QMetaObject.connectSlotsByName(Url)

    def retranslateUi(self, Url):
        _translate = QtCore.QCoreApplication.translate
        Url.setWindowTitle(_translate("Url", "MainWindow"))
        self.label.setText(_translate("Url", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">Введите URL:</span></p></body></html>"))
        self.ok_btn.setText(_translate("Url", "Ok"))
        self.delete_url_btn.setText(_translate("Url", "Удалить URL"))
        self.add_url_btn.setText(_translate("Url", "Добавить URL"))
        self.loading_label.setText(_translate("Url", "<h1>Загрузка</h1>"))
