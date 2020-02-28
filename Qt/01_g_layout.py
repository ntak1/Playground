import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Grid Layout example")

layout = QGridLayout()
buttons_names = [str(i) for i in range(16)]
ncols = nlines = 4
k = 0
for i in range(nlines):
    for j in range(ncols):
        layout.addWidget(QPushButton(buttons_names[k]),i,j)
        k += 1

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
