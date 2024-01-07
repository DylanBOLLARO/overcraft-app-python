import json
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import uic
import requests
import sys

class LoginPage(QMainWindow):
    def __init__(self, request_instance, application_instance):
        super(LoginPage, self).__init__()
        self.request_instance = request_instance
        self.application_instance = application_instance
        
        
        # Load the ui file
        uic.loadUi("./ui/login.ui", self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("OverCraft")
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Define our widgets
        self.button_close_app_login = self.findChild(QPushButton, "button_close_app_login")
        self.button_login = self.findChild(QPushButton, "button_login")
        self.lineEdit_email = self.findChild(QLineEdit, "lineEdit_email")
        self.lineEdit_password = self.findChild(QLineEdit, "lineEdit_password")
        
        # Click the buttons
        self.button_close_app_login.clicked.connect(self.close_app)
        self.button_login.clicked.connect(self.login)
        

    
    def set_credentials(self, access_token, refresh_token):
        self.application_instance.credentials["access_token"] = access_token
        self.application_instance.credentials["refresh_token"] = refresh_token

    def close_app(self):
        sys.exit()
        
    def login(self):
        api_endpoint = f"{self.application_instance.api_url}/auth/signin"
        data={"email": self.lineEdit_email.text(),"password": self.lineEdit_password.text()}
        try:
            response = requests.post(api_endpoint, data)
            if response.status_code == 200:
                response_data = json.loads(response.text)
                if 'access_token' in response_data and 'refresh_token' in response_data:
                    self.set_credentials(response_data["access_token"], response_data["refresh_token"])
                    self.hide()
                    self.application_instance.init_and_show_overlay()
                    
                return response.text
            if response.status_code == 400:
                # Assume response.text contains a JSON response
                response_data = json.loads(response.text)
                # Check if the 'message' key exists in the response
                if 'message' in response_data:
                    # Iterate through each error message and print it
                    for error_message in response_data['message']:
                        if error_message.lower().startswith('email'):
                            self.lineEdit_email.setPlaceholderText(error_message)
                        if error_message.lower().startswith('password'):
                            self.lineEdit_password.setPlaceholderText(error_message)
                else:
                    print("No error messages found in the response.")
                return None
            else:
                print(f"Error: {response.status_code}\n{response.text}")
                return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None