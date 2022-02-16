import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# Create an instace of QApplication
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt5 App")

# Set position (from top), width and height of window
ax = 100
ay = 100
width = 280
height = 80
window.setGeometry(ax,ay,width,height)

window.move(0,0)                      # Move the window to new coord
text = "<h1>Hello World!</h1>"
helloMsg = QLabel(text,parent=window) # A widget that has a parent is shown within its
                                      # parent. If the parent is killed, the child too
helloMsg.move(60,15)

# Shows the aṕplication GUI
window.show()

# Run the application's event loop'
sys.exit(app.exec_())
