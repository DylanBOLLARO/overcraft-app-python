# Form implementation generated from reading ui file 'c:\Users\BOLLARO\workspace\overcraft-app-python\ui\login.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.widget.setStyleSheet("background-color: \"#030711\";\n"
"border-radius:10;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 10, 600, 75))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: \"#f8faff\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_email.setGeometry(QtCore.QRect(60, 130, 471, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("QLineEdit {\n"
"    background-color: \"#030711\";\n"
"    border : 2px solid #1d283a;\n"
"    padding-left:20px;\n"
"    color: \"#dfe2e5\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border : 2px solid #435c86;\n"
"}\n"
"\n"
"")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setPlaceholderText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_password.setGeometry(QtCore.QRect(60, 230, 471, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
"    background-color: \"#030711\";\n"
"    border : 2px solid #1d283a;\n"
"    padding-left:20px;\n"
"    color: \"#dfe2e5\";\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border : 2px solid #435c86;\n"
"}\n"
"\n"
"")
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.button_login = QtWidgets.QPushButton(parent=self.widget)
        self.button_login.setGeometry(QtCore.QRect(150, 320, 300, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.button_login.setFont(font)
        self.button_login.setStyleSheet("QPushButton {\n"
"    background-color: \"#f8faff\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: \"#dfe2e5\";\n"
"}\n"
"")
        self.button_login.setObjectName("button_login")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: \"#f8faff\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: \"#f8faff\";")
        self.label_3.setObjectName("label_3")
        self.button_close_app_login = QtWidgets.QPushButton(parent=self.widget)
        self.button_close_app_login.setGeometry(QtCore.QRect(550, 0, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button_close_app_login.setFont(font)
        self.button_close_app_login.setStyleSheet("QPushButton:hover {\n"
"    background-color: #0d1325;\n"
"}")
        self.button_close_app_login.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\BOLLARO\\workspace\\overcraft-app-python\\ui\\../images/close.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_close_app_login.setIcon(icon)
        self.button_close_app_login.setIconSize(QtCore.QSize(32, 32))
        self.button_close_app_login.setObjectName("button_close_app_login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "OverCraft"))
        self.button_login.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Email"))
        self.label_3.setText(_translate("Form", "Password"))
