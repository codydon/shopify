# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        MainWindow.resize(787, 656)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: #00394D;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(611, 461))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-260, 30, 16, 451))
        self.line.setStyleSheet(u"border-left:2px solid #8585ad;\n"
"")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 80, 131, 91))
        font = QFont()
        font.setFamily(u"Pristina")
        font.setPointSize(72)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color:transparent;\n"
"color:green;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 200, 221, 41))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(10)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color:transparent;\n"
"color:white;\n"
"font: 87 11pt \"Arial Black\";")
        self.pin = QLineEdit(self.frame)
        self.pin.setObjectName(u"pin")
        self.pin.setGeometry(QRect(90, 260, 361, 51))
        self.pin.setFont(font1)
        self.pin.setStyleSheet(u"\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"border-radius:5px;\n"
"border: 2px solid #8585ad;\n"
"color:white;\n"
"	font: 87 11pt \"Arial Black\";\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid #00b36b;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")
        self.pin.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.pin.setEchoMode(QLineEdit.Password)
        self.pin.setAlignment(Qt.AlignCenter)
        self.pin.setDragEnabled(False)
        self.pin.setClearButtonEnabled(True)
        self.loginbtn = QPushButton(self.frame)
        self.loginbtn.setObjectName(u"loginbtn")
        self.loginbtn.setGeometry(QRect(460, 260, 91, 51))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(10)
        self.loginbtn.setFont(font2)
        self.loginbtn.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border-radius:15px;\n"
"color:white;\n"
"	font: 87 12pt \"Arial Black\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame_error = QFrame(self.frame)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setGeometry(QRect(80, 10, 450, 30))
        self.frame_error.setMaximumSize(QSize(450, 16777215))
        self.frame_error.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-radius: 5px;")
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.label_error = QLabel(self.frame_error)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setStyleSheet(u"color: rgb(35, 35, 35);")
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)


        self.gridLayout.addWidget(self.frame, 1, 1, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 79, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u058e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome To Shopify", None))
        self.pin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter pin-Code", None))
        self.loginbtn.setText(QCoreApplication.translate("MainWindow", u"Access", None))
        self.label_error.setText(QCoreApplication.translate("MainWindow", u"Error", None))
    # retranslateUi

