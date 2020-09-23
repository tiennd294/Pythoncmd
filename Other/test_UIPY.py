import tkinter as tk
from tkinter import *
from mainwindow import*
import os
import sys

# root = tk.Tk()
# canvas = tk.Canvas(root, height = 400, width = 400, bg = "#256432")
# canvas.pack()

# frame = tk.Frame(root, bg = "white")
# frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

# root.mainloop()

class MyWin(QtWidgets.QMainWindow):

	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
# 		self.btnOpen.clicked.connect(clickdemo)

# def clickdemo():
#     self.lbl_audio.setText("Day la Ok")

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec())
