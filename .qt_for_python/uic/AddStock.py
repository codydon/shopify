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
        Dialog.resize(645, 413)
        Dialog.setMinimumSize(QSize(645, 413))
        Dialog.setMaximumSize(QSize(645, 413))
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
        self.label_2.setGeometry(QRect(20, 80, 51, 16))
        self.label_2.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 80, 71, 16))
        self.label_3.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 61, 16))
        self.label_4.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 140, 51, 16))
        self.label_5.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 200, 61, 16))
        self.label_6.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 140, 71, 16))
        self.label_7.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 260, 61, 16))
        self.label_8.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 370, 371, 31))
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
        self.lineEdit_3.setGeometry(QRect(190, 100, 191, 31))
        self.lineEdit_3.setStyleSheet(u"")
        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(20, 220, 361, 31))
        self.lineEdit_6.setStyleSheet(u"")
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(20, 100, 110, 31))
        self.dateEdit.setStyleSheet(u"")
        self.dateEdit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit_2 = QDateEdit(Dialog)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(410, 160, 110, 31))
        self.dateEdit_2.setStyleSheet(u"")
        self.dateEdit_2.setCalendarPopup(True)
        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(20, 160, 111, 31))
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
        self.textEdit.setGeometry(QRect(20, 280, 361, 71))
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
        self.lineEdit_4.setGeometry(QRect(410, 100, 201, 31))
        self.lineEdit_4.setStyleSheet(u"")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 80, 71, 16))
        self.label_9.setStyleSheet(u"font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 701, 61))
        self.frame.setStyleSheet(u"background-color: #00394D;\n"
"color:rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 81, 21))
        self.label.setStyleSheet(u"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(474, 30, 171, 31))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: green;\n"
"border:none;\n"
"color:white;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(2, 90, 39);\n"
"}\n"
"\n"
"")
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(190, 160, 171, 31))
        self.spinBox.setStyleSheet(u"padding-right: 15px; /* make room for the arrows */\n"
"\n"
" border-width: 3;\n"
"\n"
" border: 1px solid gray;")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setMaximum(1000000000)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_4.setBuddy(self.doubleSpinBox)
        self.label_6.setBuddy(self.lineEdit_6)
        self.label_7.setBuddy(self.dateEdit_2)
        self.label_8.setBuddy(self.textEdit)
        self.label_9.setBuddy(self.lineEdit_4)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pushButton, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.pushButton_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Item", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"DATE :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"ITEM CODE :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"QUANTITY :", None))
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
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dialog", u"Search for iem in existing stock.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Search and Manage Items", None))
    # retranslateUi

