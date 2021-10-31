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
        MainWindow.resize(853, 606)
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
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u" \n"
"background-color: rgb(255, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")

        self.gridLayout_4.addWidget(self.groupBox, 3, 0, 1, 5)

        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
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
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
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


        self.gridLayout_4.addWidget(self.frame_5, 0, 4, 2, 1)

        self.tableWidget = QTableWidget(self.page)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 250))

        self.gridLayout_4.addWidget(self.tableWidget, 2, 0, 1, 5)

        self.pushButton_14 = QPushButton(self.page)
        self.pushButton_14.setObjectName(u"pushButton_14")
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

        self.gridLayout_4.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.page)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 25))

        self.gridLayout_4.addWidget(self.spinBox, 1, 2, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{\n"
"font: 63 8pt \"Yu Gothic UI Semibold\";\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_2, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 1)

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

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setStyleSheet(u"background-color: #00394D;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 2)


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
        QWidget.setTabOrder(self.spinBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.radioButton_5)
        QWidget.setTabOrder(self.radioButton_5, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.tableWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VITAL STATS OVERVIEW", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search :", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Serial No", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"entries", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Items", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Add Purchase", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Payments", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Vital Stats", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Add Reminder", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

