from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class TreeUi(object):
    def setupUi(self, Tree):
        if not Tree.objectName():
            Tree.setObjectName(u"Tree")
        Tree.resize(728, 558)
        self.centralwidget = QWidget(Tree)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1")
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setVisible(False)

        self.verticalLayout.addWidget(self.treeWidget)

        self.download_btn = QPushButton(self.centralwidget)
        self.download_btn.setObjectName(u"download_btn")

        self.verticalLayout.addWidget(self.download_btn)

        self.setting_btn = QPushButton(self.centralwidget)
        self.setting_btn.setObjectName(u"setting_btn")

        self.verticalLayout.addWidget(self.setting_btn)

        Tree.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tree)

        QMetaObject.connectSlotsByName(Tree)

    def retranslateUi(self, Tree):
        Tree.setWindowTitle(QCoreApplication.translate("Tree", u"MainWindow", None))
        self.download_btn.setText(QCoreApplication.translate("Tree", u"Download", None))
        self.setting_btn.setText(QCoreApplication.translate("Tree", u"Settings", None))
