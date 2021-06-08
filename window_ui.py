from PySide2 import QtCore, QtGui, QtWidgets


class TreeUi(object):
    def setupUi(self, Tree):
        Tree.setObjectName("Tree")
        Tree.resize(728, 558)
        self.centralwidget = QtWidgets.QWidget(Tree)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 60, 701, 431))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(10, 500, 701, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.download_btn.setFont(font)
        self.download_btn.setStyleSheet("QPushButton {\n"
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
        self.download_btn.setObjectName("download_btn")
        self.open_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_btn.setGeometry(QtCore.QRect(10, 530, 701, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.open_file_btn.setFont(font)
        self.open_file_btn.setStyleSheet("QPushButton {\n"
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
        self.open_file_btn.setObjectName("open_file_btn")
        self.setting_btn = QtWidgets.QPushButton(self.centralwidget)
        self.setting_btn.setGeometry(QtCore.QRect(610, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.setting_btn.setFont(font)
        self.setting_btn.setStyleSheet("QPushButton {\n"
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
        self.setting_btn.setObjectName("setting_btn")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(110, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(11, 18, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("QPushButton {\n"
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
        self.back_btn.setObjectName("back_btn")
        Tree.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tree)
        QtCore.QMetaObject.connectSlotsByName(Tree)

    def retranslateUi(self, Tree):
        _translate = QtCore.QCoreApplication.translate
        Tree.setWindowTitle(_translate("Tree", "MainWindow"))
        self.download_btn.setText(_translate("Tree", "Download"))
        self.open_file_btn.setText(_translate("Tree", "Open file"))
        self.setting_btn.setText(_translate("Tree", "Настройки"))
        self.status_label.setText(_translate("Tree", "Status: Waiting"))
        self.back_btn.setText(_translate("Tree", "Назад"))
