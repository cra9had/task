from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(422, 231)
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 41))
        self.label.setObjectName("label")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(170, 80, 111, 21))
        self.change_btn.setObjectName("change_btn")
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setGeometry(QtCore.QRect(130, 130, 201, 21))
        self.login_input.setStyleSheet(".QLineEdit{\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(81, 82, 78);\n"
"}")
        self.login_input.setObjectName("login_input")
        self.pw_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pw_input.setGeometry(QtCore.QRect(130, 180, 201, 21))
        self.pw_input.setStyleSheet(".QLineEdit{\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(81, 82, 78);\n"
"}")
        self.pw_input.setObjectName("pw_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 60, 16))
        self.label_3.setObjectName("label_3")
        self.path_lable = QtWidgets.QLineEdit(self.centralwidget)
        self.path_lable.setGeometry(QtCore.QRect(90, 30, 301, 21))
        self.path_lable.setObjectName("path_lable")
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "MainWindow"))
        self.label.setText(_translate("Settings", "Save path:"))
        self.change_btn.setText(_translate("Settings", "Change"))
        self.label_2.setText(_translate("Settings", "Username"))
        self.label_3.setText(_translate("Settings", "Password"))
