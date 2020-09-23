# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioToText.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import speech_recognition as sr
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class Ui_AudioToText(object):

    _data = ""
    def setupUi(self, AudioToText):
        AudioToText.setObjectName("AudioToText")
        AudioToText.resize(323, 159)
        self.centralwidget = QtWidgets.QWidget(AudioToText)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(20, 10, 80, 24))
        self.btnOpen.setObjectName("btnOpen")
        self.btnOpen.clicked.connect(self.btnOpen_Click)
        self.lbl_audio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_audio.setGeometry(QtCore.QRect(20, 50, 281, 14))
        self.lbl_audio.setObjectName("lbl_audio")
        self.btnSaveAs = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveAs.setGeometry(QtCore.QRect(20, 80, 80, 24))
        self.btnSaveAs.setAutoDefault(False)
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.btnSaveAs.clicked.connect(self.btnSaveAs_Click)
        self.btnSaveAs.setEnabled(False)
        AudioToText.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AudioToText)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 21))
        self.menubar.setObjectName("menubar")
        AudioToText.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AudioToText)
        self.statusbar.setObjectName("statusbar")
        AudioToText.setStatusBar(self.statusbar)

        self.retranslateUi(AudioToText)
        QtCore.QMetaObject.connectSlotsByName(AudioToText)


    def retranslateUi(self, AudioToText):
        _translate = QtCore.QCoreApplication.translate
        AudioToText.setWindowTitle(_translate("AudioToText", "AudioToText"))
        self.btnOpen.setText(_translate("AudioToText", "Open && Run..."))
        self.lbl_audio.setText("Open the .wav file!")
        self.btnSaveAs.setText(_translate("AudioToText", "Save As..."))
        
    def btnOpen_Click(self):
        file, _ = QFileDialog.getOpenFileName(None, "Open Audio files", "","Sound Files (*.wav)")
        audio = file.replace("/","\\\\")
        self.lbl_audio.setText("Converting audio file to text...")

        if audio != "":
            r = sr.Recognizer()
            with sr.AudioFile(audio) as source:
                r.adjust_for_ambient_noise(source)
                sound = r.listen(source)
                try:
                    global _data
                    _data = r.recognize_google(sound,language="vi-VI")
                except Exception as ex:
                    print(ex)

        self.lbl_audio.setText("Successfuly!")
        self.btnSaveAs.setEnabled(True)

    def btnSaveAs_Click(self):
        file, _ = QFileDialog.getSaveFileName(None,"Save As", "","Text Files (*.txt)")
        global _data
        if _data != "":
            with open(file, mode = 'w', encoding = 'utf-8') as x_file:
                x_file.write(_data)
        
        self.lbl_audio.setText("Save As Successfuly!")
        self.btnOpen.setEnabled(True)
        self.btnSaveAs.setEnabled(False)

if __name__ == "__main__":

    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

    app = QtWidgets.QApplication(sys.argv)
    AudioToText = QtWidgets.QMainWindow()
    ui = Ui_AudioToText()
    ui.setupUi(AudioToText)
    AudioToText.show()
    sys.exit(app.exec())