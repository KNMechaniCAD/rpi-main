import sys
import os
import numpy as np
import scipy.io as sio
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from GraphDisplay import Ui_MainWindow

from SignalProcesing import Math, Function
from NewSignal import NewFunctWindow
from filterWindow import filterFunctWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    #global dictio={}
    def new_function(self):
        new_window = NewFunctWindow()
        if new_window.exec_():
            self.function = new_window.function

    def plot(self, x, y):
        self.ui.Display.canvas.ax.clear()
        self.ui.Display.canvas.ax.plot(x, y)
        self.ui.Display.canvas.draw()

    
app = QApplication(sys.argv)
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Fusion"
w = AppWindow()
w.show()
sys.exit(app.exec_())


