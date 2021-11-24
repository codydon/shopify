# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 613)
        MainWindow.setStyleSheet("background-color: #00394D;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #00394D;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setStyleSheet("background-color: #00394D;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_ok = QtWidgets.QFrame(self.frame_3)
        self.frame_ok.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_ok.setStyleSheet("background-color: green;\n"
"border-radius: 5px;")
        self.frame_ok.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ok.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ok.setObjectName("frame_ok")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_ok)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_ok = QtWidgets.QLabel(self.frame_ok)
        self.label_ok.setMinimumSize(QtCore.QSize(400, 41))
        self.label_ok.setMaximumSize(QtCore.QSize(311, 41))
        self.label_ok.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_ok.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ok.setObjectName("label_ok")
        self.horizontalLayout_3.addWidget(self.label_ok)
        self.gridLayout_5.addWidget(self.frame_ok, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(403, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(120, 0))
        self.frame_2.setStyleSheet("\n"
"QPushButton{\n"
"background-color: #00394D;;\n"
"color:white;\n"
"border:none;\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color:white;\n"
"color:black;\n"
" }\n"
"QFrame{\n"
"background-color: #00394D;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 30, 121, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 121, 50))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 130, 121, 50))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 121, 50))
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 230, 121, 50))
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 280, 121, 50))
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 330, 121, 50))
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 380, 121, 50))
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 430, 121, 50))
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 480, 121, 50))
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setStyleSheet(" \n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.page)
        self.pushButton_14.setMaximumSize(QtCore.QSize(108, 16777215))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("\n"
"QPushButton{\n"
"background-color: #00394D;\n"
"color:white;\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(54, 109, 163);\n"
" }")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 0, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setMinimumSize(QtCore.QSize(581, 126))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 126))
        self.groupBox_3.setStyleSheet("\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"QRadioButton::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
"    font: 63 12pt \"Yu Gothic UI Semibold\";\n"
" }\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.radioItemName = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioItemName.setObjectName("radioItemName")
        self.gridLayout_10.addWidget(self.radioItemName, 2, 0, 1, 1)
        self.radioItemCode = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioItemCode.setObjectName("radioItemCode")
        self.gridLayout_10.addWidget(self.radioItemCode, 2, 1, 1, 1)
        self.radioCategory = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioCategory.setMinimumSize(QtCore.QSize(358, 0))
        self.radioCategory.setObjectName("radioCategory")
        self.gridLayout_10.addWidget(self.radioCategory, 2, 3, 1, 1)
        self.radioPrice = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioPrice.setObjectName("radioPrice")
        self.gridLayout_10.addWidget(self.radioPrice, 2, 2, 1, 1)
        self.radioSupplier = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioSupplier.setObjectName("radioSupplier")
        self.gridLayout_10.addWidget(self.radioSupplier, 3, 0, 1, 1)
        self.radioExpiryDate = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioExpiryDate.setObjectName("radioExpiryDate")
        self.gridLayout_10.addWidget(self.radioExpiryDate, 3, 1, 1, 1)
        self.radioDateAdded = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioDateAdded.setObjectName("radioDateAdded")
        self.gridLayout_10.addWidget(self.radioDateAdded, 3, 2, 1, 1)
        self.lineSearchProduct = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineSearchProduct.setMinimumSize(QtCore.QSize(0, 35))
        self.lineSearchProduct.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }")
        self.lineSearchProduct.setObjectName("lineSearchProduct")
        self.gridLayout_10.addWidget(self.lineSearchProduct, 0, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 3, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 3, 2, 2)
        self.label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.page)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBox.setMaximumSize(QtCore.QSize(35, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_4.addWidget(self.spinBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 2, 1, 1)
        self.stockTable = QtWidgets.QTableWidget(self.page)
        self.stockTable.setMinimumSize(QtCore.QSize(691, 241))
        self.stockTable.setMaximumSize(QtCore.QSize(16777215, 250))
        self.stockTable.setObjectName("stockTable")
        self.stockTable.setColumnCount(0)
        self.stockTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.stockTable, 2, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(399, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 3, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.updateStockBtn = QtWidgets.QPushButton(self.page)
        self.updateStockBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.updateStockBtn.setMaximumSize(QtCore.QSize(150, 30))
        self.updateStockBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateStockBtn.setStyleSheet("\n"
"QPushButton{\n"
" background-color: #4CAF50;\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(2, 90, 39);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.updateStockBtn.setObjectName("updateStockBtn")
        self.horizontalLayout.addWidget(self.updateStockBtn)
        self.deleteStockBtn = QtWidgets.QPushButton(self.page)
        self.deleteStockBtn.setMinimumSize(QtCore.QSize(120, 30))
        self.deleteStockBtn.setMaximumSize(QtCore.QSize(150, 30))
        self.deleteStockBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteStockBtn.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(170, 58, 82);\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 73, 106);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.deleteStockBtn.setObjectName("deleteStockBtn")
        self.horizontalLayout.addWidget(self.deleteStockBtn)
        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 4, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 111))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4.addWidget(self.groupBox, 4, 0, 1, 5)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.spinBox)
        self.label_2.setBuddy(self.spinBox)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.pushButton_13)
        MainWindow.setTabOrder(self.pushButton_13, self.pushButton_14)
        MainWindow.setTabOrder(self.pushButton_14, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.stockTable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ok.setText(_translate("MainWindow", "ok"))
        self.pushButton.setText(_translate("MainWindow", "Dashboard"))
        self.pushButton_2.setText(_translate("MainWindow", "search"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Purchase"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "P"))
        self.pushButton_4.setText(_translate("MainWindow", "Add Expense"))
        self.pushButton_8.setText(_translate("MainWindow", "Payments"))
        self.pushButton_9.setText(_translate("MainWindow", "Vital Stats"))
        self.pushButton_10.setText(_translate("MainWindow", "Reports"))
        self.pushButton_11.setText(_translate("MainWindow", "Expiry Reports"))
        self.pushButton_12.setText(_translate("MainWindow", "Contacts"))
        self.pushButton_13.setText(_translate("MainWindow", "Logout"))
        self.pushButton_14.setText(_translate("MainWindow", "Add Item"))
        self.groupBox_3.setTitle(_translate("MainWindow", "search product"))
        self.radioItemName.setText(_translate("MainWindow", "Item Name"))
        self.radioItemCode.setText(_translate("MainWindow", "Item Code"))
        self.radioCategory.setText(_translate("MainWindow", "Category"))
        self.radioPrice.setText(_translate("MainWindow", "Price"))
        self.radioSupplier.setText(_translate("MainWindow", "Supplier"))
        self.radioExpiryDate.setText(_translate("MainWindow", "Expiry Date"))
        self.radioDateAdded.setText(_translate("MainWindow", "Date Added"))
        self.label.setText(_translate("MainWindow", "Show"))
        self.label_2.setText(_translate("MainWindow", "entries"))
        self.updateStockBtn.setToolTip(_translate("MainWindow", "update item information"))
        self.updateStockBtn.setText(_translate("MainWindow", "UPDATE VALUE"))
        self.deleteStockBtn.setToolTip(_translate("MainWindow", "deletes an item"))
        self.deleteStockBtn.setText(_translate("MainWindow", "DELETE ROW"))
        self.groupBox.setTitle(_translate("MainWindow", "VITAL STATS OVERVIEW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
