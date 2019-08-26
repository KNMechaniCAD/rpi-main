import sys
import os
import numpy as np
import scipy.io as sio
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from Cluster import Cluster


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Cluster()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Fusion"
w = AppWindow()
w.show()
sys.exit(app.exec_())


