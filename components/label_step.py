from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont

class LabelStep(QLabel):
    def __init__(self, element):
        super(LabelStep, self).__init__()
        # Style
        self.setStyleSheet('''
            QLabel {
                background-color: #030711;
                border: 2px solid #1d283a;
                padding: 10px;
                color: #dfe2e5;
            }
        ''')
        self.setFont(QFont('Roboto', 14))
        self.setText(element["description"])
        self.setWordWrap(True)