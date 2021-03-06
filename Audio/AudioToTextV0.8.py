# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioToText.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import sys, os, shutil
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
# from pydub.playback import play

class Ui_AudioToText(object):

    def setupUi(self, AudioToText):
        AudioToText.setWindowIcon(QtGui.QIcon("_data/python2.png")) 
        # AudioToText.setWindowIcon(QtGui.QIcon(sys.path[0] + "/python2.png")) 
        AudioToText.setObjectName("AudioToText")
        AudioToText.resize(425, 351)
        self.centralwidget = QtWidgets.QWidget(AudioToText)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setGeometry(QtCore.QRect(20, 10, 75, 24))
        self.btnOpen.setObjectName("btnOpen")
        self.lbl_audio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_audio.setGeometry(QtCore.QRect(110, 10, 301, 16))
        self.lbl_audio.setObjectName("lbl_audio")
        self.btnSaveAs = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveAs.setGeometry(QtCore.QRect(20, 80, 75, 24))
        self.btnSaveAs.setAutoDefault(False)
        self.btnSaveAs.setObjectName("btnSaveAs")
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setGeometry(QtCore.QRect(20, 278, 75, 24))
        self.btnTest.setAutoDefault(False)
        self.btnTest.setObjectName("btnTest")
        self.txtData = QtWidgets.QTextEdit(self.centralwidget)
        self.txtData.setGeometry(QtCore.QRect(110, 30, 301, 241))
        self.txtData.setObjectName("txtData")
        self.txtTest = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTest.setGeometry(QtCore.QRect(110, 280, 301, 20))
        self.txtTest.setObjectName("txtTest")
        AudioToText.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AudioToText)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        AudioToText.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AudioToText)
        self.statusbar.setObjectName("statusbar")
        AudioToText.setStatusBar(self.statusbar)

        self.btnOpen.clicked.connect(self.btnOpen_Click)
        self.btnSaveAs.clicked.connect(self.btnSaveAs_Click)
        self.btnTest.clicked.connect(self.btnTest_Click)
        self.btnSaveAs.setEnabled(False)
        self.btnSaveAs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(AudioToText)
        QtCore.QMetaObject.connectSlotsByName(AudioToText)

    def retranslateUi(self, AudioToText):
        _translate = QtCore.QCoreApplication.translate
        AudioToText.setWindowTitle(_translate("AudioToText", "AudioToText"))
        self.btnOpen.setText(_translate("AudioToText", "Open"))
        self.lbl_audio.setText("Open the .wav file!")
        self.btnSaveAs.setText(_translate("AudioToText", "Save As..."))
        self.btnTest.setText(_translate("AudioToText", "Test"))

    def btnOpen_Click(self):
        path, _ = QFileDialog.getOpenFileName(None, "Open Audio files", "","Sound Files (*.wav)")
        # audio = path.replace("/","\\")
        # path='audiototext.wav'
        if path != "":
            self.lbl_audio.setText("Converting audio file to text...")
            r = sr.Recognizer()
            sound = AudioSegment.from_wav(path)
            chunks = split_on_silence(sound,
                min_silence_len = 500,
                silence_thresh = sound.dBFS-14,
                keep_silence=500,
            )
            folder_name = "audio-data"
            if not os.path.isdir(folder_name):
                os.mkdir(folder_name)
            whole_text = ""
            for i, audio_chunk in enumerate(chunks, start=1):
                chunk_filename = os.path.join(folder_name, f"audio{i}.wav")
                audio_chunk.export(chunk_filename, format="wav")
                with sr.AudioFile(chunk_filename) as source:
                    audio_listened = r.record(source)
                    try:
                        text = r.recognize_google(audio_listened,language="vi-VI")
                    except Exception as ex:
                        self.txtData.setText("False Loading!!!\n" + str(ex) + "\n" + path + "\n")
                    else:
                        text = f"{text.capitalize()}. "
                        # print(chunk_filename, ":", text)
                        print(text)
                        whole_text += text
            self.txtData.setText(whole_text)
            shutil.rmtree(folder_name)
            self.lbl_audio.setText("Successfuly!")
            self.btnSaveAs.setEnabled(True)


    def btnSaveAs_Click(self):
        try:
            file, _ = QFileDialog.getSaveFileName(None,"Save As", "","Text Files (*.txt)")
            if self.txtData.toPlainText() != "":
                with open(file, mode = 'w', encoding = 'utf-8') as x_file:
                    x_file.write(self.txtData.toPlainText())
                    self.txtTest.setText("Covert Successfuly!")
                    self.lbl_audio.setText("Save As Successfuly!")
                    self.btnOpen.setEnabled(True)
                    self.btnSaveAs.setEnabled(False)
        except Exception as ex:
            self.txtTest.setText("False Saveas!!!" + str(ex))
            # print("Demo"+(str(ex)))

    def btnTest_Click(self):
        self.txtTest.setText("demo OK")


if __name__ == "__main__":
    try:
        # sys.stdout.reconfigure(encoding='utf-8')
        # sys.stdin.reconfigure(encoding='utf-8')
        # sys.stderr.reconfigure(encoding='utf-8')

        app = QtWidgets.QApplication(sys.argv)
        styles = """
            QWidget{
                background-color: #cecece;
            }
            QPushButton{
                color: #FFFFFF;
                background-color: #4B8DF8;
                border-width: 0;
                font-size: 12px;
                outline: none !important;
                text-align: center;
                border-style: outset;
            }
            QPushButton:hover{
                background-color: #2977f7;
            }
            QPushButton:disabled{
                background-color: #eeeeee;
                color: #333;
            }
            QTextEdit {
                font-family: "MS Shell Dlg 2"; 
                font-size: 8.25pt; 
                font-weight: 400; 
                font-style: normal;
                background-color: #FFFFFF;
            }
            QLineEdit{
                font-size: 12px;
                border: none;
                border-bottom: 2px solid purple;
            }
            QLineEdit:focus{
                border: none;
                border-bottom: 2px solid red;
            }
        """
        app.setStyleSheet(styles)
        AudioToText = QtWidgets.QMainWindow()
        ui = Ui_AudioToText()
        ui.setupUi(AudioToText)
        AudioToText.show()
        sys.exit(app.exec())
    except Exception as ex:
        # self.lbl_audio.setText("False Main!!!" + str(ex))
        print(ex)
