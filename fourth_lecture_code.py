from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 GUI Tutorials")
        self.setGeometry(100,100, 400,300)
        self.setWindowIcon(QIcon("/Applications/Work Space/Python Work Space/python_pyside6/xlab.png"))
        self.setStyleSheet("background-color:blue")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())




