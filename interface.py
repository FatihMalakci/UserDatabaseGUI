# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.adduser = QtWidgets.QPushButton(self.centralwidget)
        self.adduser.setGeometry(QtCore.QRect(550, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adduser.setFont(font)
        self.adduser.setObjectName("adduser")
        self.pencere = QtWidgets.QListView(self.centralwidget)
        self.pencere.setGeometry(QtCore.QRect(10, 100, 441, 371))
        self.pencere.setObjectName("pencere")
        self.users = QtWidgets.QLabel(self.centralwidget)
        self.users.setGeometry(QtCore.QRect(170, 40, 161, 41))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.users.setFont(font)
        self.users.setObjectName("users")
        self.namebox = QtWidgets.QLineEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(480, 130, 101, 31))
        self.namebox.setObjectName("namebox")
        self.usercount = QtWidgets.QLCDNumber(self.centralwidget)
        self.usercount.setGeometry(QtCore.QRect(230, 490, 91, 41))
        self.usercount.setObjectName("usercount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 490, 181, 41))
        font = QtGui.QFont()
        font.setFamily("PT Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 550, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 90, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.sirnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.sirnamebox.setGeometry(QtCore.QRect(600, 130, 101, 31))
        self.sirnamebox.setObjectName("sirnamebox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 210, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.agebox = QtWidgets.QLineEdit(self.centralwidget)
        self.agebox.setGeometry(QtCore.QRect(480, 250, 101, 31))
        self.agebox.setObjectName("agebox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        self.menuUsers = QtWidgets.QMenu(self.menubar)
        self.menuUsers.setObjectName("menuUsers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMain_Window = QtWidgets.QAction(MainWindow)
        self.actionMain_Window.setObjectName("actionMain_Window")
        self.menubar.addAction(self.menuUsers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.adduser.setText(_translate("MainWindow", "Add User"))
        self.users.setText(_translate("MainWindow", "User List"))
        self.label_2.setText(_translate("MainWindow", "Number of Users"))
        self.label.setText(_translate("MainWindow", "The User Information is Provided by SQLite3 Database"))
        self.label_3.setText(_translate("MainWindow", "User Database by Fatih Malakçı"))
        self.label_4.setText(_translate("MainWindow", "github.com/fatihmalakci"))
        self.label_5.setText(_translate("MainWindow", "Enter User\'s Name/Sirname:"))
        self.label_6.setText(_translate("MainWindow", "Enter User\'s Age:"))
        self.menuUsers.setTitle(_translate("MainWindow", "Main Window"))
        self.actionMain_Window.setText(_translate("MainWindow", "Main Window"))

    def adduser(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

