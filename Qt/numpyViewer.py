import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.draw()

    def compute_initial_figure(self):
        pass
    
class WidgetPlot(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.setParent(parent)
        self.setLayout(QVBoxLayout())
        self.canvas =  MyMplCanvas(parent=self)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)

class Window(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("NumpyViewer v 0.0.1")
        self.generalLayout = QVBoxLayout()
        self._createMenu()
        self._createPlot()
        self.setLayout(self.generalLayout)

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&File")
        #self.menu = self.menuBar().addMenu("&Help")
        self.generalLayout.addWidget(self.menu)

    def _createPlot(self):
        plot = WidgetPlot(parent=self) 
        self.generalLayout.addWidget(plot)
        self.setCentralWidget(plot)
        self.plot = plot

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                        "QFileDialog.getOpenFileName()",
                         "","All Files (*);;Python Files (*.py)",
                         options=options)
        return fileName

    def updatePlot(self,data):
        if len(data.shape) == 1:
            self.plot.canvas.axes.plot(data)
        elif len(data.shape) == 2:
            self.plot.canvas.axes.imshow(data)        
            
        self.plot.canvas.draw()
        

class ApplicationController():
    def __init__(self,model,view):
        self._view = view
        self._model = model
        self._connectSignals()

    def openNumpyFile(self):
        fileName = self._view.openFileNameDialog()
        try:
            data = np.load(fileName)
        except:
            print("Errror loading the file {}".format(fileName))
            return
        self._view.updatePlot(data)
            
    def _connectSignals(self):
        self._view.menu.addAction("Open New",self.openNumpyFile)
        self._view.menu.addAction("Exit",self._view.close)

def plus():
    return 1+2

def main():
    app = QApplication(sys.argv) 
    view = Window()
    model = plus
    appCtrl = ApplicationController(model, view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
