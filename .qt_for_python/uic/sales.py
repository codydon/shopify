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
        Sales.resize(848, 693)
        Sales.setAutoFillBackground(False)
        Sales.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Sales.setDocumentMode(False)
        self.centralwidget = QWidget(Sales)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.navbar = QFrame(self.centralwidget)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 100))
        self.navbar.setStyleSheet(u"background-color: #00394D;")
        self.navbar.setFrameShape(QFrame.StyledPanel)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.navbar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.back = QFrame(self.navbar)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(80, 80))
        self.back.setFrameShape(QFrame.StyledPanel)
        self.back.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.back)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 51))
        font = QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

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
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.cashier = QComboBox(self.frame_2)
        self.cashier.addItem("")
        self.cashier.addItem("")
        self.cashier.addItem("")
        self.cashier.addItem("")
        self.cashier.setObjectName(u"cashier")
        self.cashier.setGeometry(QRect(170, 40, 171, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.cashier.setFont(font2)
        self.cashier.setAcceptDrops(True)
        self.cashier.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"")
        self.cashier.setEditable(False)
        self.cashier.setMaxVisibleItems(20)
        self.cashier.setDuplicatesEnabled(True)
        self.date = QDateTimeEdit(self.frame_2)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(170, 20, 161, 22))
        self.date.setFont(font1)
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
        self.line.setGeometry(QRect(150, 10, 21, 91))
        self.line.setStyleSheet(u"background-color: none;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.cashier_2 = QComboBox(self.frame_2)
        self.cashier_2.addItem("")
        self.cashier_2.addItem("")
        self.cashier_2.setObjectName(u"cashier_2")
        self.cashier_2.setGeometry(QRect(10, 40, 141, 31))
        self.cashier_2.setFont(font2)
        self.cashier_2.setAcceptDrops(True)
        self.cashier_2.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.cashier_2.setEditable(False)
        self.cashier_2.setMaxVisibleItems(20)
        self.cashier_2.setDuplicatesEnabled(True)

        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.navbar, 0, 0, 1, 3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, 50, -1, 50)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(99, 47))
        self.comboBox.setMaximumSize(QSize(1000, 47))
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setWeight(75)
        self.comboBox.setFont(font3)
        self.comboBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(True)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	background-color:transparent;\n"
"	border:8px;\n"
"	border-bottom: 2px solid gray;\n"
"\n"
"}")
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(100)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtTop)

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.list_2 = QFrame(self.centralwidget)
        self.list_2.setObjectName(u"list_2")
        self.list_2.setFrameShape(QFrame.StyledPanel)
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
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(255, 171, 74));
        self.list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(40, 186, 8));
        self.list.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(QColor(252, 73, 13));
        self.list.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.list.rowCount() < 6):
            self.list.setRowCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.list.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.list.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.list.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.list.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.list.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.list.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.list.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.list.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.list.setItem(1, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.list.setItem(1, 3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.list.setItem(2, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.list.setItem(2, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.list.setItem(2, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.list.setItem(2, 3, __qtablewidgetitem20)
        self.list.setObjectName(u"list")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setFont(font2)
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
        self.list.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.list.setAlternatingRowColors(True)
        self.list.setRowCount(6)
        self.list.horizontalHeader().setVisible(True)
        self.list.horizontalHeader().setCascadingSectionResizes(True)
        self.list.horizontalHeader().setProperty("showSortIndicator", True)
        self.list.horizontalHeader().setStretchLastSection(True)
        self.list.verticalHeader().setCascadingSectionResizes(True)
        self.list.verticalHeader().setProperty("showSortIndicator", True)
        self.list.verticalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.list, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.list_2, 2, 0, 1, 3)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(400, 200))
        self.frame_3.setMaximumSize(QSize(400, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 70, 341, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_4 = QComboBox(self.layoutWidget_2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 35))
        self.comboBox_4.setMaximumSize(QSize(16777215, 35))
        self.comboBox_4.setEditable(True)

        self.horizontalLayout_2.addWidget(self.comboBox_4)

        self.pushButton_4 = QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 35))
        self.pushButton_4.setMaximumSize(QSize(50, 35))
        self.pushButton_4.setStyleSheet(u"background-color: #00394D;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 50, 111, 20))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color:#00394D;")
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(200, 130, 141, 41))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_5.setFont(font5)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background-color: #00394D;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.frame_3, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 200))
        self.frame.setMaximumSize(QSize(400, 200))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 50, 211, 31))
        self.lineEdit_3.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 140, 331, 41))
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 136, 0);\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 60, 91, 20))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color:#00394D;")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 90, 121, 20))
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color:#00394D;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 20, 91, 20))
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color:#00394D;")
        self.total = QLineEdit(self.frame)
        self.total.setObjectName(u"total")
        self.total.setEnabled(False)
        self.total.setGeometry(QRect(170, 10, 211, 31))
        self.total.setFont(font6)
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
        self.cashier_3 = QComboBox(self.frame)
        self.cashier_3.addItem("")
        self.cashier_3.addItem("")
        self.cashier_3.setObjectName(u"cashier_3")
        self.cashier_3.setGeometry(QRect(180, 90, 201, 31))
        self.cashier_3.setFont(font2)
        self.cashier_3.setAcceptDrops(True)
        self.cashier_3.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"")
        self.cashier_3.setEditable(False)
        self.cashier_3.setMaxVisibleItems(20)
        self.cashier_3.setDuplicatesEnabled(True)

        self.gridLayout_4.addWidget(self.frame, 3, 2, 1, 1)

        Sales.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Sales)
        self.statusbar.setObjectName(u"statusbar")
        Sales.setStatusBar(self.statusbar)

        self.retranslateUi(Sales)

        QMetaObject.connectSlotsByName(Sales)
    # setupUi

    def retranslateUi(self, Sales):
        Sales.setWindowTitle(QCoreApplication.translate("Sales", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        Sales.setToolTip(QCoreApplication.translate("Sales", u"Make a sale", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Sales", u"\u25c4", None))
        self.label_2.setText(QCoreApplication.translate("Sales", u"Current Store:", None))
        self.cashier.setItemText(0, QCoreApplication.translate("Sales", u"Admin", None))
        self.cashier.setItemText(1, QCoreApplication.translate("Sales", u"Dan", None))
        self.cashier.setItemText(2, QCoreApplication.translate("Sales", u"Synthia", None))
        self.cashier.setItemText(3, QCoreApplication.translate("Sales", u"New Item", None))

        self.cashier.setCurrentText(QCoreApplication.translate("Sales", u"Admin", None))
#if QT_CONFIG(tooltip)
        self.date.setToolTip(QCoreApplication.translate("Sales", u"Today's Date", None))
#endif // QT_CONFIG(tooltip)
        self.cashier_2.setItemText(0, QCoreApplication.translate("Sales", u"Main", None))
        self.cashier_2.setItemText(1, QCoreApplication.translate("Sales", u"Sub-Branch", None))

        self.cashier_2.setCurrentText(QCoreApplication.translate("Sales", u"Main", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Sales", u"Home", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Sales", u"Sugar asdda sda sdas d asdwe rwe r wer  wer we rtwegh fh fgh fgh fghfg", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Sales", u"Maize", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Sales", u"Biscuit 45g", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Sales", u"Cooking oil", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Sales", u"Choose item(s)", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Sales", u"Id", None));
        ___qtablewidgetitem1 = self.list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Sales", u"Item", None));
        ___qtablewidgetitem2 = self.list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Sales", u"Cost", None));
        ___qtablewidgetitem3 = self.list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Sales", u"Price", None));
        ___qtablewidgetitem4 = self.list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Sales", u"S.p", None));
        ___qtablewidgetitem5 = self.list.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Sales", u"Quantity", None));
        ___qtablewidgetitem6 = self.list.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Sales", u"Total", None));
        ___qtablewidgetitem7 = self.list.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Sales", u"New Row", None));
        ___qtablewidgetitem8 = self.list.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Sales", u"New Row", None));
        ___qtablewidgetitem9 = self.list.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Sales", u"New Row", None));

        __sortingEnabled = self.list.isSortingEnabled()
        self.list.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.list.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Sales", u"qweqwe", None));
        ___qtablewidgetitem11 = self.list.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Sales", u"wqeqwe", None));
        ___qtablewidgetitem12 = self.list.item(0, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Sales", u"qweqw", None));
        ___qtablewidgetitem13 = self.list.item(0, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Sales", u"qweqw", None));
        ___qtablewidgetitem14 = self.list.item(1, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Sales", u"sdfsdfsdfsdfsdf sdfsdfsdfsdf", None));
        ___qtablewidgetitem15 = self.list.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Sales", u"sfdsfsdfsdf sdf sdfsdfsdfsd", None));
        ___qtablewidgetitem16 = self.list.item(1, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Sales", u"fgh", None));
        ___qtablewidgetitem17 = self.list.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Sales", u"asdas", None));
        ___qtablewidgetitem18 = self.list.item(2, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Sales", u"sdfsdf", None));
        ___qtablewidgetitem19 = self.list.item(2, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Sales", u"sdfsd", None));
        ___qtablewidgetitem20 = self.list.item(2, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Sales", u"sdfs", None));
        self.list.setSortingEnabled(__sortingEnabled)

        self.comboBox_4.setItemText(0, QCoreApplication.translate("Sales", u"Choose Customer", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Sales", u"Caroline Chelop", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Sales", u"Felix Kiptum", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Sales", u"Anastesia", None))

        self.pushButton_4.setText(QCoreApplication.translate("Sales", u"Find", None))
        self.label_8.setText(QCoreApplication.translate("Sales", u"Customer Account:", None))
        self.pushButton_5.setText(QCoreApplication.translate("Sales", u"Add New", None))
        self.pushButton_2.setText(QCoreApplication.translate("Sales", u"Complete Sale", None))
        self.label_5.setText(QCoreApplication.translate("Sales", u"Amount:", None))
        self.label_6.setText(QCoreApplication.translate("Sales", u"Payment", None))
        self.label_7.setText(QCoreApplication.translate("Sales", u"Total Cost", None))
        self.total.setText(QCoreApplication.translate("Sales", u"5000", None))
        self.cashier_3.setItemText(0, QCoreApplication.translate("Sales", u"Mpesa", None))
        self.cashier_3.setItemText(1, QCoreApplication.translate("Sales", u"Cheque", None))

        self.cashier_3.setCurrentText(QCoreApplication.translate("Sales", u"Mpesa", None))
    # retranslateUi

