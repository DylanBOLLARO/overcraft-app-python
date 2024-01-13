from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget

class ContainerLabelStep(QWidget):
    def __init__(self, element):
        super().__init__()
        layout = QHBoxLayout()
        layout.setSpacing(5)
        layout.setContentsMargins(0,0,0,0)
        
        self.label_population = LabelStep(str(element["population"]))
        self.label_population.setStyleSheet(self.label_population.styleSheet() + "color: #e5c07b;")
        self.label_timer = LabelStep(f"{element['timer'] // 60:01}:{element['timer'] % 60:02}")
        self.label_timer.setStyleSheet(self.label_population.styleSheet() + "color: #98c379;")
        self.label_description = LabelStep(str(element["description"]))
        
        layout.addWidget(self.label_population )
        layout.addWidget(self.label_timer)
        layout.addWidget(self.label_description, 1)

        self.setLayout(layout)
        
class LabelStep(QLabel):
    def __init__(self, text):
        super().__init__()
        # Style
        self.setStyleSheet('''
                background-color: #030711;
                padding: 10px;
                color: #dfe2e5;
        ''')
        self.setFont(QFont('Roboto', 12))
        self.setText(text)
        self.setWordWrap(True)