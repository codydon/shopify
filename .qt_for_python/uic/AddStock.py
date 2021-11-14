# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddStock.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(781, 424)
        Dialog.setMinimumSize(QSize(781, 424))
        Dialog.setMaximumSize(QSize(781, 424))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setCursor(QCursor(Qt.ArrowCursor))
        Dialog.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        Dialog.setModal(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 81, 16))
        self.label_2.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 80, 71, 16))
        self.label_3.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 200, 81, 16))
        self.label_4.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 200, 51, 16))
        self.label_5.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 200, 61, 16))
        self.label_6.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 71, 16))
        self.label_7.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 260, 61, 16))
        self.label_8.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 380, 371, 31))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: #00394D;\n"
"border-radius:15px;\n"
"color:white;\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0083b3;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(220, 100, 201, 31))
        self.lineEdit_3.setStyleSheet(u"")
        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(460, 220, 311, 31))
        self.lineEdit_6.setStyleSheet(u"")
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 100, 131, 31))
        self.dateEdit.setStyleSheet(u"")
        self.dateEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit_2 = QDateEdit(Dialog)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(20, 280, 131, 31))
        self.dateEdit_2.setStyleSheet(u"")
        self.dateEdit_2.setCalendarPopup(True)
        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(20, 220, 131, 31))
        self.doubleSpinBox.setStyleSheet(u"padding-right: 15px; /* make room for the arrows */\n"
"\n"
" border-width: 3;\n"
"\n"
" border: 1px solid gray;")
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setAccelerated(False)
        self.doubleSpinBox.setProperty("showGroupSeparator", False)
        self.doubleSpinBox.setMaximum(1000000.000000000000000)
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(220, 280, 361, 71))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setTabletTracking(True)
        self.textEdit.setStyleSheet(u"\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" ")
        self.textEdit.setTabChangesFocus(True)
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(460, 100, 311, 31))
        self.lineEdit_4.setStyleSheet(u"")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(490, 80, 71, 16))
        self.label_9.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 781, 61))
        self.frame.setStyleSheet(u"background-color: #00394D;\n"
"color:rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 81, 21))
        self.label.setStyleSheet(u"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"")
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(220, 220, 201, 31))
        self.spinBox.setStyleSheet(u"padding-right: 15px; /* make room for the arrows */\n"
"\n"
" border-width: 3;\n"
"\n"
" border: 1px solid gray;")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMaximum(1000000000)
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(220, 160, 201, 31))
        self.lineEdit_5.setStyleSheet(u"")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 140, 81, 20))
        self.label_10.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 160, 131, 31))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 140, 81, 20))
        self.label_11.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(470, 140, 101, 16))
        self.label_12.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(460, 160, 311, 31))
        self.lineEdit_7.setStyleSheet(u"")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 140, 41, 21))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-color: rgb(57, 114, 171);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_4.setBuddy(self.doubleSpinBox)
        self.label_5.setBuddy(self.spinBox)
        self.label_6.setBuddy(self.lineEdit_6)
        self.label_7.setBuddy(self.dateEdit_2)
        self.label_8.setBuddy(self.textEdit)
        self.label_9.setBuddy(self.lineEdit_4)
        self.label_10.setBuddy(self.lineEdit_5)
        self.label_11.setBuddy(self.comboBox)
        self.label_12.setBuddy(self.lineEdit_7)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.dateEdit, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.pushButton_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Item", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"DATE ADDED :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"ITEM CODE :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"NO. OF ITEMS", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"PRICE :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"SUPPLIER :", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"EXPIRY DATE :", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"REMARKS :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Dialog", u"Save item to stock.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"SAVE ITEM", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Dialog", u"supplier's company name/ owner", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Dialog", u"d/M/yyyy", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"ITEM NAME :", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ADD  ITEM", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"e.g brand, color, shape e.t.c,,", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"DESCRIPTION :", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"CATEGORY :", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"MEASUREMENTS :", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Dialog", u"e.g: ml, cm, kg, g, watts e.t.c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("Dialog", u"click to add new category", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"+", None))
    # retranslateUi

