import os
from dotenv import load_dotenv

# Custom
from pages.login_page import LoginPage
from pages.overlay import OverlayPage
from utils.networking import RequestsApi
from components.timer import Timer

class Application:
    def __init__(self):
        load_dotenv(".env")
        self.api_url = os.getenv('API_URL')
        self.timer_instance = Timer()
        self.credentials = {"access_token": None, "refresh_token": None}
        self.request_instance = RequestsApi(self.api_url)
        self.login_page = LoginPage(self.request_instance, application_instance=self)
        if self.credentials["access_token"] is None:
            self.login_page.show()

    def init_and_show_overlay(self):
        self.overlay_page = OverlayPage(self.request_instance, self.timer_instance, application_instance=self)
        self.overlay_page.show()