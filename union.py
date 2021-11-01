import sys
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint, QTimer, QTime, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore,QtSql
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect
import sales as sales


from PyQt5.QtWidgets import QDialog,QTableWidget, QTableWidgetItem,QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QGridLayout,QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
data = ["uasin-gishu","kericho","nandi"]


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
       
  
class MyActions(sales.Ui_Sales, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyActions, self).__init__()
        self.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
       
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    def create_tableUser(self):
        query = "CREATE TABLE IF NOT EXISTS login(username VARCHAR UNIQUE, password VARCHAR)"
        cursor.execute(query)
        conn.commit()
    def create_tableRecords(self):
        query = "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, county VARCHAR, date VARCHAR, latitude INTEGER,longitude INTEGER,new INTEGER,recovered INTEGER,deceased INTEGER, info VARCHAR, pop VARCHAR)"
        cursor.execute(query)
        conn.commit()

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
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qt_app=MyActions()
    qt_app.show()
    app.exec_()