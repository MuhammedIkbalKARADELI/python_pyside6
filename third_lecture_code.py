from PySide6.QtWidgets import QApplication, QWidget
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 GUI Tutorials")
        self.setGeometry(100,100, 400,300)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())





