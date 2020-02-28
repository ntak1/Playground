# MVC design pattern
1. **Model**: business logic
2. **View**: GUI
3. **Controller**: connects model and view. Ex:
	1. Acces the GUI's public interface
	2. Handle th creation of math expressions
	3. Connect button clicked signals with the appropriate slots

Step-by-step MVC pattern for a GUI desktop application:
1. The user performs an action or request (event).
2. The view notifies the controller about the user's action.
3. Thre controller gets the user's request and queries the model for a response.
4. The model preocesses the controller query, performs the required operations, and returns and answer or result.
5. The cotroller receives the model's answer and updates the view accordingly.
6. The user finally sees the requested result on the view.

# References
* A good intro tutorial on PyQt5 most of the sritpts in this repo are based in the following tutorial:  
https://realpython.com/python-pyqt-gui-calculator/  

* Some other refferences
https://pythonspot.com/pyqt5-file-dialog/  
https://pythonspot.com/pyqt5-matplotlib/  
http://zetcode.com/gui/pyqt5/layout/  
