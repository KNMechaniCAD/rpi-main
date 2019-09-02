# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cluster.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QPen
from PyQt5.QtCore import Qt



class Cluster(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 616)
        Form.setAutoFillBackground(True)
        back=Form.palette()
        back.setColor(Form.backgroundRole(), Qt.white)
        Form.setPalette(back)
        self.Speed = QtWidgets.QLCDNumber(Form)
        self.Speed.setGeometry(QtCore.QRect(570, 420, 71, 41))
        self.Speed.setObjectName("lcdNumber")
        self.DriverStep = QtWidgets.QLCDNumber(Form)
        self.DriverStep.setGeometry(QtCore.QRect(80, 420, 71, 41))
        self.DriverStep.setObjectName("DriverStep")
        self.SpeedBar = QtWidgets.QProgressBar(Form)
        self.SpeedBar.setGeometry(QtCore.QRect(50, 490, 650, 41))
        self.SpeedBar.setObjectName("SpeedBar")
        self.SpeedBar.setOrientation(QtCore.Qt.Horizontal)
        self.SpeedBar.setValue(0)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(50, 50, 50, 350))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setValue(0)
        self.Cart=QtWidgets.QLabel(Form)
        self.Cart.setPixmap(QtGui.QPixmap("Vehicle.png"))
        self.Cart.setGeometry(300,100,135,50)
        self.LED_Cap=QtWidgets.QLabel(Form)
        self.LED_Cap.setPixmap(QtGui.QPixmap("green.png"))
        self.LED_Cap.setGeometry(570,100,40,40)
        self.LED_Temp=QtWidgets.QLabel(Form)
        self.LED_Temp.setPixmap(QtGui.QPixmap("red.png"))
        self.LED_Temp.setGeometry(570,200,40,40)
        self.LED_Pitch=QtWidgets.QLabel(Form)
        self.LED_Pitch.setPixmap(QtGui.QPixmap("red.png"))
        self.LED_Pitch.setGeometry(570,300,40,40)
        self.PitchRate = QtWidgets.QLCDNumber(Form)
        self.PitchRate.setGeometry(QtCore.QRect(450, 70, 71, 41))
        self.PitchRate.setObjectName("PitchRate")
        self.CapText=QtWidgets.QLabel(Form)
        self.CapText.setText('Capacitor Rate')
        self.CapText.setGeometry(620,300,80,80)
        self.TempText=QtWidgets.QLabel(Form)
        self.TempText.setText('Temp Rate')
        self.TempText.setGeometry(620,200,80,80)
        self.PitchText=QtWidgets.QLabel(Form)
        self.PitchText.setText('Pitch Rate')
        self.PitchText.setGeometry(620,100,80,80)
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
