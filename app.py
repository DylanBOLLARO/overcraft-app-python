import sys
from PyQt6.QtWidgets import QApplication
import qdarktheme
from pages.login import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    w.show()
    sys.exit(app.exec())
    