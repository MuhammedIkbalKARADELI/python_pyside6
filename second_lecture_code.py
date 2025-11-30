from PySide6.QtWidgets import QApplication, QDialog
import sys

app = QApplication([])

window = QDialog()

window.show()
sys.exit(app.exec())
