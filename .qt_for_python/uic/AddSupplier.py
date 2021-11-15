# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddSupplier.ui'
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
        Dialog.resize(400, 340)
        Dialog.setMinimumSize(QSize(400, 239))
        Dialog.setMaximumSize(QSize(13000, 13000))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 401, 41))
        self.frame.setStyleSheet(u"background-color: #00394D;\n"
"color:rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 141, 21))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 70, 231, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 290, 171, 31))
        self.pushButton.setStyleSheet(u"\n"
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
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 110, 231, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        self.lineEdit_2.setInputMethodHints(Qt.ImhPreferNumbers)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(130, 150, 231, 31))
        self.lineEdit_3.setTabletTracking(True)
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 190, 231, 31))
        self.comboBox.setMouseTracking(True)
        self.comboBox.setTabletTracking(True)
        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(130, 230, 231, 31))
        self.doubleSpinBox.setMouseTracking(True)
        self.doubleSpinBox.setTabletTracking(True)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox.setMaximum(1000000000.000000000000000)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 91, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 91, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 91, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 200, 121, 16))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 240, 91, 16))
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.lineEdit)
        self.label_3.setBuddy(self.lineEdit_2)
        self.label_4.setBuddy(self.lineEdit_3)
        self.label_5.setBuddy(self.comboBox)
        self.label_6.setBuddy(self.doubleSpinBox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.pushButton)

        self.retranslateUi(Dialog)
        Dialog.accepted.connect(self.lineEdit.setFocus)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ADD NEW SUPPLIER", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"supplier name", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"SAVE SUPPLIER", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"supplier number", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"email", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SUPPLIER NAME :", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"SUPPLIER NUMBER :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"SUPPLIER EMAIL :", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"SUPPLIER CATEGORY  :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"SUPPLIER'S DEBT :", None))
    # retranslateUi

