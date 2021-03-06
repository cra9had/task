import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class TreeUi(object):
    def setupUi(self, Tree):
        if not Tree.objectName():
            Tree.setObjectName(u"Tree")
        Tree.resize(750, 607)
        Tree.setMinimumSize(QSize(722, 592))
        self.icon = QIcon("images/icon.ico")
        Tree.setWindowIcon(self.icon)
        self.centralwidget = QWidget(Tree)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.header().setVisible(False)

        self.gridLayout_2.addWidget(self.treeWidget, 1, 0, 1, 3)

        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy1)
        self.back_btn.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
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

        self.setting_btn = QPushButton(self.centralwidget)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy1.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy2)
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

        self.open_file_btn = QPushButton(self.centralwidget)
        self.open_file_btn.setObjectName(u"open_file_btn")
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
        self.tray_icon = QSystemTrayIcon(Tree)
        self.tray_icon.setIcon(self.icon)
        self.tray_icon.activated.connect(Tree.show_window)
        show_action = QAction("????????????????", Tree)
        quit_action = QAction("??????????????", Tree)
        hide_action = QAction("????????????????", Tree)
        show_action.triggered.connect(Tree.show_window)
        hide_action.triggered.connect(Tree.hide)
        quit_action.triggered.connect(sys.exit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.showMessage(
            "DOWNLOADER",
            "???????????? ?? ????????",
            QSystemTrayIcon.Information,
            2000
        )
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.gridLayout_2.addWidget(self.stop_btn, 4, 0, 1, 3)

        self.search_btn = QPushButton(self.centralwidget)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy1.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy1)
        self.search_btn.setMinimumSize(QSize(100, 0))
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.search_btn, 2, 2, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"}")
        self.progressBar.setValue(0)
        self.gridLayout_2.addWidget(self.progressBar, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        Tree.setCentralWidget(self.centralwidget)
        self.retranslateUi(Tree)
        QMetaObject.connectSlotsByName(Tree)

    def retranslateUi(self, Tree):
        Tree.setWindowTitle(QCoreApplication.translate("Tree", u"DOWNLOADER", None))
        self.back_btn.setText(QCoreApplication.translate("Tree", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.setting_btn.setText(QCoreApplication.translate("Tree", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.status_label.setText(QCoreApplication.translate("Tree", u"Status: Waiting", None))
        self.open_file_btn.setText(QCoreApplication.translate("Tree", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0424\u0430\u0439\u043b", None))
        self.download_btn.setText(QCoreApplication.translate("Tree", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.stop_btn.setText(QCoreApplication.translate("Tree", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.search_btn.setText(QCoreApplication.translate("Tree", u"\u041f\u043e\u0438\u0441\u043a", None))
