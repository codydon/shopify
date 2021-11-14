# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 613)
        MainWindow.setStyleSheet(u"background-color: #00394D;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #00394D;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setStyleSheet(u"background-color: #00394D;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_ok = QFrame(self.frame_3)
        self.frame_ok.setObjectName(u"frame_ok")
        self.frame_ok.setMaximumSize(QSize(450, 16777215))
        self.frame_ok.setStyleSheet(u"background-color: green;\n"
"border-radius: 5px;")
        self.frame_ok.setFrameShape(QFrame.StyledPanel)
        self.frame_ok.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_ok)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_ok = QLabel(self.frame_ok)
        self.label_ok.setObjectName(u"label_ok")
        self.label_ok.setMinimumSize(QSize(400, 41))
        self.label_ok.setMaximumSize(QSize(311, 41))
        self.label_ok.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_ok.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_ok)


        self.gridLayout_5.addWidget(self.frame_ok, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(403, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(120, 0))
        self.frame_2.setStyleSheet(u"\n"
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
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 30, 121, 50))
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 80, 121, 50))
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 130, 121, 50))
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 180, 121, 50))
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(0, 230, 121, 50))
        self.pushButton_8.setMinimumSize(QSize(0, 50))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(0, 280, 121, 50))
        self.pushButton_9.setMinimumSize(QSize(0, 50))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(0, 330, 121, 50))
        self.pushButton_10.setMinimumSize(QSize(0, 50))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11 = QPushButton(self.frame_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(0, 380, 121, 50))
        self.pushButton_11.setMinimumSize(QSize(0, 50))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(0, 430, 121, 50))
        self.pushButton_12.setMinimumSize(QSize(0, 50))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(0, 480, 121, 50))
        self.pushButton_13.setMinimumSize(QSize(0, 50))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u" \n"
"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_14 = QPushButton(self.page)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMaximumSize(QSize(108, 16777215))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"\n"
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

        self.gridLayout_4.addWidget(self.pushButton_14, 0, 0, 1, 3)

        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(581, 126))
        self.groupBox_3.setMaximumSize(QSize(16777215, 126))
        self.groupBox_3.setStyleSheet(u"\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"QRadioButton::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
"	font: 63 12pt \"Yu Gothic UI Semibold\";\n"
" }\n"
"")
        self.gridLayout_10 = QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.radioItemName = QRadioButton(self.groupBox_3)
        self.radioItemName.setObjectName(u"radioItemName")

        self.gridLayout_10.addWidget(self.radioItemName, 2, 0, 1, 1)

        self.radioItemCode = QRadioButton(self.groupBox_3)
        self.radioItemCode.setObjectName(u"radioItemCode")

        self.gridLayout_10.addWidget(self.radioItemCode, 2, 1, 1, 1)

        self.radioCategory = QRadioButton(self.groupBox_3)
        self.radioCategory.setObjectName(u"radioCategory")
        self.radioCategory.setMinimumSize(QSize(358, 0))

        self.gridLayout_10.addWidget(self.radioCategory, 2, 3, 1, 1)

        self.radioPrice = QRadioButton(self.groupBox_3)
        self.radioPrice.setObjectName(u"radioPrice")

        self.gridLayout_10.addWidget(self.radioPrice, 2, 2, 1, 1)

        self.radioSupplier = QRadioButton(self.groupBox_3)
        self.radioSupplier.setObjectName(u"radioSupplier")

        self.gridLayout_10.addWidget(self.radioSupplier, 3, 0, 1, 1)

        self.radioExpiryDate = QRadioButton(self.groupBox_3)
        self.radioExpiryDate.setObjectName(u"radioExpiryDate")

        self.gridLayout_10.addWidget(self.radioExpiryDate, 3, 1, 1, 1)

        self.radioDateAdded = QRadioButton(self.groupBox_3)
        self.radioDateAdded.setObjectName(u"radioDateAdded")

        self.gridLayout_10.addWidget(self.radioDateAdded, 3, 2, 1, 1)

        self.lineSearchProduct = QLineEdit(self.groupBox_3)
        self.lineSearchProduct.setObjectName(u"lineSearchProduct")
        self.lineSearchProduct.setMinimumSize(QSize(0, 35))
        self.lineSearchProduct.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }")

        self.gridLayout_10.addWidget(self.lineSearchProduct, 0, 0, 1, 4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 3, 3, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 3, 2, 2)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.page)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 25))
        self.spinBox.setMaximumSize(QSize(35, 16777215))

        self.gridLayout_4.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 2, 1, 1)

        self.stockTable = QTableWidget(self.page)
        self.stockTable.setObjectName(u"stockTable")
        self.stockTable.setMinimumSize(QSize(691, 241))
        self.stockTable.setMaximumSize(QSize(16777215, 250))

        self.gridLayout_4.addWidget(self.stockTable, 2, 0, 1, 5)

        self.horizontalSpacer_3 = QSpacerItem(399, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 3, 0, 1, 4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.updateStockBtn = QPushButton(self.page)
        self.updateStockBtn.setObjectName(u"updateStockBtn")
        self.updateStockBtn.setMinimumSize(QSize(120, 30))
        self.updateStockBtn.setMaximumSize(QSize(150, 30))
        self.updateStockBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateStockBtn.setStyleSheet(u"\n"
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

        self.horizontalLayout.addWidget(self.updateStockBtn)

        self.deleteStockBtn = QPushButton(self.page)
        self.deleteStockBtn.setObjectName(u"deleteStockBtn")
        self.deleteStockBtn.setMinimumSize(QSize(120, 30))
        self.deleteStockBtn.setMaximumSize(QSize(150, 30))
        self.deleteStockBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteStockBtn.setStyleSheet(u"\n"
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

        self.horizontalLayout.addWidget(self.deleteStockBtn)


        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 4, 1, 1)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 111))

        self.gridLayout_4.addWidget(self.groupBox, 4, 0, 1, 5)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(9, 9, 694, 532))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 671, 70))
        self.frame_7.setMinimumSize(QSize(671, 70))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"background-color: #00394D;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.frame_4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 218, 674, 250))
        self.tableWidget_2.setMinimumSize(QSize(674, 250))
        self.tableWidget_2.setMaximumSize(QSize(16777215, 13000))
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(30, 100, 400, 75))
        self.frame_5.setMinimumSize(QSize(400, 75))
        self.frame_5.setMaximumSize(QSize(500, 16777215))
        self.frame_5.setStyleSheet(u"QRadioButton{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_5)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 0, 1, 1, 1)

        self.radioButton_2 = QRadioButton(self.frame_5)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 0, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.frame_5)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_3.addWidget(self.radioButton_3, 0, 3, 1, 1)

        self.radioButton_4 = QRadioButton(self.frame_5)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_3.addWidget(self.radioButton_4, 0, 4, 1, 1)

        self.radioButton_5 = QRadioButton(self.frame_5)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_3.addWidget(self.radioButton_5, 0, 5, 1, 1)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(300, 40))
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 5)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.spinBox)
        self.label_2.setBuddy(self.spinBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.stockTable)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add Purchase", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Vital Stats", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Add Reminder", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"search product", None))
        self.radioItemName.setText(QCoreApplication.translate("MainWindow", u"Item Name", None))
        self.radioItemCode.setText(QCoreApplication.translate("MainWindow", u"Item Code", None))
        self.radioCategory.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.radioPrice.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.radioSupplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.radioExpiryDate.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None))
        self.radioDateAdded.setText(QCoreApplication.translate("MainWindow", u"Date Added", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"entries", None))
#if QT_CONFIG(tooltip)
        self.updateStockBtn.setToolTip(QCoreApplication.translate("MainWindow", u"update item information", None))
#endif // QT_CONFIG(tooltip)
        self.updateStockBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
#if QT_CONFIG(tooltip)
        self.deleteStockBtn.setToolTip(QCoreApplication.translate("MainWindow", u"deletes an item", None))
#endif // QT_CONFIG(tooltip)
        self.deleteStockBtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VITAL STATS OVERVIEW", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search :", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Serial No", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
    # retranslateUi

