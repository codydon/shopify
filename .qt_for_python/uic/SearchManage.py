# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchManage.ui'
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
        Dialog.resize(630, 424)
        Dialog.setMinimumSize(QSize(630, 370))
        Dialog.setMaximumSize(QSize(13000, 13000))
        Dialog.setModal(True)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 70, 611, 101))
        self.groupBox.setStyleSheet(u"QRadioButton::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
"	font: 63 8pt \"Yu Gothic UI Semibold\";\n"
" }")
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 20, 521, 31))
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 60, 82, 17))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 80, 82, 17))
        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(150, 60, 82, 17))
        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(150, 80, 82, 17))
        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(290, 80, 82, 17))
        self.radioButton_6 = QRadioButton(self.groupBox)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(290, 60, 82, 17))
        self.radioButton_7 = QRadioButton(self.groupBox)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(420, 60, 82, 17))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 631, 61))
        self.frame.setStyleSheet(u"background-color: #00394D;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 221, 21))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 170, 611, 192))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 370, 391, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }")
        self.lineEdit_5.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_5.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 25))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton{\n"
" background-color: #4CAF50;\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(2, 90, 39);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(65, 25))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(170, 58, 82);\n"
"border:none;\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 73, 106);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.lineEdit_4, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.radioButton_6)
        QWidget.setTabOrder(self.radioButton_6, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.radioButton_5)
        QWidget.setTabOrder(self.radioButton_5, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Search and Manage Stock", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"search", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Item Name", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Supplier", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Item Code", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"Expiry Date", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Date Added", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SEARCH & MANAGE STOCK", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Item ID", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Dialog", u"update item information", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"UPDATE", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Dialog", u"deletes an item", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"DELETE", None))
    # retranslateUi

