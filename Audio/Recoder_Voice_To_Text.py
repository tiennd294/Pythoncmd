# Audio To Text
import os,sys
import speech_recognition as sr
from os import path
from pydub import AudioSegment

r = sr.Recognizer()
with sr.Microphone() as mic:
	print("I'm listening...")
	audio = r.listen(mic)
	print("...")
	try:
		data = r.recognize_google(audio,language="vi-VI")
		print("Transcription: " + data)
	except:
		print("Error! ...")                