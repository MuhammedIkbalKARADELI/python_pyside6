# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
import resource

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PySide6 GUI")
        self.setGeometry(100,100, 400,300)
        self.setWindowIcon(QIcon("/Applications/Work Space/Python Work Space/python_pyside6/xlab.png"))     


if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())


