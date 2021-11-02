import sys
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint, QTimer, QTime, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore,QtSql
from PyQt5.QtCore import QTimer, QTime, Qt, QDate, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QCompleter, QComboBox

import sales as sales


from PyQt5.QtWidgets import QDialog,QTableWidget, QTableWidgetItem,QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QGridLayout,QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("shopify.db")
cursor = conn.cursor()

class Mainclass(sales.Ui_Sales, QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainclass, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        header = self.tableWidgetUser.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # PAGE 1
        
        
        self.dash.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard))

class ExtendedComboBox(QComboBox):
    def __init__(self):
        super(ExtendedComboBox, self).__init__()

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(250, 215, 40, 120)
        self.setFixedWidth(900)
        self.setFixedHeight(50)
        self.setWindowTitle("SearchMe!")

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add a completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)
        choosebutton = QPushButton('Click me', self)
        #choosebutton.clicked.connect(self.clickMethod)
        choosebutton.resize(100,32)
        choosebutton.move(50, 50) 

        # connect signals
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)


    # on selection of an item from the completer, select the corresponding item from combobox 
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated[str].emit(self.itemText(index))


    # on model change, update the models of the filter and completer as well 
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)


    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)    
  
  
class MyActions(sales.Ui_Sales, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyActions, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        header = self.list.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)

        #functional buttons
        self.newcustomer.clicked.connect(self.createtempSales)
        self.salepop.clicked.connect(self.listItems)
        self.hidepop.clicked.connect(self.hidesale)
        self.listItems();
        self.date.setDateTime(QDateTime.currentDateTime())

        
     
        
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    def createtempSales(self):
        query = "CREATE TABLE IF NOT EXISTS temp(id INTEGER PRIMARY KEY AUTOINCREMENT,item_code VARCHAR UNIQUE, item_name VARCHAR, price INTEGER, saleprice INTEGER, total INTEGER, quantity INTEGER)"
        cursor.execute(query)
        conn.commit()
        print("temp table created")
    def hidesale(self):
        self.combo = ExtendedComboBox()
        self.combo.hide()
    def listItems(self):
        try:
            conn = sqlite3.connect("shopify.db")
            cursor = conn.cursor()
            query = "SELECT * FROM STOCK  "
            cursor.execute(query)
            itemstore = cursor.fetchall()
            self.combo = ExtendedComboBox()
            
            mycounter=0
            for item in itemstore:
                self.combo.addItem(itemstore[mycounter][3])
                #print(itemstore[mycounter][2])
                mycounter = mycounter+1
            self.combo.resize(600, 40)
            self.combo.show()
        
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could find Product  Record from the Database.')
        conn.close()
    def add_us(self):
        username = input("New username: ")
        password = input("New password: ")
        self.add_user(username, password)
    def add_user(self, username, password):
        
        query = "INSERT INTO login (username, password) VALUES (?, ?)"
        cursor.execute(query, (username, password))
        conn.commit()

    def check_user(self, username, password):
        query = 'SELECT * FROM login WHERE username = ? AND password = ?'
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.commit()
        print('[DEBUG][check] result:', result)
        return result

    def login(self):
        username = self.email.text()
        password = self.pin.text()
        if self.check_user(username, password):
            self.errorsms.setText("You are logged in")
            self.w = Mainclass()
            self.w.show()
            self.hide()
        else:
            self.errorsms.setText("Check your credentials! ")
    def closeEvent(self, event):
        sys.exit(0)
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qt_app=MyActions()
    qt_app.show()
    app.exec_()