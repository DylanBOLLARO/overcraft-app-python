import sys
from PyQt5.QtWidgets import QApplication

# Custom
from app import Application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Application()
    sys.exit(app.exec())
    