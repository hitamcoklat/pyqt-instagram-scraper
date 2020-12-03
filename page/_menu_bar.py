from PyQt5 import QtCore
from PySide2 import QtWidgets
from page.page_ig import MainWindow

class MenuBar:

    def __init__(self):
        super()
        self.mainView()

    def mainView(self):

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuPage = QtWidgets.QMenu(self.menubar)
        self.menuPage.setObjectName("menuPage")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        # self.actionExit = Q

        # Menu Top
        self.actionTable = QtWidgets.QAction(MainWindow)
        self.actionTable.setObjectName("actionTable")
        self.menuPageShopify = QtWidgets.QAction(MainWindow)
        self.menuPageShopify.setObjectName("menuPageShopify")
        self.actionChart = QtWidgets.QAction(MainWindow)
        self.actionChart.setObjectName("actionChart")
        self.actionPage = QtWidgets.QAction(MainWindow)
        self.actionPage.setObjectName("actionPage")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        # Daftarkan ke list menu panel top
        self.menuExit.addAction(self.actionExit)
        self.menuView.addAction(self.actionTable)
        self.menuView.addAction(self.actionChart)
        self.menuPage.addAction(self.menuPageShopify)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.menuExit.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Tools"))
        self.menuPage.setTitle(_translate("MainWindow", "Page"))
        self.menuPageShopify.setText(_translate("MainWindow", "Shopify"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTable.setText(_translate("MainWindow", "Export CSV"))
        self.actionChart.setText(_translate("MainWindow", "Export Caption to TXT"))
        self.actionAbout.setText(_translate("MainWindow", "About"))