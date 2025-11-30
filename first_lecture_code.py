## Opening Window ##
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.statusBar().showMessage("Hello GUI")
window.menuBar().addMenu("File")

window.show()

sys.exit(app.exec())