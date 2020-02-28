# -*- coding: utf-8 -*-
"""
Numpy Viewer - version 0

This program opens an 1D numpy array and plots it using PyQt5 and
matplotlib.
The code in here is a slight mofification of the ones provided in
    https://pythonspot.com/pyqt5-file-dialog/
    https://pythonspot.com/pyqt5-matplotlib/
"""

import sys
import random
import numpy as np

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        # Main Window attributes
        self.title = "Numpy Viewer v 0.0.0"
        self.top = 0
        self.left = 0
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Menu 
        self.layout = QVBoxLayout()
        openButton = QPushButton("Open New")
        openButton.clicked.connect(self.openFileNameDialog)
        self.layout.addWidget(openButton)

        # Add plot session
        self.canvas = PlotCanvas(self, width=5,height=4)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        
        self.show()

    def openFileNameDialog(self,canvas):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                        "QFileDialog.getOpenFileName()",
                         "","All Files (*);;Python Files (*.py)",
                         options=options)
        if fileName:
            print("openFileNameDialog {}".format(fileName))
            # Update canvas
            canvas = PlotCanvas(self,width=5,height=4)
            self.layout.removeWidget(self.canvas)       # Remove previous
            self.layout.addWidget(canvas)               # Put the new
            self.canvas = canvas                        # Update
            if type(fileName) == list:
                fileName = fileName[0]
            canvas.plot(fileName)
    
        
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self,npyFile=None):
        if npyFile != None:
            data = np.load(npyFile)
            ax = self.figure.add_subplot(111)
            ax.plot(data,'r-')
            ax.set_title("{}".format(npyFile.split(".")[0]))
            self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
