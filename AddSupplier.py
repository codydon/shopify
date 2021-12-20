from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(400, 340)
        Dialog.setMinimumSize(QtCore.QSize(400, 239))
        Dialog.setMaximumSize(QtCore.QSize(13000, 13000))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 41))
        self.frame.setStyleSheet("background-color: #00394D;\n"
"color:rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 231, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 171, 31))
        self.pushButton.setStyleSheet("\n"
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
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 110, 231, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 150, 231, 31))
        self.lineEdit_3.setTabletTracking(True)
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"     border: 1px solid gray;\n"
"     border-radius: 15px;\n"
"     padding: 0 8px;\n"
"     background: white;\n"
"     selection-background-color: darkgray;\n"
" }\n"
"")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 190, 231, 31))
        self.comboBox.setMouseTracking(True)
        self.comboBox.setTabletTracking(True)
        self.comboBox.setObjectName("comboBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 230, 231, 31))
        self.doubleSpinBox.setMouseTracking(True)
        self.doubleSpinBox.setTabletTracking(True)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox.setMaximum(1000000000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_2.setBuddy(self.lineEdit)
        self.label_3.setBuddy(self.lineEdit_2)
        self.label_4.setBuddy(self.lineEdit_3)
        self.label_5.setBuddy(self.comboBox)
        self.label_6.setBuddy(self.doubleSpinBox)

        self.retranslateUi(Dialog)
        Dialog.accepted.connect(self.lineEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.doubleSpinBox)
        Dialog.setTabOrder(self.doubleSpinBox, self.pushButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ADD NEW SUPPLIER"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "supplier name"))
        self.pushButton.setText(_translate("Dialog", "SAVE SUPPLIER"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "supplier number"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "email"))
        self.label_2.setText(_translate("Dialog", "SUPPLIER NAME :"))
        self.label_3.setText(_translate("Dialog", "SUPPLIER NUMBER :"))
        self.label_4.setText(_translate("Dialog", "SUPPLIER EMAIL :"))
        self.label_5.setText(_translate("Dialog", "SUPPLIER CATEGORY  :"))
        self.label_6.setText(_translate("Dialog", "SUPPLIER\'S DEBT :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
