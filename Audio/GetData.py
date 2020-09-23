import sys
import speech_recognition as sr
# import pyaudio
# from gtts import gTTS
# import playsound
import os
# from timeit import default_timer as timer
import threading 
# import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

text = ""

def AudioTotText(audio):
	r = sr.Recognizer()
	with sr.AudioFile(audio) as source:
		r.adjust_for_ambient_noise(source)
		print("Converting audio file to text...")
		sound = r.listen(source)
		try:
			text = r.recognize_google(sound,language="vi-VI")
		except Exception as ex:
			print(ex)
		return text

def save_txt(name,data = ""):
	print(text)
	if data != "":
	    file_name = name + '.txt'
	    with open(file_name, mode = 'w', encoding = 'utf-8') as x_file:
	        x_file.write(data)
#print(AudioTotText("Id1.500.wav"))
save_txt("Id1.500",AudioTotText("Id1.500.wav"))

# time = os.path.getmtime("Id1.500.wav")
# print(time)
# time = os.path.getmtime("Id1.500.m4a")
# print(time)

# import time
# while True:
# 	print (time.strftime("%H:%M:%S"))

