#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

import sys
import inventory as inventory
import AddStock as AddStock
import AddCategory as AddCategory
import AddSupplier as AddSupplier
import login as login
import sales as sales
import AddPurchase as AddPurchase
import InventoryReport as InventoryReport
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
                self.pushButton_10.clicked.connect(self.inventoryReport)
                self.pushButton_14.clicked.connect(self.AddStock)
                self.pushButton_3.clicked.connect(self.Addpurchase)
                self.pushButton_11.clicked.connect(
                    lambda: self.stackedWidget.setCurrentWidget(self.page_2))
                self.pushButton.clicked.connect(
                    lambda: self.stackedWidget.setCurrentWidget(self.page))
                self.radioItemName.setChecked(True)
                self.lineSearchProduct.textChanged.connect(self.radio_selected)
                self.deleteStockBtn.clicked.connect(self.delete_product)
                self.updateStockBtn.clicked.connect(self.edit_product)
                self.stockTable.selectionModel().selectionChanged.connect(self.on_select)
                self.Showstatus()
                if self.lineSearchProduct.text() == '':
                    query = (" SELECT * FROM STOCK; ")
                    r = c.execute(query)
                    res = r.fetchall()
                    self.stockTable.setRowCount(0)
                    self.stockTable.setColumnCount(12)
                    self.stockTable.setHorizontalHeaderLabels(
                        ['id', 'item_code', 'category', 'item_name', 'description', 'measurement', 'quantity', 'price', 'supplier', 'date_added', 'exp_date', 'remarks'])
                    self.stockTable.hideColumn(0)
                    for row_number, row_data in enumerate(res):
                        self.stockTable.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.stockTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

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
#open InventoryReport Window
        def inventoryReport(self):
            self.window = InventoryReport()
            self.window.show()

        def AddStock(self):
            self.window = AddStockWindow()
            self.window.show()

        def Addpurchase(self):
            self.window=purchaseWindow()
            self.window.show()
        global cell_value
        cell_value = ''
        global current_row
        current_row = -1
        def on_select(self, selected):
            for ix in selected.indexes():
                print('selected cell location row : {0}, column: {1}'.format(ix.row(), ix.column()))
                global current_row
                current_row = self.stockTable.currentRow()
                print(current_row)
                global cell_value
                cell_value = self.stockTable.item(current_row, 0).text()
                break

        def delete_product(self):
            #cell_value = self.tableWidget.item(current_row, 0).text()
            if cell_value:
                try:
                    q = ("DELETE FROM stock WHERE id = ?;")
                    c.execute(q, [cell_value])
                    connection.commit()
                    dialog("Item deleted from stock successfully!")
                except:
                    warn("Error on delete!")
                self.radio_selected()
            else:
                warn("No row chosen!")

        def edit_product(self):
            try:
                p_id = cell_value
                current_column = self.stockTable.currentColumn()
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
                current_txt = self.stockTable.item(current_row, current_column)
                if current_txt:
                    current_text = current_txt.text()
                else:
                    current_text = ''
                    asd = -1
                    warn("No value chosen!")
                print(current_column)
                #if cell_value != '' and current_row != -1:
                if asd != -1 :
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
                    #else:
                    #        warn("wrong choice. try again!")
                    self.radio_selected()
            except Exception as e:
                print("error", e)

        def radio_selected(self):
            user_inp = self.lineSearchProduct.text()
            if self.radioItemName.isChecked():
                clmn = 'item_name'
            elif self.radioSupplier.isChecked():
                clmn = 'supplier'
            elif self.radioItemCode.isChecked():
                clmn = 'item_code'
            elif self.radioExpiryDate.isChecked():
                clmn = 'exp_date'
            elif self.radioDateAdded.isChecked():
                clmn = 'date_added'
            elif self.radioPrice.isChecked():
                clmn = 'price'
            elif self.radioCategory.isChecked():
                clmn = 'category'
            else:
                user_inp = ''

            query = (" SELECT * FROM STOCK WHERE ("+clmn+") LIKE ( ? ||'%'); ")
            r = c.execute(query, [user_inp])
            res = r.fetchall()
            #results = res[0]
            self.stockTable.setRowCount(0)
            self.stockTable.setColumnCount(12)
            self.stockTable.setHorizontalHeaderLabels(
                ['id', 'item_code', 'category', 'item_name', 'description', 'measurement', 'quantity', 'price', 'supplier', 'date_added', 'exp_date', 'remarks'])
            self.stockTable.hideColumn(0)
            for row_number, row_data in enumerate(res):
                self.stockTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.stockTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        def show_expiry(self):
            query = (" SELECT * FROM STOCK; ")
            r = c.execute(query)
            res = r.fetchall()
            self.stockTable.setRowCount(0)
            self.stockTable.setColumnCount(12)
            self.stockTable.setHorizontalHeaderLabels(
                ['id', 'item_code', 'category', 'item_name', 'description', 'measurement', 'quantity', 'price', 'supplier', 'date_added', 'exp_date', 'remarks'])
            self.stockTable.hideColumn(0)
            for row_number, row_data in enumerate(res):
                self.stockTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.stockTable.setItem(
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
            global s_list
            s_list = self.comboBox_2

            d = connection.cursor()
            d.execute('''CREATE TABLE IF NOT EXISTS CATEGORIES (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                category  VARCHAR UNIQUE NOT NULL )''')
            d.close()
            c.execute("SELECT category FROM categories ORDER BY category ASC;")
            rows = c.fetchall()
            for row in rows:
                    self.comboBox.addItem(str(row[0]))
            
            c.execute('''CREATE TABLE IF NOT EXISTS SUPPLIERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                supplier_name  VARCHAR UNIQUE NOT NULL ,
                supplier_no  VARCHAR UNIQUE NOT NULL ,
                email  VARCHAR UNIQUE NOT NULL ,
                category  VARCHAR  NOT NULL ,
                debt  VARCHAR  NOT NULL ,
                time_stamp  timestamp);''')
            c.execute("SELECT supplier_name FROM suppliers ORDER BY category ASC;")
            rs = c.fetchall()
            for row in rs:
                self.comboBox_2.addItem(str(row[0]))
            #            
            self.pushButton_2.clicked.connect(self.AddItem)
            self.pushButton_3.clicked.connect(self.addcatg)
            self.pushButton_4.clicked.connect(self.addsupp)
            self.comboBox.activated.connect(self.filter_supplier)

        def addcatg(self):
            self.window = AddCategoryWindow()
            self.window.show()

        def addsupp(self):
            self.window = AddSupplierWindow()
            self.window.show()

        def filter_supplier(self):
            self.comboBox_2.clear()
            v = self.comboBox.currentText()
            print(v)
            q = "SELECT supplier_name FROM suppliers where category = ?"
            r = c.execute(q,[v])
            rsl = r.fetchall()
            print(rsl)
            for row in rsl:
                self.comboBox_2.addItem(str(row[0]))
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
            supplier = self.comboBox_2.currentText()
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
                self.comboBox.clear()
                self.comboBox_2.clear()
                self.doubleSpinBox.setValue(0.00)
                self.spinBox.setValue(0)
                self.lineEdit_7.clear()
                self.textEdit.clear()
                #reset comboBox 
                d = connection.cursor()
                d.execute('''CREATE TABLE IF NOT EXISTS CATEGORIES (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    category  VARCHAR UNIQUE NOT NULL )''')
                d.close()
                c.execute("SELECT category FROM categories ORDER BY category ASC;")
                rows = c.fetchall()
                for row in rows:
                        self.comboBox.addItem(str(row[0]))
                
                c.execute('''CREATE TABLE IF NOT EXISTS SUPPLIERS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    supplier_name  VARCHAR UNIQUE NOT NULL ,
                    supplier_no  VARCHAR UNIQUE NOT NULL ,
                    email  VARCHAR UNIQUE NOT NULL ,
                    category  VARCHAR  NOT NULL ,
                    debt  VARCHAR  NOT NULL ,
                    time_stamp  timestamp);''')
                c.execute("SELECT supplier_name FROM suppliers ORDER BY category ASC;")
                rs = c.fetchall()
                for row in rs:
                    self.comboBox_2.addItem(str(row[0]))

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
                    cb_stock.clear()
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
class AddSupplierWindow(AddSupplier.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(AddSupplierWindow,self).__init__()
        self.setupUi(self)

        q = c.execute("SELECT category FROM categories ORDER BY category ASC;")
        rsl = c.fetchall()
        for row in rsl:
                self.comboBox.addItem(str(row[0]))
        #connect buttons
        self.comboBox.addItem("s1")
        self.pushButton.clicked.connect(self.addsupplier)
        onlyInt = QIntValidator()
        self.lineEdit_2.setValidator(onlyInt)

    def addsupplier(self):
        sname = self.lineEdit.text()
        s_no = self.lineEdit_2.text()
        s_email= self.lineEdit_3.text()
        s_catg = self.comboBox.currentText()
        s_debt = self.doubleSpinBox.text()
        time_stamp = datetime.datetime.now()
        #print(sname, s_email, s_no, s_catg, s_debt, time_stamp)

        d = connection.cursor()
        d.execute('''CREATE TABLE IF NOT EXISTS SUPPLIERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                supplier_name  VARCHAR UNIQUE NOT NULL ,
                supplier_no  VARCHAR UNIQUE NOT NULL ,
                email  VARCHAR UNIQUE NOT NULL ,
                category  VARCHAR  NOT NULL ,
                debt  VARCHAR  NOT NULL ,
                time_stamp  timestamp);''')
        d.close()
        
        if not sname:
                warn("category name is missing!")
        else:
            try:
                sql = """INSERT INTO suppliers(supplier_name, supplier_no, email, category, debt, time_stamp) VALUES (?, ?, ?, ?, ?, ?);"""
                c.execute(sql, [sname, s_no, s_email, s_catg, s_debt, time_stamp])            
                connection.commit()
                try:
                    c.execute("SELECT supplier_name FROM suppliers ORDER BY category ASC;")
                    rows = c.fetchall()
                    print(rows)
                    s_list.clear()
                    for row in rows:
                        s_list.addItem(str(row[0]))
                    connection.commit()                    
                except Exception as e:
                    warn("The sync not done!!!")
                    print("the sync not done!!", e)

                dialog("supplier Saved Successfully")           
            except Exception as e:
                print('Error', e)                    
                warn("The supplier already exists. Try again!")            
            self.lineEdit.clear()    
            self.lineEdit_2.clear()    
            self.lineEdit_3.clear()    
            #self.comboBox.clear()
            self.doubleSpinBox.setValue(0.00)
  
#Inventory report
class InventoryReport(InventoryReport.Ui_Dialog, QtWidgets.QMainWindow):
        def __init__(self):
                super(InventoryReport,self).__init__()
                #setting up the first window
                self.setupUi(self)
                
                #placing items to comboBox
                query = (" SELECT item_code,item_name,supplier FROM STOCK; ")
                r = c.execute(query)
                global res
                res = r.fetchall()
                for item in res:
                    self.comboBoxItemCode.addItem(item[0])
                    self.comboBoxItemName.addItem(item[1]) 
                    self.comboBoxSupplier.addItem(item[2])
                    
                #mapping items to tableWidget
                query = (" SELECT * FROM STOCK; ")
                items = c.execute(query)
                r = items.fetchall()
               #setting items to tablewidget           
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(12)
                self.tableWidget.setHorizontalHeaderLabels(
                    ['id', 'item_code', 'category', 'item_name', 'description', 'measurement', 'quantity', 'price', 'supplier', 'date_added', 'exp_date', 'remarks'])
                self.tableWidget.hideColumn(0)
                for row_number, row_data in enumerate(r):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                #pushButtons connections
                self.clearButton.clicked.connect(self.clear)
                self.pushButtonPrint.clicked.connect(self.printFunction)
        def clear(self):
            #index = self.comboBoxItemCode.findText("item code", QtCore.Qt.MatchFixedString)
            self.comboBoxItemCode.setCurrentIndex(0)  
            self.comboBoxItemName.setCurrentIndex(0)  
            self.comboBoxSupplier.setCurrentIndex(0) 
        def printFunction(self):
            pass    
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
        w = Main()
        #show the window and start the app
        w.show()
        app.exec_()

