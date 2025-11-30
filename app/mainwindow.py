# This python file uses the following encoding: utf-8
import sys 
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.statusBar().showMessage("Wellcome to PySide6 GUI")
        self.menuBar().addMenu("File")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())







