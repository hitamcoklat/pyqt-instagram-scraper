# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form-ig.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QProgressBar, QMessageBox
from PySide2.QtCore import QBasicTimer
from lib.ig_scrapper import IGScrapper
import csv
import time

class Ui_MainWindow(object):

    def loadDataInstagram(self):

        self.username = self.input_username.text()
        self.jmlData = self.input_jml_data.text()

        self.pilihanCombo = self.comboBox.currentText()
        time.sleep(3)
        self.btn_submit.setText("Loading...")

        if (self.pilihanCombo == 'Search Media By HashTag'):
            print('pencarian hashtag')
            self.dataMedia = IGScrapper.get_medias_by_tag(
                self.username, int(self.jmlData))
        else:
            print('pencarian username')
            self.dataMedia = IGScrapper.get_account_medias_by_username(
                self.username, int(self.jmlData))
            print(self.dataMedia)

        self.btn_submit.setText("Submit")
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
        print('print ke excell')

        with open('data-scrape.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["No", "LINK INSTAGRAM", "JML. LIKE", "JML. COMMENT", "CAPTION", "HASHTAG"])

            row = 1
            for val in self.dataMedia:
                writer.writerow([row, val["linkInstagram"], val["numberOfLikes"], val["numberOfComments"], val["caption"], val["hashtags"]])
                row = row + 1

    def exportTXT(self):
        print('print ke text')
        with open("data-scrape-caption.txt", "a") as myfile:
            for val in self.dataMedia:
                myfile.write(val['caption'].lstrip().rstrip('\r\n'))

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


        self.input_username = QtWidgets.QLineEdit(self.centralwidget)
        self.input_username.setGeometry(QtCore.QRect(260, 440, 261, 41))
        self.input_username.setText("")
        self.input_username.setObjectName("input_username")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(670, 390, 191, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 420, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(670, 450, 191, 41))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(lambda: self.loadDataInstagram())
        # self.btn_submit.clicked.connect(self.loadingDialog)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 400, 220, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.input_jml_data = QtWidgets.QLineEdit(self.centralwidget)
        self.input_jml_data.setGeometry(QtCore.QRect(550, 440, 101, 41))
        self.input_jml_data.setToolTip("")
        self.input_jml_data.setAutoFillBackground(False)
        self.input_jml_data.setText("")
        self.input_jml_data.setObjectName("input_jml_data")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 420, 271, 17))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(250, 390, 281, 101))
        self.columnView.setObjectName("columnView")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(540, 390, 121, 101))
        self.columnView_2.setObjectName("columnView_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 410, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.columnView_2.raise_()
        self.columnView.raise_()
        self.tableWidget.raise_()
        self.input_username.raise_()
        self.btn_submit.raise_()
        self.label.raise_()
        self.input_jml_data.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        # self.actionExit = Q

        self.actionTable = QtWidgets.QAction(MainWindow)
        self.actionTable.setObjectName("actionTable")
        self.actionChart = QtWidgets.QAction(MainWindow)
        self.actionChart.setObjectName("actionChart")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuExit.addAction(self.actionExit)
        self.menuView.addAction(self.actionTable)
        self.menuView.addAction(self.actionChart)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        # self.actionTable.trigger(self.exportCSV)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instagram Tools"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Search By Username"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Search Media By HashTag"))
        self.label_4.setText(_translate("MainWindow", ".:Instagram Scraper:."))
        self.btn_submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Masukan Username/Hashtag"))
        self.label_2.setText(_translate("MainWindow", "Pastikan user instagram tidak private"))
        self.label_3.setText(_translate("MainWindow", "Jml. Data"))
        self.menuExit.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Tools"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTable.setText(_translate("MainWindow", "Export CSV"))
        self.actionChart.setText(_translate("MainWindow", "Export Caption to TXT"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

        # self.actionTable.cl

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionTable.triggered.connect(self.exportCSV)
        self.actionChart.triggered.connect(self.exportTXT)
        self.actionExit.triggered.connect(self.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
