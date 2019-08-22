# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cluster.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 616)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(570, 420, 71, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.DriverStep = QtWidgets.QLCDNumber(Form)
        self.DriverStep.setGeometry(QtCore.QRect(80, 420, 71, 41))
        self.DriverStep.setObjectName("DriverStep")
        self.SpeedBar = QtWidgets.QProgressBar(Form)
        self.SpeedBar.setGeometry(QtCore.QRect(90, 490, 551, 41))
        self.SpeedBar.setProperty("value", 24)
        self.SpeedBar.setObjectName("SpeedBar")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(50, 170, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
