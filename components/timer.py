from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.time_counter = 0
        self.timer.timeout.connect(self.update_timer)
        self.timer_delta = 0

    def define_label(self, QLabel=None):
        self.label_timer_scrolling = QLabel

    def start_timer(self):
        self.timer.start(1000)
        
    def pause_timer(self):
        self.timer.stop()

    def unpause_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)

    def reset_timer(self):
        self.timer.stop()
        self.time_counter = 0
        self.label_timer_scrolling.setText('00:00')

    def update_timer(self):
        self.time_counter += 1
        self.label_timer_scrolling.setText("{:02}:{:02}".format(self.time_counter // 60, self.time_counter % 60))
        