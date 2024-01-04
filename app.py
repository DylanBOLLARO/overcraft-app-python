import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import qdarktheme
import requests
import os
from dotenv import load_dotenv

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(450, 250)
        self.setWindowTitle("OverCraft")
        load_dotenv(".env")
        self.api_url = os.getenv('API_URL')
        
        def make_post_request(api_endpoint, email, password):
            data = {
                "email": email,
                "password": password
            }
            try:
                response = requests.post(api_endpoint, data=data)
                if response.status_code == 200:
                    print(response.text)
                    self.label_email.setText("")
                    self.label_password.setText("")
                    return response.text
                else:
                    print(f"Error: {response.status_code}\n{response.text}")
                    return None
            except requests.RequestException as e:
                print(f"An error occurred: {e}")
                return None
            
        def login():
            api_endpoint = f"{self.api_url}/auth/signin"
            print(api_endpoint, self.label_email.text(), self.label_password.text())
            make_post_request(api_endpoint, self.label_email.text(), self.label_password.text())
            
        form_layout = QFormLayout()
        self.setLayout(form_layout)
        
        label_name_app = QLabel("OverCraft")
        label_name_app.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Create a QFont object and set its properties
        font = QFont("Helvetica", 36)
        font.setBold(True)  # Set the font weight to bold
        label_name_app.setFont(font)
        
        self.label_email = QLineEdit(self)
        self.label_email.setFont(QFont("Helvetica", 18))
        
        self.label_password = QLineEdit(self)
        self.label_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_password.setFont(QFont("Helvetica", 18))
        
        form_layout.addRow(label_name_app)
        form_layout.addRow("Email", self.label_email)
        form_layout.addRow("Password", self.label_password)

        # Connect the clicked signal to the on_button_click method
        sign_in_button = QPushButton("Sign in")
        sign_in_button.setFont(QFont("Helvetica", 18))
        
        sign_in_button.clicked.connect(login)
        form_layout.addRow(sign_in_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    w.show()
    sys.exit(app.exec())
