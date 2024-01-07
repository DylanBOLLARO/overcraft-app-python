from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont

class ButtonBuild(QPushButton):
    def __init__(self, build, overlay_instance):
        super(ButtonBuild, self).__init__()
        self.build = build
        self.overlay_instance = overlay_instance

        # Set the button text to the title from self.build
        self.setText(self.build['title'])
        
        # Connect the clicked signal to a lambda function that prints the title
        self.clicked.connect(self.button_clicked)
        
        # Style
        self.setStyleSheet("QPushButton {"
            "background-color: #030711; "
            "border: 2px solid #1d283a; "
            "padding:5px;"
            "color: #dfe2e5; "
            "}"
            "QPushButton:hover {"
            "background-color: #0d1325; "
            "}")
        self.setFont(QFont('Roboto', 14))
        
    def button_clicked(self):
        self.overlay_instance.get_build(self.build["id"])
        self.overlay_instance.label_name_build.setText(self.build['title'])