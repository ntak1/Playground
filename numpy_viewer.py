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
        openButton = QPushButton("Open")
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
            self.layout.removeWidget(self.canvas)
            self.layout.addWidget(canvas)
            self.canvas = canvas
            if type(fileName) == list:
                fileName = fileName[0]
            canvas.plot(fileName)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,
                        "QFileDialog.getOpenFileNames()",
                         "","All Files (*);;Python Files (*.py)",
                         options=options)
        if files:
            print("OpenFileNamesDialog {}".format(files))
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,
                        "QFileDialog.getSaveFileName()",
                        "","All Files (*);;Text Files (*.txt)",
                        options=options)
        if fileName:
            print("SaveFileDialog {}".format(fileName))
        
        
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
        if npyFile == None:
            pass
           # data = [random.random() for i in range(25)]
           # ax = self.figure.add_subplot(111)
           # #ax = self.figure.add_axes((100,100,100,100))
           # ax.plot(data, 'r-')
           # ax.set_title('PyQt Matplotlib Example')
           # self.axes = ax
           # self.draw()
        else:
            #self.fig.clf()
            #self.axes.cla()
           # self.fig.delaxes(self.axes)
           # self.fig.clear()
           # plt.close(self.fig)

            data = np.load(npyFile)
            ax = self.figure.add_subplot(111)
            #ax = self.figure.add_axes((100,100,100,100))
            ax.plot(data,'r-')
            ax.set_title("{}".format(npyFile.split(".")[0]))
            print(data.shape)
            #self.fig.canvas.draw_idle()
            self.draw()
            #self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
