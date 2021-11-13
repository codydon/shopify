#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

import sys
import inventory as inventory
import AddStock as AddStock
import AddCategory as AddCategory
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
                self.pushButton_2.clicked.connect(
                    lambda: self.stackedWidget.setCurrentWidget(self.page_2))
                self.pushButton.clicked.connect(
                    lambda: self.stackedWidget.setCurrentWidget(self.page))
                self.radioButton_6.setChecked(True)
                self.lineEdit_4.textChanged.connect(self.radio_selected)
                self.pushButton_16.clicked.connect(self.delete_product)
                self.pushButton_15.clicked.connect(self.edit_product)
                self.tableWidget_2.selectionModel().selectionChanged.connect(self.on_select)
            #self.field.returnPressed.connect(self.radio_selected)
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

        def on_select(self, selected):
            for ix in selected.indexes():
                #print('selected cell location row : {0}, column: {1}'.format(ix.row(), ix.column()))
                global current_row
                current_row = self.tableWidget_2.currentRow()
                #print(current_row)
                global cell_value
                cell_value = self.tableWidget_2.item(current_row, 0).text()
                break

        def delete_product(self):
            #cell_value = self.tableWidget.item(current_row, 0).text()
            try:
                q = ("DELETE FROM stock WHERE id = ?;")
                c.execute(q, [cell_value])
                connection.commit()
                dialog("Item deleted from stock successfully!")
            except:
                warn("Error on delete!")
            self.radio_selected()

        def edit_product(self):
            p_id = cell_value
            current_column = self.tableWidget_2.currentColumn()
            if current_column == 1:
                column = 'item_code'
            elif current_column == 2:
                column = 'category'
            elif current_column == 3:
                column = 'item_name'
            elif current_column == 4:
                column = 'description'
            elif current_column == 5:
                column = 'measurement'
            elif current_column == 6:
                column = 'quantity'
            elif current_column == 7:
                column = 'price'
            elif current_column == 8:
                column = 'supplier'
            elif current_column == 9:
                column = 'date_added'
            elif current_column == 10:
                column = 'exp_date'
            elif current_column == 11:
                column = 'remarks'
            else:
                column = ' '
            current_text = self.tableWidget_2.item(
                current_row, current_column).text()
            if current_column > 1:
                try:
                    q = ("UPDATE  stock SET ("+column+") = ? WHERE id = ?;")
                    c.execute(q, [current_text, p_id])
                    connection.commit()
                    dialog("Stock updated successfully!")
                except:
                    warn("Error on update!")
            else:
                warn("wrong choice. try again!")
            self.radio_selected()

        def radio_selected(self):
            user_inp = self.lineEdit_4.text()
            if self.radioButton_6.isChecked():
                clmn = 'item_name'
            elif self.radioButton_12.isChecked():
                clmn = 'supplier'
            elif self.radioButton_11.isChecked():
                clmn = 'item_code'
            elif self.radioButton_10.isChecked():
                clmn = 'exp_date'
            elif self.radioButton_9.isChecked():
                clmn = 'date_added'
            elif self.radioButton_8.isChecked():
                clmn = 'price'
            elif self.radioButton_7.isChecked():
                clmn = 'category'
            else:
                user_inp = ''

            query = (" SELECT * FROM STOCK WHERE ("+clmn+") LIKE ( ? ||'%'); ")
            r = c.execute(query, [user_inp])
            res = r.fetchall()
            #results = res[0]
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setColumnCount(12)
            self.tableWidget_2.setHorizontalHeaderLabels(
                ['id', 'item_code', 'category', 'item_name', 'description', 'measurement', 'quantity', 'price', 'supplier', 'date_added', 'exp_date', 'remarks'])
            self.tableWidget_2.hideColumn(0)
            for row_number, row_data in enumerate(res):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(
                        row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



        

class salesWindow(sales.Ui_Sales, QtWidgets.QMainWindow):
    def __init__(self):
            super(salesWindow,self).__init__()
            #setting up the first window
            self.setupUi(self)


class purchaseWindow(AddPurchase.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(purchaseWindow, self).__init__()
        self.setupUi(self)
        #connect btns
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

            global cb_stock
            cb_stock = self.comboBox

            d = connection.cursor()
            d.execute('''CREATE TABLE IF NOT EXISTS CATEGORIES (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                category  VARCHAR UNIQUE NOT NULL )''')
            d.close()
            c.execute("SELECT category FROM categories ORDER BY category ASC;")
            rows = c.fetchall()
            for row in rows:
                    self.comboBox.addItem(str(row[0]))
            #
            
            self.pushButton_2.clicked.connect(self.AddItem)
            self.pushButton_3.clicked.connect(self.addcatg)

        def addcatg(self):
            self.window = AddCategoryWindow()
            self.window.show()

        def AddItem(self):
            temp_date = self.dateEdit.date() 
            var_date = temp_date.toPyDate()
            item_code = self.lineEdit_3.text()
            category = self.comboBox.currentText()
            item_name = self.lineEdit_4.text()
            description = self.lineEdit_5.text()
            measurement = self.lineEdit_7.text()
            quantity = self.doubleSpinBox.value()
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
                measurement VARCHAR NOT NULL,
                quantity FLOAT NOT NULL,
                price DOUBLE NOT NULL,
                supplier VARCHAR NOT NULL,
                date_added DATE NOT NULL,
                exp_date DATE ,
                remarks LONGTEXT)''')
            if not item_code:
                warn("item code is missing!")
            elif not item_name:
                warn("item name is missing!")
            elif not category:
                warn("Item category  is missing!")
            elif not description:
                warn("Item description  is missing!")
            elif not measurement:
                warn("Item measurement  is missing!")
            elif quantity <= 0:
                warn("please input number of items!")
            elif not supplier:
                warn("Item supplier is missing!")
            else:
                #insert stock item
                try:
                    sql = """INSERT INTO STOCK (item_code, category, item_name, description,measurement, quantity, price, supplier, date_added, exp_date, remarks ) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                    vars = (item_code, category, item_name, description,measurement, quantity, price, supplier, var_date, exp_date, remarks,)
                    c.execute(sql, vars,)            
                    connection.commit()
                    c.close
                    dialog("Item Saved Successfully")           
                except:                    
                    warn("The Item Code already exists")
                self.lineEdit_3.clear()
                self.lineEdit_4.clear()
                self.lineEdit_5.clear()
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.comboBox.set('')
                self.doubleSpinBox.setValue(0.00)
                self.spinBox.setValue(0)
                self.lineEdit_7.clear()
                self.textEdit.clear()
        

           
            #set default value of the combobox


class AddCategoryWindow(AddCategory.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(AddCategoryWindow,self).__init__()
        self.setupUi(self)
        #connect buttons
        self.pushButton.clicked.connect(self.addcategory)

    def addcategory(self):
        cname = self.lineEdit.text()
        d = connection.cursor()
        d.execute('''CREATE TABLE IF NOT EXISTS CATEGORIES (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                category  VARCHAR UNIQUE NOT NULL )''')
        d.close()

        c = connection.cursor()
        if not cname:
                warn("category name is missing!")
        else:
            try:
                sql = """INSERT INTO categories(category) VALUES (?);"""
                v = (cname,)
                c.execute(sql, v)            
                connection.commit()
                try:
                    c.execute("SELECT category FROM categories ORDER BY category ASC;")
                    rows = c.fetchall()
                    for row in rows:
                        cb_stock.addItem(str(row[0]))
                        connection.commit()
                    
                except Exception as e:
                    warn("The sync not done!!!")
                    print("the sync not done!!", e)

                dialog("Category Saved Successfully")           
            except:                    
                warn("The category already exists. Try again!")
            
            self.lineEdit.clear()
        



       
        
            
            


#informational msg
def dialog(w):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(w)
    msg.setWindowTitle("notification")
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

