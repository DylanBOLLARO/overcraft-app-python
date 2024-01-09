import sys
import requests
from enum import Enum

# PyQt5
from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedWidget, QWidget, QSlider, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import uic

# Custom
from components.button_build import ButtonBuild

class Size(Enum):
    SMALL = {'width': 350, 'height': 600}
    MEDIUM = {'width': 400, 'height': 700}
    LARGE = {'width': 450, 'height': 850}
    
class OverlayPage(QMainWindow):
    def __init__(self, request_instance, timer_instance, application_instance):
        super(OverlayPage, self).__init__()
        self.request_instance = request_instance
        self.timer_instance = timer_instance
        self.application_instance = application_instance
        self.builds = None

        # Load the ui file
        uic.loadUi("./ui/overlay.ui", self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute ( Qt.WA_TransparentForMouseEvents, False);
        self.setWindowTitle("OverCraft")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.set_window_size(Size.MEDIUM)
        # self.setWindowOpacity(0.75)
        self.move(0,0)
        
        # Define buttons
        self.button_open_settings = self.findChild(QPushButton, "button_open_settings")
        self.button_settings_back = self.findChild(QPushButton, "button_settings_back")
        self.button_close_app_overlay = self.findChild(QPushButton, "button_close_app_overlay")
        self.button_display_build_back = self.findChild(QPushButton, "button_display_build_back")
        self.button_set_small_size = self.findChild(QPushButton, "button_set_small_size")
        self.button_set_medium_size = self.findChild(QPushButton, "button_set_medium_size")
        self.button_set_large_size = self.findChild(QPushButton, "button_set_large_size")
        self.button_start_scrolling = self.findChild(QPushButton, "button_start_scrolling")
        
        # Define labels
        self.label_name_build = self.findChild(QLabel, "label_name_build")
        self.label_timer_scrolling = self.findChild(QLabel, "label_timer_scrolling")
        self.timer_instance.define_label(self.label_timer_scrolling)
        
        # Define our widgets
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.page_overlay = self.findChild(QWidget, "page_1")
        self.page_settings = self.findChild(QWidget, "page_2")
        self.page_display_build = self.findChild(QWidget, "page_3")
        self.slider_opacity = self.findChild(QSlider, "horizontalSlider")
        self.verticalLayout_9 = self.findChild(QVBoxLayout, "verticalLayout_9")
        self.verticalLayout_10 = self.findChild(QVBoxLayout, "verticalLayout_10")
        
        # Define our pages
        self.stackedWidget.addWidget (self.page_overlay)
        self.stackedWidget.addWidget (self.page_settings)
        self.stackedWidget.addWidget (self.page_display_build)
        
        # Click the buttons
        self.button_close_app_overlay.clicked.connect(self.close_app)
        self.button_open_settings.clicked.connect(self.show_page_settings)
        self.button_settings_back.clicked.connect(self.button_back_main_page)
        self.button_display_build_back.clicked.connect(self.button_back_main_page)
        self.slider_opacity.valueChanged.connect(self.slide_it)      
        self.button_set_small_size.clicked.connect(lambda: self.set_window_size(Size.SMALL)) 
        self.button_set_medium_size.clicked.connect(lambda: self.set_window_size(Size.MEDIUM))
        self.button_set_large_size.clicked.connect(lambda: self.set_window_size(Size.LARGE))     
        self.button_start_scrolling.clicked.connect(self.button_start_timer)     
        
        # Define first view
        self.stackedWidget.setCurrentWidget(self.page_overlay)
        
        
        self.builds = self.request_instance.get_all_builds()
        
        if len(self.builds) > 0:
            for element in self.builds:
                self.verticalLayout_9.addWidget(ButtonBuild(element, overlay_instance=self))

    def button_start_timer(self):
        self.timer_instance.start_timer()
        self.button_start_scrolling.hide()

    def button_back_main_page(self):
        self.stackedWidget.setCurrentWidget(self.page_overlay)
        self.timer_instance.reset_timer()
        
    def get_build(self, build_id):
        self.show_page_display_build()
    
    def slide_it(self, value):
        self.setWindowOpacity(value/100)
        
    def close_app(self):
        sys.exit()
        
    def show_page_settings(self):
        self.stackedWidget.setCurrentWidget(self.page_settings)
        
    def show_page_overlay(self):
        self.stackedWidget.setCurrentWidget(self.page_overlay)
        
    def show_page_display_build(self):
        self.stackedWidget.setCurrentWidget(self.page_display_build)
        
    def set_window_size(self, size_enum):
        size_data = size_enum.value
        self.resize(size_data['width'], size_data['height'])