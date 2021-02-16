# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer_interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setFixedSize(273, 315)
		MainWindow.setStyleSheet("background-color: rgb(90, 214, 132);")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(190, 100, 75, 23))
		self.pushButton.setStyleSheet(".QPushButton {\n"
"background-color: rgb(196, 208, 206);\n"
"font-weight: 600;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"    background-color: rgb(156, 156, 156)\n"
"}")	
		self.pushButton.setObjectName("pushButton")
		self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_2.setGeometry(QtCore.QRect(110, 90, 59, 31))
		self.spinBox_2.setStyleSheet("font-size: 16px;\n"
"background-color: rgb(196, 208, 206);\n"
"font-weight: 600;\n"
"height: 15px;")
		self.spinBox_2.setObjectName("spinBox_2")
		self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_3.setGeometry(QtCore.QRect(110, 50, 59, 31))
		self.spinBox_3.setStyleSheet("font-size: 16px;\n"
"background-color: rgb(196, 208, 206);\n"
"font-weight: 600;\n"
"height: 15px;")
		self.spinBox_3.setObjectName("spinBox_3")
		self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_4.setGeometry(QtCore.QRect(110, 10, 59, 31))
		self.spinBox_4.setStyleSheet("font-size: 16px;\n"
"background-color: rgb(196, 208, 206);\n"
"font-weight: 600;\n"
"height: 15px;")
		self.spinBox_4.setObjectName("spinBox_4")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 10, 81, 31))
		self.label.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font-weight: 600;\n"
"font-size: 15px;\n"
"border-radius: 6px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 90, 81, 31))
		self.label_2.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font-weight: 600;\n"
"font-size: 15px;\n"
"border-radius: 6px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 31))
		self.label_3.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font-weight: 600;\n"
"font-size: 15px;\n"
"border-radius: 6px;\n"
"padding-left: 5px;\n"
"padding-right: 5px;")
		self.label_3.setObjectName("label_3")
		self.listView = QtWidgets.QListView(self.centralwidget)
		self.listView.setGeometry(QtCore.QRect(10, 130, 256, 161))
		self.listView.setObjectName("listView")
		label_y = 140
		for index in range(4, 10):
			label_name = 'label_' + str(index)
			button_name = 'button_' + str(index)
			self.__setattr__(label_name, QtWidgets.QLabel(self.centralwidget))
			self.__setattr__(button_name, QtWidgets.QPushButton(self.centralwidget))
			label = self.__getattribute__(label_name)
			button = self.__getattribute__(button_name)
			label.setGeometry(QtCore.QRect(20, label_y, 200, 13))
			label.setObjectName(label_name)
			button.setGeometry(QtCore.QRect(210, label_y, 0, 15)) # 35 - width
			label.setStyleSheet('font-size: 12px;')
			button.setStyleSheet('font-size: 12px;')
			label_y += 25

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Start"))
		self.label.setText(_translate("MainWindow", "Hours:"))
		self.label_2.setText(_translate("MainWindow", "Seconds:"))
		self.label_3.setText(_translate("MainWindow", "Minutes:"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(242, 141)
        Dialog.setStyleSheet("background-color: rgb(90, 214, 132);")
        icon = QtGui.QIcon('apple.ico')
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-110, 100, 311, 21))
        self.buttonBox.setStyleSheet("background-color: #fff;")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 141, 41))
        self.lineEdit.setStyleSheet("background-color: #fff;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(25)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 141, 16))
        self.label.setStyleSheet("font-weight: bold;\n"
"font-size: 16px;")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Reminder Name"))
