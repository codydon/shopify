#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

import sys
import inventory as inventory
import AddStock as AddStock
import SearchManage as SearchManage

import sqlite3

try:
    connection = sqlite3.connect('shopify.db')
    c = connection.cursor()
    print("Database created and Successfully Connected to SQLite")
except sqlite3.Error as error:
    print("Error while connecting ")



#CLASSES
class Main(inventory.Ui_MainWindow, QtWidgets.QMainWindow):
        def __init__(self):
                super(Main,self).__init__()
                #setting up the first window
                self.setupUi(self)
                #
                self.pushButton_14.clicked.connect(self.AddStock)


        def AddStock(self):
            self.window = AddStockWindow()
            self.window.show()

        def showdialog(self):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("This is a message box")
            msg.setInformativeText("This is additional information")
            msg.setWindowTitle("MessageBox demo")
            msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec()

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
            item_name = self.lineEdit_4.text()
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
                item_name VARCHAR NOT NULL,
                quantity FLOAT NOT NULL,
                price DOUBLE NOT NULL,
                supplier VARCHAR NOT NULL,
                date_added DATE NOT NULL,
                exp_date DATE NOT NULL,
                remarks LONGTEXT NOT NULL)''')

            #insert stock item
            try:
                sql = """INSERT INTO STOCK (item_code, item_name, quantity, price, supplier, date_added, exp_date, remarks ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
                vars = (item_code, item_name, quantity, price, supplier, var_date, exp_date, remarks,)
                c.execute(sql, vars,)            
                connection.commit()            
            except sqlite3.Error as error:
                print("Item code already exists")

class SearchManageWindow(SearchManage.Ui_Dialog, QtWidgets.QDialog):
        def __init__(self):
                super(SearchManageWindow,self).__init__()
                self.setupUi(self)

        

#APP LAUNCH
if __name__ == "__main__":
        #create an application
        app = QtWidgets.QApplication(sys.argv)
        w = Main()
        #show the window and start the app
        w.show()
        app.exec_()