from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont

# Custom
from components.label_step import ContainerLabelStep

class ButtonBuild(QPushButton):
    def __init__(self, build, overlay_instance):
        super(ButtonBuild, self).__init__()
        self.build = build
        self.overlay_instance = overlay_instance
        self.steps = None

        
        # Set the button text to the title from self.build
        self.setText(self.build['title'])
        
        # Connect the clicked signal to a lambda function that prints the title
        self.clicked.connect(self.button_clicked)
        
        # Style
        self.setStyleSheet('''
            QPushButton {
                background-color: #030711;
                border: 2px solid #1d283a;
                padding: 10px;
                color: #dfe2e5;
            }
            
            QPushButton:hover {
                background-color: #0d1325;
            }
        ''')
        self.setFont(QFont('Roboto', 14))
        
    def button_clicked(self):
        # Disconnect any existing connections
        self.overlay_instance.timer_instance.timer.timeout.disconnect()
        # Connect the timeout signal to the refresh_label_displayed method
        self.overlay_instance.timer_instance.timer.timeout.connect(self.overlay_instance.timer_instance.update_timer)
        self.overlay_instance.timer_instance.timer.timeout.connect(self.refresh_label_displayed)
        
        self.overlay_instance.get_build(self.build["id"])
        self.overlay_instance.label_name_build.setText(self.build['title'])
        self.steps = sorted(self.overlay_instance.request_instance.get_all_steps_of_build_by_build_id(self.build["id"]), key=lambda x: x['position'])
        self.overlay_instance.button_start_scrolling.show()
        
        while self.overlay_instance.verticalLayout_10.count() > 0:
            item = self.overlay_instance.verticalLayout_10.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                
        self.refresh_label_displayed()
                
    def refresh_label_displayed(self):
        self.overlay_instance.timer_instance.timer_delta = sum(1 for d in self.steps if 'timer' in d and d['timer'] < self.overlay_instance.timer_instance.time_counter)
        # Clear the existing labels from the layout
        for i in reversed(range(self.overlay_instance.verticalLayout_10.count())):
            self.overlay_instance.verticalLayout_10.itemAt(i).widget().setParent(None)

        # Create and add LabelStep instances to the layout based on self.steps
        for index, element in enumerate(self.steps):
            if index >= 0+self.overlay_instance.timer_instance.timer_delta and index < self.overlay_instance.number_of_element_to_display+self.overlay_instance.timer_instance.timer_delta:
                label_step = ContainerLabelStep(element)
                self.overlay_instance.label_list_references.append(label_step)
                self.overlay_instance.verticalLayout_10.addWidget(label_step)
            