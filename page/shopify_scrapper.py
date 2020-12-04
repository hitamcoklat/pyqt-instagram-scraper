import csv
import webbrowser
from pathlib import Path
from PySide2 import QtCore, QtGui, QtWidgets
from lib.shopify_scrapper import ShopifyScrape

class Ui_MainWindow(object):

    def __init__(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())

    def getData(self):
        print('submit shopify')
        shopName = self.plainTextEdit.toPlainText()
        jmlData = self.comboBox_2.currentText()

        if(shopName == ''):
            return

        s = ShopifyScrape(int(jmlData))
        self.dataMedia = s.main(shopName)

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Code', 'Collection', 'Category', 'Name', 'Variant Name', 'Price', 'In Stock', 'URL', 'Image URL'])

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget.setRowCount(0)

        row = 0
        for val in self.dataMedia:

            self.tableWidget.insertRow(row)

            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(val["code"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(val["collection"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(val["category"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(val["name"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(val["variantName"])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(val["price"])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(val["inStock"])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(val["URL"])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(val["imageURL"])))

            row += 1

    def gotoShopifyPage(self):
        return

    def gotoInstagramPage(self):
        from page.page_ig import MainWindow
        self.close()
        w = MainWindow(self)
        w.show()

    def exportCSV(self):

        try:
            with open("./data-scrape.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['No', 'Code', 'Collection', 'Category', 'Name', 'Variant Name', 'Price', 'In Stock', 'URL', 'Image URL'])

                row = 1
                for val in self.dataMedia:
                    writer.writerow([row, val["code"], val["collection"], val["category"], val["name"], val["variantName"], val["price"], val["inStock"], val["URL"], val["imageURL"]])
                    row +=1
        except UnicodeEncodeError as x:
            pass

        filename = Path("./data-scrape.csv")
        webbrowser.open(filename.absolute().as_uri())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 575)
        MainWindow.setFixedHeight(575)
        MainWindow.setFixedWidth(903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 901, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(700, 390, 191, 121))
        self.btn_submit.setStyleSheet("font-size: 24px; font-weight: bold; background-color: green; color: white;")
        self.btn_submit.setObjectName("btn_submit")

        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(260, 390, 301, 121))
        self.columnView.setObjectName("columnView")

        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(570, 390, 121, 121))
        self.columnView_2.setObjectName("columnView_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 400, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 430, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        jml_list = ["10", "50", "100", "150", "200"]
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(588, 440, 86, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(jml_list)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(270, 430, 281, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 410, 141, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.columnView_2.raise_()
        self.columnView.raise_()
        self.tableWidget.raise_()
        self.btn_submit.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.plainTextEdit.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        # self.actionExit = Q

        # Menu Top
        self.actionTable = QtWidgets.QAction(MainWindow)
        self.actionTable.setObjectName("actionTable")

        self.menuPageShopify = QtWidgets.QAction(MainWindow)
        self.menuPageShopify.setObjectName("menuPageShopify")

        self.menuPageInstagram = QtWidgets.QAction(MainWindow)
        self.menuPageInstagram.setObjectName("menuPageInstagram")

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
        self.menuPage.addAction(self.menuPageInstagram)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.btn_submit.clicked.connect(lambda: self.getData())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrape Tools Lite Version"))
        self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "Max Data"))
        self.label_4.setText(_translate("MainWindow", ".:Shopify Scraper:."))
        self.label_5.setText(_translate("MainWindow", "Input Shop Name"))
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
        self.menuPageShopify.triggered.connect(self.gotoShopifyPage)
        self.menuPageInstagram.triggered.connect(self.gotoInstagramPage)
        print('ke halaman shopify')