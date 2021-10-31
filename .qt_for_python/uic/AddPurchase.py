# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddPurchase.ui'
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
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(627, 370)
        Dialog.setMinimumSize(QSize(396, 370))
        Dialog.setMaximumSize(QSize(3960, 3700))
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
" }")
        Dialog.setModal(True)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -10, 631, 371))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 160, 71, 20))
        self.label_4.setStyleSheet(u"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 200, 71, 20))
        self.label_6.setStyleSheet(u"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(200, 240, 361, 71))
        self.textEdit.setStyleSheet(u"\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" ")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 80, 51, 20))
        self.label_2.setStyleSheet(u"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(200, 120, 191, 31))
        self.lineEdit_3.setStyleSheet(u"")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 332, 371, 31))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: #00394D;\n"
"border-radius:15px;\n"
"color:white;\n"
"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #0083b3;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 120, 131, 20))
        self.label_3.setStyleSheet(u"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(200, 200, 221, 31))
        self.lineEdit_6.setStyleSheet(u"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 250, 71, 20))
        self.label_8.setStyleSheet(u"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 631, 61))
        self.frame.setStyleSheet(u"background-color: #00394D;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 30, 131, 21))
        self.label.setStyleSheet(u"font: 63 12pt \"Yu Gothic UI Semibold\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.doubleSpinBox = QDoubleSpinBox(self.frame_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(200, 160, 181, 31))
        self.doubleSpinBox.setStyleSheet(u"padding-right: 15px; /* make room for the arrows */\n"
"\n"
" border-width: 3;\n"
"border-radius:10px;\n"
" border: 1px solid gray;")
        self.dateEdit = QDateEdit(self.frame_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(200, 80, 171, 31))
        self.dateEdit.setStyleSheet(u"\n"
"     border: 1px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" ")
        self.dateEdit.setCalendarPopup(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Item", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"QUANTITY :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"SUPPLIER :", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"DATE :", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Dialog", u"Save item to stock.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"SAVE PURCHASE", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"TRANSACTION CODE:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"REMARKS :", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ADD PURCHASE", None))
    # retranslateUi

