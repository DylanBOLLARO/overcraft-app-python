# Form implementation generated from reading ui file 'c:\Users\BOLLARO\workspace\overcraft-app-python\ui\overlay.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 700)
        Form.setStyleSheet("border-radius:10;")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_1.setObjectName("page_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_open_settings = QtWidgets.QPushButton(parent=self.page_1)
        self.button_open_settings.setMinimumSize(QtCore.QSize(50, 50))
        self.button_open_settings.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_open_settings.setFont(font)
        self.button_open_settings.setStyleSheet("QPushButton {\n"
"    background-color: #030711;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_open_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\BOLLARO\\workspace\\overcraft-app-python\\ui\\../images/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_open_settings.setIcon(icon)
        self.button_open_settings.setIconSize(QtCore.QSize(32, 32))
        self.button_open_settings.setObjectName("button_open_settings")
        self.horizontalLayout_3.addWidget(self.button_open_settings)
        self.label_7 = QtWidgets.QLabel(parent=self.page_1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.button_close_app_overlay = QtWidgets.QPushButton(parent=self.page_1)
        self.button_close_app_overlay.setMinimumSize(QtCore.QSize(50, 50))
        self.button_close_app_overlay.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_close_app_overlay.setFont(font)
        self.button_close_app_overlay.setStyleSheet("QPushButton {\n"
"    background-color: #030711;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_close_app_overlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\BOLLARO\\workspace\\overcraft-app-python\\ui\\../images/close.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_close_app_overlay.setIcon(icon1)
        self.button_close_app_overlay.setIconSize(QtCore.QSize(32, 32))
        self.button_close_app_overlay.setObjectName("button_close_app_overlay")
        self.horizontalLayout_3.addWidget(self.button_close_app_overlay)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_6.addLayout(self.verticalLayout_9)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_6.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_3.setStyleSheet("")
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_display_build_back = QtWidgets.QPushButton(parent=self.page_3)
        self.button_display_build_back.setMinimumSize(QtCore.QSize(50, 50))
        self.button_display_build_back.setMaximumSize(QtCore.QSize(50, 50))
        self.button_display_build_back.setStyleSheet("QPushButton {\n"
"    background-color: #030711;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_display_build_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\BOLLARO\\workspace\\overcraft-app-python\\ui\\../images/chevron-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_display_build_back.setIcon(icon2)
        self.button_display_build_back.setIconSize(QtCore.QSize(32, 32))
        self.button_display_build_back.setObjectName("button_display_build_back")
        self.horizontalLayout.addWidget(self.button_display_build_back)
        self.label_name_build = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_build.setFont(font)
        self.label_name_build.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;")
        self.label_name_build.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name_build.setObjectName("label_name_build")
        self.horizontalLayout.addWidget(self.label_name_build)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout.addLayout(self.verticalLayout_10)
        spacerItem1 = QtWidgets.QSpacerItem(20, 542, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.button_start_scrolling = QtWidgets.QPushButton(parent=self.page_3)
        self.button_start_scrolling.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_start_scrolling.setFont(font)
        self.button_start_scrolling.setStyleSheet("QPushButton {\n"
"    background-color: \"#f8faff\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: \"#dfe2e5\";\n"
"}\n"
"")
        self.button_start_scrolling.setObjectName("button_start_scrolling")
        self.verticalLayout.addWidget(self.button_start_scrolling)
        self.label_timer_scrolling = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.label_timer_scrolling.setFont(font)
        self.label_timer_scrolling.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;")
        self.label_timer_scrolling.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_timer_scrolling.setObjectName("label_timer_scrolling")
        self.verticalLayout.addWidget(self.label_timer_scrolling)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setEnabled(True)
        self.page_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_settings_back = QtWidgets.QPushButton(parent=self.page_2)
        self.button_settings_back.setMinimumSize(QtCore.QSize(50, 50))
        self.button_settings_back.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_settings_back.setFont(font)
        self.button_settings_back.setStyleSheet("QPushButton {\n"
"    background-color: #030711;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_settings_back.setText("")
        self.button_settings_back.setIcon(icon2)
        self.button_settings_back.setIconSize(QtCore.QSize(32, 32))
        self.button_settings_back.setObjectName("button_settings_back")
        self.horizontalLayout_5.addWidget(self.button_settings_back)
        self.label_6 = QtWidgets.QLabel(parent=self.page_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.page_2)
        self.label.setMinimumSize(QtCore.QSize(0, 75))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;\n"
"padding: 10px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(parent=self.page_2)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalSlider.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;\n"
"padding: 10px;")
        self.horizontalSlider.setMinimum(20)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setProperty("value", 75)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksAbove)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 75))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: \"#f8faff\";\n"
"background-color: #030711;\n"
"padding: 10px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_set_small_size = QtWidgets.QPushButton(parent=self.page_2)
        self.button_set_small_size.setMinimumSize(QtCore.QSize(50, 50))
        self.button_set_small_size.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_set_small_size.setFont(font)
        self.button_set_small_size.setStyleSheet("QPushButton {\n"
"    background-color: \"#030711\";\n"
"    border : 2px solid #1d283a;\n"
"    padding-left:20px;\n"
"    color: \"#dfe2e5\";\n"
"    padding:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_set_small_size.setObjectName("button_set_small_size")
        self.horizontalLayout_2.addWidget(self.button_set_small_size)
        self.button_set_medium_size = QtWidgets.QPushButton(parent=self.page_2)
        self.button_set_medium_size.setMinimumSize(QtCore.QSize(50, 50))
        self.button_set_medium_size.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_set_medium_size.setFont(font)
        self.button_set_medium_size.setStyleSheet("QPushButton {\n"
"    background-color: \"#030711\";\n"
"    border : 2px solid #1d283a;\n"
"    padding-left:20px;\n"
"    color: \"#dfe2e5\";\n"
"    padding:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_set_medium_size.setObjectName("button_set_medium_size")
        self.horizontalLayout_2.addWidget(self.button_set_medium_size)
        self.button_set_large_size = QtWidgets.QPushButton(parent=self.page_2)
        self.button_set_large_size.setMinimumSize(QtCore.QSize(50, 50))
        self.button_set_large_size.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_set_large_size.setFont(font)
        self.button_set_large_size.setStyleSheet("QPushButton {\n"
"    background-color: \"#030711\";\n"
"    border : 2px solid #1d283a;\n"
"    padding-left:20px;\n"
"    color: \"#dfe2e5\";\n"
"    padding:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_set_large_size.setObjectName("button_set_large_size")
        self.horizontalLayout_2.addWidget(self.button_set_large_size)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.widget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "OverCraft"))
        self.label_name_build.setText(_translate("Form", "build_title"))
        self.button_start_scrolling.setText(_translate("Form", "START"))
        self.label_timer_scrolling.setText(_translate("Form", "00:00"))
        self.label_6.setText(_translate("Form", "Settings page"))
        self.label.setText(_translate("Form", "Window opacity"))
        self.label_2.setText(_translate("Form", "Window size"))
        self.button_set_small_size.setText(_translate("Form", "S"))
        self.button_set_medium_size.setText(_translate("Form", "M"))
        self.button_set_large_size.setText(_translate("Form", "L"))
