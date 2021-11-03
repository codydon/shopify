#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

import sys
import inventory as inventory
import AddStock as AddStock
import SearchManage as SearchManage
import login as login
import sales as sales
import AddPurchase as AddPurchase
import datetime
import sqlite3
currentdatetime = datetime.datetime.now()

try:
    connection = sqlite3.connect('shopify.db')
    c = connection.cursor()
    print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
    print("Error while connecting ")



#CLASSES
class LoginWindow(login.Ui_MainWindow, QtWidgets.QMainWindow):
        def __init__(self):
            super(LoginWindow,self).__init__()
            #setting up the first window
            self.setupUi(self)
            self.frame_error.hide()
            self.loginbtn.clicked.connect(self.Auth)
           
            
        stylePopupError = (
            "background-color: rgb(255, 85, 127); border-radius: 5px;")
        
       #Authentication         
        def Auth(self):
            # hinding the error message after some time
            def hideframe():
                self.frame_error.hide()
                
                 
            def showMessage(message):
                self.frame_error.show()
                self.label_error.setText(message)
                QtCore.QTimer.singleShot(5000,hideframe)
            c = connection.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS USERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                user_no  INTEGER UNIQUE NOT NULL,
                name VARCHAR NOT NULL,
                role VARCHAR NOT NULL,
                id_no INTEGER NOT NULL,
                dob DATE NOT NULL,
                gender VARCHAR NOT NULL,
                date_emp DATE NOT NULL,
                end_date DATE NOT NULL,
                remarks LONGTEXT NOT NULL,
                password VARCHAR NOT NULL)''')
            p = self.pin.text()
            c.execute("SELECT role FROM users WHERE password=?", (p,))
            for item in c:    
                role = item[0]
            d = connection.cursor()
            d.execute("SELECT COUNT(role) FROM users WHERE password=?", (p,))   
            for count in d:    
                n = count[0]
            if n == 0:
                text = "WRONG CREDENTIALS. TRY AGAIN!!"
                showMessage(text)
                self.frame_error.setStyleSheet(self.stylePopupError)
           
            elif role == "ADMIN":
                self.window = Main()
                self.window.show()
                self.hide()
            elif role == "CASHIER":
                self.window = salesWindow()
                self.window.show()
                self.hide()
            else:
                text = "WRONG CREDENTIALS. TRY AGAIN!!"
                showMessage(text)
                self.frame_error.setStyleSheet(self.stylePopupError)
                
            
class Main(inventory.Ui_MainWindow, QtWidgets.QMainWindow):
        def __init__(self):
                super(Main,self).__init__()
                #setting up the first window
                self.setupUi(self)
                #
       
                self.frame_ok.hide()
                self.pushButton_14.clicked.connect(self.AddStock)
                self.pushButton_3.clicked.connect(self.Addpurchase)
                self.Showstatus()
        stylePopupOk = (
            "background-color:green; border-radius: 5px;")
        def Showstatus(self):
            def hideframe():
                self.frame_ok.hide()
            def showMessage(message):
                self.frame_ok.show()
                self.label_ok.setText(message)
                QtCore.QTimer.singleShot(5000,hideframe)
            success = "You successfully logged in!!"
            showMessage(success)
            self.frame_ok.setStyleSheet(self.stylePopupOk)

        def AddStock(self):
            self.window = AddStockWindow()
            self.window.show()
        def Addpurchase(self):
            self.window=purchaseWindow()
            self.window.show()    

        

class salesWindow(sales.Ui_Sales, QtWidgets.QMainWindow):
    def __init__(self):
            super(salesWindow,self).__init__()
            #setting up the first window
            self.setupUi(self)


class purchaseWindow(AddPurchase.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(purchaseWindow, self).__init__()
        self.setupUi(self)
       
        self.pushButton_2.clicked.connect(self.recordpurchase)

    def recordpurchase(self):
        temp_date = self.dateEdit.date()
        var_date = temp_date.toPyDate()
        transactioncode = self.lineEdit_3.text()
        quantity = self.doubleSpinBox.text()
        supplier = self.lineEdit_6.text()
        remarks = self.textEdit.toPlainText()
        #db
        c = connection.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS PURCHASES (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            transactionCode  VARCHAR UNIQUE NOT NULL,
            quantity FLOAT NOT NULL,
            supplier VARCHAR NOT NULL,
            dateOfpurchase DATE NOT NULL,
            remarks LONGTEXT NOT NULL,
            daterecorded TIMESTAMP NOT NULL)''')

        #insert stock item
        try:
            sql = """INSERT INTO PURCHASES (transactionCode,quantity,supplier, dateOfPurchase,remarks,daterecorded ) 
                    VALUES (?, ?, ?, ?, ?, ?);"""
            vars = (transactioncode,quantity,
                    supplier, var_date, remarks,currentdatetime)
            c.execute(sql, vars,)
            connection.commit()
            c.close
            dialog("Purchase recorded Successfully")
        except:
            warn("The purchase already exists")
        self.dateEdit.setDate(QDate.currentDate())
        self.lineEdit_3.clear()
        self.doubleSpinBox.setValue(0.00)
        self.lineEdit_6.clear()
        self.textEdit.clear()

class AddStockWindow(AddStock.Ui_Dialog, QtWidgets.QDialog):
        def __init__(self):
                super(AddStockWindow,self).__init__()
                self.setupUi(self)
                #
                self.pushButton.clicked.connect(self.SearchManage)
                self.pushButton_2.clicked.connect(self.AddItem)

        def SearchManage(self):
            self.window = SearchManageWindow()
            self.window.show()

        def AddItem(self):            
            temp_date = self.dateEdit.date() 
            var_date = temp_date.toPyDate()
            item_code = self.lineEdit_3.text()
            category = self.comboBox.currentText()
            item_name = self.lineEdit_4.text()
            description = self.lineEdit_5.text()
            volume_weight = self.lineEdit_7.text()
            quantity = self.doubleSpinBox.text()
            price = self.spinBox.value()
            exp_temp = self.dateEdit_2.date()
            exp_date = exp_temp.toPyDate() 
            supplier = self.lineEdit_6.text()
            remarks = self.textEdit.toPlainText()
            #db
            c = connection.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS STOCK (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                item_code  VARCHAR UNIQUE NOT NULL,
                category VARCHAR NOT NULL,
                item_name VARCHAR NOT NULL,
                description VARCHAR NOT NULL,
                volume_weight VARCHAR NOT NULL,
                quantity FLOAT NOT NULL,
                price DOUBLE NOT NULL,
                supplier VARCHAR NOT NULL,
                date_added DATE NOT NULL,
                exp_date DATE NOT NULL,
                remarks LONGTEXT NOT NULL)''')

            #insert stock item
            try:
                sql = """INSERT INTO STOCK (item_code, category, item_name, description,volume_weight, quantity, price, supplier, date_added, exp_date, remarks ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                vars = (item_code, category, item_name, description,volume_weight, quantity, price, supplier, var_date, exp_date, remarks,)
                c.execute(sql, vars,)            
                connection.commit()
                c.close
                dialog("Item Saved Successfully")           
            except:
                warn("The Item Code already exists")
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.doubleSpinBox.setValue(0.00)
            self.spinBox.setValue(0)
            self.lineEdit_7.clear()
            self.textEdit.clear()
            #set default value of the combobox



    




class SearchManageWindow(SearchManage.Ui_Dialog, QtWidgets.QDialog):
        def __init__(self):
                super(SearchManageWindow,self).__init__()
                self.setupUi(self)

#informational msg
def dialog(w):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(w)
    msg.setWindowTitle("hint")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec()   
    
#warning msg   
def warn(w):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(w)
    msg.setWindowTitle("warning")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.exec()     

#APP LAUNCH
if __name__ == "__main__":
        #create an application
        app = QtWidgets.QApplication(sys.argv)
        w = LoginWindow()
        #show the window and start the app
        w.show()
        app.exec_()
