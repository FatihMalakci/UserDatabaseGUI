from PyQt5 import QtCore, QtGui, QtWidgets
import database
from database import connectdatabase
import sqlite3
import time


class Ui_MainWindow(object):

#Function for warning massages.

    def warningmessages(self, message):
        self.warningmassage.setText(f'{message}')

# Function for loading our data.

    def loaddata(self):
        self.Databasenamelabel.setText(database.databasename())
        # connection = sqlite3.connect('users.db')
        query = "SELECT * FROM users"
        # connection.execute(query)
        result = connectdatabase('users.db').execute(query)
        self.pencere.setRowCount(0)
        self.pencere.setAutoScroll(True)
        self.pencere.setHorizontalHeaderLabels(('Name','Sirname','Age','Phone'))
        self.pencere.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        for row_number, row_data in enumerate(result):
            self.pencere.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.pencere.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

# Function for making the add user button work.

    def adduserbutton(self):
        check = database.checkuser(self.namebox.text(),self.sirnamebox.text())
        if self.namebox.text() == '' or self.sirnamebox.text() == '' or self.agebox.text() == '' or self.phonebox.text() == '':
            self.warningmessages("Error! Please fill all the areas!")
        elif check == True:
            self.warningmassage.setText('Error! User already exists!')
        else:
            database.insertuser(self.namebox.text(),self.sirnamebox.text(),self.agebox.text(),self.phonebox.text())
            self.warningmessages('User Added Successfully.')
            self.loadusersbtn.click()
            self.usercount.display(database.countusers())
            self.namebox.setText("")
            self.sirnamebox.setText("")
            self.agebox.setText("")
            self.phonebox.setText("")


# Function for making the delete user button work.

    def deleteuserbutton(self):
        check = database.checkuser(self.namebox.text(), self.sirnamebox.text())
        if self.namebox.text() == '' or self.sirnamebox.text() == '':
            self.warningmessages('Error! Please fill name and sirname areas!')
        elif check == False:
            self.warningmessages("Error! User does not exists!")
        else:
            self.warningmessages(f'User {self.namebox.text()} {self.sirnamebox.text()} Deleted Successfully.')
            database.deleteuser(self.namebox.text(),self.sirnamebox.text())
            self.loadusersbtn.click()
            self.usercount.display(database.countusers())
            self.namebox.setText("")
            self.sirnamebox.setText("")
            self.agebox.setText("")
            self.phonebox.setText("")


# General UI Setting.

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.adduserbtn = QtWidgets.QPushButton(self.centralwidget)
        self.adduserbtn.setGeometry(QtCore.QRect(480, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adduserbtn.setFont(font)
        self.adduserbtn.setObjectName("adduserbtn")

        # This is for calling adduserbutton function when add user button is pressed.
        self.adduserbtn.clicked.connect(self.adduserbutton)

        self.deluserbtn = QtWidgets.QPushButton(self.centralwidget)
        self.deluserbtn.setGeometry(QtCore.QRect(630, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deluserbtn.setFont(font)
        self.deluserbtn.setObjectName("deluserbtn")

        # This is for calling deleteuserbutton function when delete user button is pressed.
        self.deluserbtn.clicked.connect(self.deleteuserbutton)

        self.pencere = QtWidgets.QTableWidget(self.centralwidget)
        self.pencere.setGeometry(QtCore.QRect(10, 100, 441, 361))
        self.pencere.setRowCount(11)
        self.pencere.setColumnCount(4)
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
        self.namebox.setGeometry(QtCore.QRect(480, 180, 101, 31))
        self.namebox.setObjectName("namebox")
        self.usercount = QtWidgets.QLCDNumber(self.centralwidget)
        self.usercount.setGeometry(QtCore.QRect(230, 490, 91, 41))
        self.usercount.setObjectName("usercount")

        self.usercount.display(database.countusers()) # This makes the user count lcd display work.

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
        self.label.setGeometry(QtCore.QRect(500, 530, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 0, 230, 31))
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
        self.label_5.setGeometry(QtCore.QRect(480, 140, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.sirnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.sirnamebox.setGeometry(QtCore.QRect(610, 180, 101, 31))
        self.sirnamebox.setObjectName("sirnamebox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 250, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.agebox = QtWidgets.QLineEdit(self.centralwidget)
        self.agebox.setGeometry(QtCore.QRect(480, 300, 101, 31))
        self.agebox.setObjectName("agebox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(630, 250, 151, 21))
        self.warningmassage = QtWidgets.QLabel(self.centralwidget)
        self.warningmassage.setGeometry(QtCore.QRect(460, 420, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.warningmassage.setFont(font)
        self.warningmassage.setAutoFillBackground(False)
        self.warningmassage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.warningmassage.setText("")
        self.warningmassage.setObjectName("warningmassage")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.phonebox = QtWidgets.QLineEdit(self.centralwidget)
        self.phonebox.setGeometry(QtCore.QRect(630, 300, 101, 31))
        self.phonebox.setObjectName("phonebox")
        self.loadusersbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loadusersbtn.setGeometry(QtCore.QRect(660, 60, 91, 31))
        self.loadusersbtn.setObjectName("loadusersbtn")

        self.loadusersbtn.clicked.connect(self.loaddata) # This makes load data button work.

        self.Databasenamelabel = QtWidgets.QLabel(self.centralwidget)
        self.Databasenamelabel.setGeometry(QtCore.QRect(540, 560, 250, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Databasenamelabel.setFont(font)
        self.Databasenamelabel.setText("")
        self.Databasenamelabel.setObjectName("Databasenamelabel")
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
        self.loadusersbtn.click()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SSS", "User Database GUI by Fatih Malakçı"))
        self.adduserbtn.setText(_translate("MainWindow", "Add User"))
        self.deluserbtn.setText(_translate("MainWindow", "Delete User"))
        self.users.setText(_translate("MainWindow", "User List"))
        self.label_2.setText(_translate("MainWindow", "Number of Users:"))
        self.label.setText(_translate("MainWindow", "The User Information is Provided by SQLite3 Database"))
        self.label_3.setText(_translate("MainWindow", "User Database GUI by Fatih Malakçı"))
        self.label_4.setText(_translate("MainWindow", "github.com/fatihmalakci"))
        self.label_5.setText(_translate("MainWindow", "Enter User\'s Name/Sirname:"))
        self.label_6.setText(_translate("MainWindow", "Enter User\'s Age:"))
        self.label_7.setText(_translate("MainWindow", "Enter User\'s Phone:"))
        self.loadusersbtn.setText(_translate("MainWindow", "Load Users"))
        self.menuUsers.setTitle(_translate("", ""))
        self.actionMain_Window.setText(_translate("MainWindow", "Main Window"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

