from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(471, 172)
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.change_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_btn.setGeometry(QtCore.QRect(152, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.change_btn.setFont(font)
        self.change_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(26,115,232);\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"    border: 1px solid rgb(26,115,232);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(27,102,201);\n"
"}")
        self.change_btn.setObjectName("change_btn")
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setGeometry(QtCore.QRect(80, 100, 191, 18))
        self.login_input.setStyleSheet(".QLineEdit{\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border: 1px solid white;\n"
"}")
        self.login_input.setObjectName("login_input")
        self.pw_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pw_input.setGeometry(QtCore.QRect(80, 70, 191, 18))
        self.pw_input.setStyleSheet(".QLineEdit{\n"
"    border-style: outset;\n"
"    border-radius: 5px;\n"
"    border: 1px solid white;\n"
"}")
        self.pw_input.setObjectName("pw_input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(2, 67, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 100, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(12, 137, 111, 19))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.theme_changer = QtWidgets.QCheckBox(self.centralwidget)
        self.theme_changer.setEnabled(True)
        self.theme_changer.setGeometry(QtCore.QRect(130, 130, 71, 31))
        self.theme_changer.setStyleSheet("QCheckBox::indicator:unchecked {\n"
"     image: url(images/switch_off.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"     image: url(images/switch_on.png);\n"
"}")
        self.theme_changer.setText("")
        self.theme_changer.setObjectName("theme_changer")
        self.path_lable = QtWidgets.QLineEdit(self.centralwidget)
        self.path_lable.setGeometry(QtCore.QRect(70, 10, 331, 20))
        self.path_lable.setObjectName("path_lable")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(2, 12, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Settings.setCentralWidget(self.centralwidget)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "MainWindow"))
        self.change_btn.setText(_translate("Settings", "Поменять"))
        self.label_3.setText(_translate("Settings", "Пароль"))
        self.label_2.setText(_translate("Settings", "Логин"))
        self.label_4.setText(_translate("Settings", "Темная"))
