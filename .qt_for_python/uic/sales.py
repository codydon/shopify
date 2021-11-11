# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Sales(object):
    def setupUi(self, Sales):
        if not Sales.objectName():
            Sales.setObjectName(u"Sales")
        Sales.setWindowModality(Qt.WindowModal)
        Sales.resize(1002, 598)
        Sales.setAutoFillBackground(False)
        Sales.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Sales.setDocumentMode(False)
        self.centralwidget = QWidget(Sales)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 140))
        self.frame.setMaximumSize(QSize(400, 140))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(180, 90, 211, 41))
        self.lineEdit_3.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 100, 91, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color:#00394D;")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 20, 121, 20))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color:#00394D;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 60, 91, 20))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color:#00394D;")
        self.total = QLineEdit(self.frame)
        self.total.setObjectName(u"total")
        self.total.setEnabled(False)
        self.total.setGeometry(QRect(180, 50, 211, 31))
        self.total.setFont(font)
        self.total.setCursor(QCursor(Qt.SizeAllCursor))
        self.total.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"border:none;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"background-color:transparent;\n"
"border-bottom: 1px solid #00394D;")
        self.total.setInputMethodHints(Qt.ImhPreferNumbers)
        self.total.setMaxLength(20000000)
        self.total.setEchoMode(QLineEdit.Normal)
        self.total.setCursorPosition(4)
        self.total.setAlignment(Qt.AlignCenter)
        self.total.setReadOnly(True)
        self.total.setClearButtonEnabled(False)
        self.comboBox_5 = QComboBox(self.frame)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(180, 20, 211, 31))
        self.comboBox_5.setMinimumSize(QSize(211, 31))
        self.comboBox_5.setMaximumSize(QSize(16777215, 35))
        self.comboBox_5.setEditable(True)
        self.sale = QPushButton(self.frame)
        self.sale.setObjectName(u"sale")
        self.sale.setGeometry(QRect(400, 20, 71, 111))
        self.sale.setStyleSheet(u"background-color: rgb(0, 136, 0);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.sale.setCheckable(True)
        self.sale.setAutoDefault(False)
        self.sale.setFlat(False)

        self.gridLayout_4.addWidget(self.frame, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.navbar = QFrame(self.centralwidget)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 100))
        self.navbar.setStyleSheet(u"background-color: #00394D;")
        self.navbar.setFrameShape(QFrame.NoFrame)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.navbar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.back = QFrame(self.navbar)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(120, 80))
        self.back.setFrameShape(QFrame.NoFrame)
        self.back.setFrameShadow(QFrame.Raised)
        self.salepop = QPushButton(self.back)
        self.salepop.setObjectName(u"salepop")
        self.salepop.setGeometry(QRect(20, 10, 91, 61))
        font1 = QFont()
        font1.setFamily(u"Ubuntu Mono")
        font1.setPointSize(30)
        font1.setItalic(False)
        self.salepop.setFont(font1)
        self.salepop.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.hidepop = QPushButton(self.back)
        self.hidepop.setObjectName(u"hidepop")
        self.hidepop.setGeometry(QRect(40, 20, 61, 41))
        self.hidepop.setFont(font1)
        self.hidepop.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.hidepop.raise_()
        self.salepop.raise_()

        self.gridLayout_2.addWidget(self.back, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(383, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.navbar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(350, 80))
        self.frame_2.setMaximumSize(QSize(350, 200))
        self.frame_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 121, 21))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.date = QDateTimeEdit(self.frame_2)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(170, 20, 161, 22))
        self.date.setFont(font2)
        self.date.setLayoutDirection(Qt.LeftToRight)
        self.date.setWrapping(False)
        self.date.setFrame(False)
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setReadOnly(True)
        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setAccelerated(True)
        self.date.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.date.setProperty("showGroupSeparator", True)
        self.date.setCurrentSection(QDateTimeEdit.DaySection)
        self.date.setCalendarPopup(False)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(150, 0, 21, 111))
        self.line.setStyleSheet(u"background-color: none;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.comboBox_6 = QComboBox(self.frame_2)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(10, 40, 131, 31))
        self.comboBox_6.setMinimumSize(QSize(23, 31))
        self.comboBox_6.setMaximumSize(QSize(16777215, 35))
        self.comboBox_6.setEditable(True)
        self.comboBox_7 = QComboBox(self.frame_2)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(220, 40, 131, 31))
        self.comboBox_7.setMinimumSize(QSize(23, 31))
        self.comboBox_7.setMaximumSize(QSize(16777215, 35))
        self.comboBox_7.setStyleSheet(u"")
        self.comboBox_7.setEditable(True)
        self.label_2.raise_()
        self.date.raise_()
        self.comboBox_6.raise_()
        self.comboBox_7.raise_()
        self.line.raise_()

        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.navbar, 0, 0, 1, 3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(400, 140))
        self.frame_3.setMaximumSize(QSize(400, 140))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 50, 341, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_4 = QComboBox(self.layoutWidget_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 31))
        self.comboBox_4.setMaximumSize(QSize(16777215, 35))
        self.comboBox_4.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_4)

        self.pushButton_4 = QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 31))
        self.pushButton_4.setMaximumSize(QSize(50, 35))
        self.pushButton_4.setStyleSheet(u"background-color: #00394D;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 30, 111, 20))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color:#00394D;")
        self.newcustomer = QPushButton(self.frame_3)
        self.newcustomer.setObjectName(u"newcustomer")
        self.newcustomer.setGeometry(QRect(250, 100, 111, 31))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.newcustomer.setFont(font4)
        self.newcustomer.setCursor(QCursor(Qt.PointingHandCursor))
        self.newcustomer.setStyleSheet(u"background-color: #00394D;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.frame_3, 2, 0, 1, 1)

        self.list_2 = QFrame(self.centralwidget)
        self.list_2.setObjectName(u"list_2")
        self.list_2.setFrameShape(QFrame.NoFrame)
        self.list_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.list_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.list = QTableWidget(self.list_2)
        if (self.list.columnCount() < 7):
            self.list.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        brush = QBrush(QColor(52, 101, 164, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setBackground(QColor(255, 171, 74));
        __qtablewidgetitem3.setForeground(brush);
        self.list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setBackground(QColor(40, 186, 8));
        self.list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setBackground(QColor(252, 73, 13));
        self.list.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.list.rowCount() < 4):
            self.list.setRowCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.list.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.list.setItem(1, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.list.setItem(1, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.list.setItem(1, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.list.setItem(1, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.list.setItem(2, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.list.setItem(2, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.list.setItem(2, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.list.setItem(2, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.list.setItem(2, 4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.list.setItem(2, 5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.list.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.list.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.list.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.list.setItem(3, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.list.setItem(3, 4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.list.setItem(3, 5, __qtablewidgetitem25)
        self.list.setObjectName(u"list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(12)
        self.list.setFont(font5)
        self.list.setLayoutDirection(Qt.LeftToRight)
        self.list.setStyleSheet(u"/* QScrollArea ------------------------------------------------------------\n"
"\n"
"\n"
"/* QScrollBar -------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qscrollbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QScrollBar:horizontal {\n"
"  height: 16px;\n"
"  margin: 2px 16px 2px 16px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: #19232D;\n"
"  width: 16px;\n"
"  margin: 16px 2px 16px 2px;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-width: 8px;\n"
"}\n"
""
                        "\n"
"QScrollBar::handle:horizontal:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: #787878;\n"
"  border: 1px solid #32414B;\n"
"  min-height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"  background-color: #148CD2;\n"
"  border: 1px solid #148CD2;\n"
"  border-radius: 4px;\n"
"  min-height: 8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  margin: 0px 0px 0px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar"
                        "::add-line:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_down_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_down.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  margin: 0px 3px 0px 3px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-l"
                        "ine:vertical {\n"
"  margin: 3px 0px 3px 0px;\n"
"  border-image: url(\":/qss_icons/rc/arrow_up_disabled.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {\n"
"  border-image: url(\":/qss_icons/rc/arrow_up.png\");\n"
"  height: 12px;\n"
"  width: 12px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"  background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"/* QTextEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examp"
                        "les.html#customizing-specific-widgets\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"  background: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QPlainTextEdit ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QPlainTextEdit {\n"
"  background-color: #19232D;\n"
"  color: #F0F0F0;\n"
"  border-radius: 4px;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QPlainTextEdit:selected {\n"
"  backg"
                        "round: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QSizeGrip --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qsizegrip\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QSizeGrip {\n"
"  background: transparent;\n"
"  width: 12px;\n"
"  height: 12px;\n"
"  image: url(\":/qss_icons/rc/window_grip.png\");\n"
"}\n"
"\n"
"/* QStackedWidget ---------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QStackedWidget {\n"
"  padding: 2px;\n"
"  border: 1px solid #32414B;\n"
"  border: 1px solid #19232D;\n"
"}\n"
"\n"
"/* QToolBar ---------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtoolbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QToolBar {\n"
"  background-color: #32414B"
                        ";\n"
"  border-bottom: 1px solid #19232D;\n"
"  padding: 2px;\n"
"  font-weight: bold;\n"
"  spacing: 2px;\n"
"}\n"
"\n"
"QToolBar QToolButton {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #32414B;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked {\n"
"  border: 1px solid #19232D;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::handle:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_move_vertical.png\");\n"
"}\n"
"\n"
"QToolBar::separator:horizontal {\n"
"  width: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_horizontal.png\");\n"
"}\n"
"\n"
"QToolBar::separator:vertical {\n"
"  height: 16px;\n"
"  image: url(\":/qss_icons/rc/toolbar_separator_vertical.png\");\n"
"}\n"
""
                        "\n"
"QToolButton#qt_toolbar_ext_button {\n"
"  background: #32414B;\n"
"  border: 0px;\n"
"  color: #F0F0F0;\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: #1464A0;\n"
"  color: #19232D;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"  background-color: #14506E;\n"
"  color: #787878;\n"
"  border-radius: 4px;\n"
"}\n"
"QComboBox {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  selection-background-color: #1464A0;\n"
"  padding-left: 4px;\n"
"  padding-right: 36px;\n"
"  /* 4 + 16*2 See scrollbar size */\n"
"  /* Fixes #103, #111 */\n"
"  min-height: 1.5em;\n"
"  /* padding-top: 2px;     removed to fix #132 */\n"
"  /* padding-bottom: 2px;  removed to fix #132 */\n"
"  /* min-width: 75px;      removed to fix #109 */\n"
"  /* Needed to remove indicator - fix #132 */\n"
"}\n"
"\n"
"/* QLineEdit --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-e"
                        "xamples.html#customizing-qlineedit\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"  background-color: #19232D;\n"
"  padding-top: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-bottom: 2px;\n"
"  /* This QLineEdit fix  103, 111 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  border-style: solid;\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 0px;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"  background-color: #19232D;\n"
"  color: #787878;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  border: 1px solid #148CD2;\n"
"  color: #F0F0F0;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"  background-color: #1464A0;\n"
"  color: #32414B;\n"
"}\n"
"\n"
"/* QTabWiget --------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"---------------------------------"
                        "------------------------------------------ */\n"
"QTabWidget {\n"
"  padding: 2px;\n"
"  selection-background-color: #32414B;\n"
"}\n"
"\n"
"QTabWidget QWidget {\n"
"  /* Fixes #189 */\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border: 1px solid #32414B;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  /* Fixes double border inside pane with pyqt5 */\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabWidget::pane:selected {\n"
"  background-color: #32414B;\n"
"  border: 1px solid #1464A0;\n"
"}\n"
"\n"
"/* QTabBar ----------------------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar {\n"
"  qproperty-drawBase: 0;\n"
"  border-radius: 4px;\n"
"  margin: 0px;\n"
"  padding: 2px;\n"
"  border: 0;\n"
"  /* left: 5px; move to the right by 5px - removed for fix */\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"  border: 0;\n"
""
                        "  margin: 2px;\n"
"  padding: 2px;\n"
"  image: url(\":/qss_icons/rc/window_close.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"/* QTabBar::tab - selected ------------------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtabwidget-and-qtabbar\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTabBar::tab {\n"
"  /* !selected and disabled ----------------------------------------- */\n"
"  /* selected ------------------------------------------------------- */\n"
"}\n"
"\n"
"QTabBar::tab:top:selected:disabled {\n"
"  border-bottom: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected:disabled {\n"
"  border-top: 3px solid #14506E;\n"
"  color: #787878;\n"
"  backgrou"
                        "nd-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected:disabled {\n"
"  border-right: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected:disabled {\n"
"  border-left: 3px solid #14506E;\n"
"  color: #787878;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:disabled {\n"
"  border-bottom: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:disabled {\n"
"  border-top: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:disabled {\n"
"  border-right: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:disabled {\n"
"  border-left: 3px solid #19232D;\n"
"  color: #787878;\n"
"  background-color: #19232D;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"  border-bottom: 2px solid #19232D;\n"
"  margin-top: 2px;\n"
"}\n"
"\n"
""
                        "QTabBar::tab:bottom:!selected {\n"
"  border-top: 2px solid #19232D;\n"
"  margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"  border-left: 2px solid #19232D;\n"
"  margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"  border-right: 2px solid #19232D;\n"
"  margin-left: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:top {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  min-width: 5px;\n"
"  border-bottom: 3px solid #32414B;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"  background-color: #505F69;\n"
"  color: #F0F0F0;\n"
"  border-bottom: 3px solid #1464A0;\n"
"  border-top-left-radius: 3px;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-bottom: 3px solid #148CD2;\n"
"  /* Fixes spyder-ide/spyder#"
                        "9766 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom {\n"
"  color: #F0F0F0;\n"
"  border-top: 3px solid #32414B;\n"
"  background-color: #32414B;\n"
"  margin-left: 2px;\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"  padding-top: 2px;\n"
"  padding-bottom: 2px;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-width: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-top: 3px solid #1464A0;\n"
"  border-bottom-left-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-top: 3px solid #148CD2;\n"
"  /* Fixes spyder-ide/spyder#9766 */\n"
"  padding-left: 4px;\n"
"  padding-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:left {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top:"
                        " 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-left-radius: 3px;\n"
"  border-bottom-left-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-right: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-right: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right {\n"
"  color: #F0F0F0;\n"
"  background-color: #32414B;\n"
"  margin-top: 2px;\n"
"  padding-left: 2px;\n"
"  padding-right: 2px;\n"
"  padding-top: 4px;\n"
"  padding-bottom: 4px;\n"
"  border-top-right-radius: 3px;\n"
"  border-bottom-right-radius: 3px;\n"
"  min-height: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"  color: #F0F0F0;\n"
"  background-color: #505F69;\n"
"  border-left: 3px solid #1464A0;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected:hover {\n"
"  border: 1px solid #148CD2;\n"
"  border-left: 3px solid #148CD2;\n"
"  padding: 0px;\n"
"}\n"
"\n"
"QTabB"
                        "ar QToolButton {\n"
"  /* Fixes #136 */\n"
"  background-color: #32414B;\n"
"  height: 12px;\n"
"  width: 12px;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed {\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QTabBar QToolButton:pressed:hover {\n"
"  border: 1px solid #148CD2;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_left_disabled.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right.png\");\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"  image: url(\":/qss_icons/rc/arrow_right_disabled.png\");\n"
"}\n"
"\n"
"/* QDockWiget -------------------------------------------------------------\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QDockWidget {\n"
"  outline: 1px solid #32414B;\n"
"  background-color: #19232D;\n"
"  border: 1px solid"
                        " #32414B;\n"
"  border-radius: 4px;\n"
"  titlebar-close-icon: url(\":/qss_icons/rc/window_close.png\");\n"
"  titlebar-normal-icon: url(\":/qss_icons/rc/window_undock.png\");\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"  /* Better size for title bar */\n"
"  padding: 6px;\n"
"  spacing: 4px;\n"
"  border: none;\n"
"  background-color: #32414B;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_close_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_close_pressed.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button {\n"
"  background-color: #32414B;\n"
"  border-radius: 4px;\n"
"  border: none;\n"
"}\n"
"\n"
"QDockWidget::float-button:hover {\n"
"  image: url(\":/qss_icons/rc/window_undock_focus.png\");\n"
"}\n"
"\n"
"QDockWidget::float-button:pressed {\n"
"  image: url(\":/qss_icons/rc/window_undock_pres"
                        "sed.png\");\n"
"}\n"
"\n"
"/* QTreeView QListView QTableView -----------------------------------------\n"
"\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtreeview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qlistview\n"
"https://doc.qt.io/qt-5/stylesheet-examples.html#customizing-qtableview\n"
"\n"
"--------------------------------------------------------------------------- */\n"
"QTreeView:branch:selected, QTreeView:branch:hover {\n"
"  background: url(\":/qss_icons/rc/transparent.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:!adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_line.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_more.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:!has-children:!has-siblings:adjoins-item {\n"
"  border-image: url(\":/qss_icons/rc/branch_end.png\") 0;\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has"
                        "-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_closed.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {\n"
"  border-image: none;\n"
"  image: url(\":/qss_icons/rc/branch_open.png\");\n"
"}\n"
"\n"
"QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_closed_focus.png\");\n"
"}\n"
"\n"
"QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {\n"
"  image: url(\":/qss_icons/rc/branch_open_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked,\n"
"QListView::indicator:checked {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,\n"
"QListView::indicator:checked:hover,\n"
"QListView::indicator:checked:focus,\n"
"QListVie"
                        "w::indicator:checked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_checked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked,\n"
"QListView::indicator:unchecked {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,\n"
"QListView::indicator:unchecked:hover,\n"
"QListView::indicator:unchecked:focus,\n"
"QListView::indicator:unchecked:pressed {\n"
"  image: url(\":/qss_icons/rc/checkbox_unchecked_focus.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate,\n"
"QListView::indicator:indeterminate {\n"
"  image: url(\":/qss_icons/rc/checkbox_indeterminate.png\");\n"
"}\n"
"\n"
"QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,\n"
"QListView::indicator:indeterminate:hover,\n"
"QListView::indicator:indeterminate:focus,\n"
"QListView::indicator:indeterminate:pressed {\n"
"  image: url"
                        "(\":/qss_icons/rc/checkbox_indeterminate_focus.png\");\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView,\n"
"QTableView,\n"
"QColumnView {\n"
"  \n"
"background-color: rgba(0, 170, 255,.2);\n"
"  border: 1px solid #32414B;\n"
" \n"
"	color: rgb(0, 0, 0);\n"
"  gridline-color: #32414B;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"  background-color: #32414B;\n"
"  color: #F0F0F0;\n"
"  padding: 2px;\n"
"  border-radius: 0px;\n"
"  text-align: left;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.list.setFrameShape(QFrame.StyledPanel)
        self.list.setFrameShadow(QFrame.Raised)
        self.list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.list.setTabKeyNavigation(False)
        self.list.setProperty("showDropIndicator", True)
        self.list.setDragEnabled(False)
        self.list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.list.setAlternatingRowColors(True)
        self.list.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.list.setTextElideMode(Qt.ElideMiddle)
        self.list.setSortingEnabled(True)
        self.list.setRowCount(4)
        self.list.horizontalHeader().setVisible(True)
        self.list.horizontalHeader().setCascadingSectionResizes(True)
        self.list.horizontalHeader().setProperty("showSortIndicator", True)
        self.list.horizontalHeader().setStretchLastSection(False)
        self.list.verticalHeader().setCascadingSectionResizes(True)
        self.list.verticalHeader().setProperty("showSortIndicator", True)
        self.list.verticalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.list, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.list_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.list_2, 1, 0, 1, 3)

        Sales.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Sales)
        self.statusbar.setObjectName(u"statusbar")
        Sales.setStatusBar(self.statusbar)

        self.retranslateUi(Sales)

        self.sale.setDefault(False)


        QMetaObject.connectSlotsByName(Sales)
    # setupUi

    def retranslateUi(self, Sales):
        Sales.setWindowTitle(QCoreApplication.translate("Sales", u"Shopify", None))
#if QT_CONFIG(tooltip)
        Sales.setToolTip(QCoreApplication.translate("Sales", u"Make a sale", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Sales", u"Amount:", None))
        self.label_6.setText(QCoreApplication.translate("Sales", u"Payment:", None))
        self.label_7.setText(QCoreApplication.translate("Sales", u"Total:", None))
        self.total.setText(QCoreApplication.translate("Sales", u"5000", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("Sales", u"Cash", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Sales", u"Mpesa", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Sales", u"Account", None))

        self.sale.setText(QCoreApplication.translate("Sales", u"Sale", None))
#if QT_CONFIG(shortcut)
        self.sale.setShortcut(QCoreApplication.translate("Sales", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.salepop.setText(QCoreApplication.translate("Sales", u"\u25c4", None))
#if QT_CONFIG(shortcut)
        self.salepop.setShortcut(QCoreApplication.translate("Sales", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.hidepop.setText(QCoreApplication.translate("Sales", u"\u25c4", None))
#if QT_CONFIG(shortcut)
        self.hidepop.setShortcut(QCoreApplication.translate("Sales", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("Sales", u"Current Store:", None))
#if QT_CONFIG(tooltip)
        self.date.setToolTip(QCoreApplication.translate("Sales", u"Today's Date", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Sales", u"Cash", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Sales", u"Main Store", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Sales", u"Store2", None))

        self.comboBox_7.setItemText(0, QCoreApplication.translate("Sales", u"Cash", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Sales", u"Main Store", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("Sales", u"Store2", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("Sales", u"Choose Customer", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Sales", u"Caroline Chelop", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Sales", u"Felix Kiptum", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Sales", u"Anastesia", None))

        self.pushButton_4.setText(QCoreApplication.translate("Sales", u"Find", None))
        self.label_8.setText(QCoreApplication.translate("Sales", u"Customer Account:", None))
        self.newcustomer.setText(QCoreApplication.translate("Sales", u"Add New", None))
        ___qtablewidgetitem = self.list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Sales", u"Item_Id", None));
        ___qtablewidgetitem1 = self.list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Sales", u"Item", None));
        ___qtablewidgetitem2 = self.list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Sales", u"Price(Ksh.)", None));
        ___qtablewidgetitem3 = self.list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Sales", u"S.p(Ksh.)", None));
        ___qtablewidgetitem4 = self.list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Sales", u"Quantity", None));
        ___qtablewidgetitem5 = self.list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Sales", u"Total", None));
        ___qtablewidgetitem6 = self.list.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Sales", u"Delete", None));
        ___qtablewidgetitem7 = self.list.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Sales", u"1_____", None));

        __sortingEnabled = self.list.isSortingEnabled()
        self.list.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.list.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Sales", u"item001", None));
        ___qtablewidgetitem9 = self.list.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Sales", u"Sugar 1kg", None));
        ___qtablewidgetitem10 = self.list.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Sales", u"100", None));
        ___qtablewidgetitem11 = self.list.item(1, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Sales", u"110", None));
        ___qtablewidgetitem12 = self.list.item(1, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Sales", u"2", None));
        ___qtablewidgetitem13 = self.list.item(1, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Sales", u"220", None));
        ___qtablewidgetitem14 = self.list.item(2, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Sales", u"item002", None));
        ___qtablewidgetitem15 = self.list.item(2, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Sales", u"Match box 120g", None));
        ___qtablewidgetitem16 = self.list.item(2, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Sales", u"30", None));
        ___qtablewidgetitem17 = self.list.item(2, 3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Sales", u"25", None));
        ___qtablewidgetitem18 = self.list.item(2, 4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Sales", u"5", None));
        ___qtablewidgetitem19 = self.list.item(2, 5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Sales", u"125", None));
        ___qtablewidgetitem20 = self.list.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Sales", u"item003", None));
        ___qtablewidgetitem21 = self.list.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Sales", u"Cooking oil (Rina)", None));
        ___qtablewidgetitem22 = self.list.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Sales", u"550", None));
        ___qtablewidgetitem23 = self.list.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Sales", u"450", None));
        ___qtablewidgetitem24 = self.list.item(3, 4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Sales", u"5", None));
        ___qtablewidgetitem25 = self.list.item(3, 5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Sales", u"2500", None));
        self.list.setSortingEnabled(__sortingEnabled)

    # retranslateUi

