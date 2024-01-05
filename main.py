from PyQt5.QtWidgets import QApplication
import sys
from pages.login_page import LoginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LoginPage()
    sys.exit(app.exec())
    