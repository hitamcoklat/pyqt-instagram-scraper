from PySide2.QtWidgets import QStackedWidget
from PySide2 import QtCore, QtGui, QtWidgets
from lib.ig_scrapper import IGScrapper
import csv
import time
from pathlib import Path
import webbrowser
from dialog_about import Ui_AboutWindow
from page.shopify_scrapper import MainWindow as ShopifyPage

class Ui_MainWindow(object):

    def __init__(self, show):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())

    def openWindowAbout(self):
        print('open window about')
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def loadDataInstagram(self):

        self.username = self.input_username.text()
        self.jmlData = self.comboBox_2.currentText()

        if(self.username == ''):
            return

        self.pilihanCombo = self.comboBox.currentText()
        self.btn_submit.setText("Loading...")

        d = IGScrapper(self.username, int(self.jmlData))

        if (self.pilihanCombo == 'Search Media By HashTag'):
            print('pencarian hashtag')
            self.dataMedia = d.get_medias_by_tag()
        else:
            print('pencarian username')
            self.dataMedia = d.get_account_medias_by_username()
            print(self.dataMedia)

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Link Instagram', 'Jml. Likes', 'Jml. Comments', 'Caption', 'Hashtags'])

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        # self.jmlFollower = IGScrapper.get_account_followers_by_username(self.username)
        self.tableWidget.setRowCount(0)

        row = 0
        for val in self.dataMedia:

            self.tableWidget.insertRow(row)

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val["linkInstagram"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(val["numberOfLikes"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val["numberOfComments"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(val["caption"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(val["hashtags"])))
            print(val["linkInstagram"])
            row = row + 1
            print(row)

    def exportCSV(self):

        try:
            with open("../data-scrape.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["No", "LINK INSTAGRAM", "JML. LIKE", "JML. COMMENT", "CAPTION", "HASHTAG"])

                row = 1
                for val in self.dataMedia:
                    writer.writerow([row, val["linkInstagram"], val["numberOfLikes"], val["numberOfComments"], val["caption"], val["hashtags"]])
                    row = row + 1
        except UnicodeEncodeError as x:
            pass

        filename = Path("./data-scrape.csv")
        webbrowser.open(filename.absolute().as_uri())

        # self.showDialogExport()

    def exportTXT(self):
        print('print ke text')
        with open("data-scrape-caption.txt", "a") as myfile:
            for val in self.dataMedia:
                myfile.write(val['caption'].lstrip().rstrip('\r\n'))

        self.showDialogExport()

    def gotoShopifyPage(self):
        self.close()
        w = ShopifyPage(self)
        w.show()

    def gotoInstagramPage(self):
        print('ke halaman Instagram')

    def showDialogExport(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("Data berhasil di export!")
        msg.setInformativeText("File disimpan di folder tempat aplikasi ini berada.")
        msg.setWindowTitle("Info")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 575)
        MainWindow.setFixedHeight(575)
        MainWindow.setFixedWidth(903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 901, 381))
        self.tableWidget.setSortingEnabled(True)

        self.input_username = QtWidgets.QLineEdit(self.centralwidget)
        self.input_username.setGeometry(QtCore.QRect(260, 440, 261, 41))
        self.input_username.setText("")
        self.input_username.setStyleSheet("padding-left: 20px; font-size: 18px; padding-right: 20px;")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(670, 390, 191, 41))
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 420, 221, 41))
        self.label_4.setStyleSheet("font-size: 18px; font-weight: bold; font-style: italic;")

        jml_list = ["10", "50", "100", "150", "200"]
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(558, 440, 86, 35))
        self.comboBox_2.setStyleSheet("font-weight: bold; text-align: center;")
        self.comboBox_2.addItems(jml_list)

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(670, 450, 191, 41))
        self.btn_submit.setText("Submit")
        self.btn_submit.setStyleSheet("font-size: 18px; font-weight: bold; background-color: green; color: white;")
        self.btn_submit.clicked.connect(lambda: self.loadDataInstagram())
        # self.btn_submit.clicked.connect(self.loadingDialog)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 400, 220, 17))
        self.label.setStyleSheet("font-weight: bold; font-size: 12px;")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 420, 271, 17))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)

        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(250, 390, 281, 101))
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(540, 390, 121, 101))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 410, 71, 17))
        self.label_3.setStyleSheet("font-size: 12px; font-weight: bold;")

        self.columnView_2.raise_()
        self.columnView.raise_()
        self.tableWidget.raise_()
        self.input_username.raise_()
        self.btn_submit.raise_()
        self.label.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuPage = QtWidgets.QMenu(self.menubar)
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        # self.actionExit = Q

        # Menu Top
        self.actionTable = QtWidgets.QAction(MainWindow)
        self.menuPageShopify = QtWidgets.QAction(MainWindow)
        self.menuPageInstagram = QtWidgets.QAction(MainWindow)
        self.actionChart = QtWidgets.QAction(MainWindow)
        self.actionPage = QtWidgets.QAction(MainWindow)
        self.actionAbout = QtWidgets.QAction(MainWindow)

        # Daftarkan ke list menu panel top
        self.menuExit.addAction(self.actionExit)
        self.menuView.addAction(self.actionTable)
        self.menuView.addAction(self.actionChart)

        self.menuPage.addAction(self.menuPageShopify)
        self.menuPage.addAction(self.menuPageInstagram)

        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrape Tools Lite Version"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Search By Username"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Search Media By HashTag"))
        self.label_4.setText(_translate("MainWindow", ".:Instagram Scraper:."))
        # self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Insert Username/Hashtag"))
        self.label_2.setText(_translate("MainWindow", "Instagram Account not be private"))
        self.label_3.setText(_translate("MainWindow", "Data Show"))
        self.menuExit.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Tools"))
        self.menuPage.setTitle(_translate("MainWindow", "Page"))
        self.menuPageShopify.setText(_translate("MainWindow", "Shopify"))
        self.menuPageInstagram.setText(_translate("MainWindow", "Instagram"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTable.setText(_translate("MainWindow", "Export CSV"))
        self.actionChart.setText(_translate("MainWindow", "Export Caption to TXT"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionTable.triggered.connect(self.exportCSV)
        self.actionChart.triggered.connect(self.exportTXT)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.openWindowAbout)
        self.menuPageShopify.triggered.connect(self.gotoShopifyPage)
        self.menuPageInstagram.triggered.connect(self.gotoInstagramPage)
