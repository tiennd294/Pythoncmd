# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 159)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(20, 10, 75, 24))
        self.btnOpen.setObjectName("btnOpen")
        self.lbl_audio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_audio.setGeometry(QtCore.QRect(20, 50, 281, 16))
        self.lbl_audio.setObjectName("lbl_audio")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(20, 80, 75, 24))
        self.btnRun.setAutoDefault(False)
        self.btnRun.setObjectName("btnRun")
        self.btnRun.clicked.connect(self.btnRun_Click)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 21))
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
        self.btnOpen.setText(_translate("MainWindow", "Open"))
        self.lbl_audio.setText(_translate("MainWindow", "demo Form"))
        self.btnRun.setText(_translate("MainWindow", "Run..."))

    def btnRun_Click(self):
        msg = QMessageBox()
        msg.setWindowTitle("Infomation!")
        msg.setText("Demo Form OK")
        x = msg.exec_()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())