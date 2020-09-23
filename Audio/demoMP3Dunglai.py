import sys, os
import pyttsx3
import speech_recognition
# import gtts
from datetime import date,datetime
from pydub import AudioSegment

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

robot_brain = ""
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
you = ""
#Robot listening....
# while True:
# 	with speech_recognition.Microphone() as mic:
# 		print("Robot: I'm listening...")
# 		audio = robot_ear.record(mic, duration = 5)
# 		print("Robot:...")

# 	try:
# 		you = robot_ear.recognize_google(audio, language = 'vi-VN')
# 		print("\nYou: " + you)
# 	except:
# 		robot_brain = "Toi khong hieu ban noi gi ! ..."
# 		print("Robot:..." + robot_brain)

# def texttospeech(text):
#     output = gTTS(text,lang="vi", slow=False)
#     output.save("output.mp3")
#     os.system("mpg123 " + "output.mp3")
#     os.remove("output.mp3")
#     print(text)
#     return text

# def speechtotext():
# 	robot_ear = speech_recognition.Recognizer()
# 	with speech_recognition.Microphone() as mic:
# 		print("Robot: I'm listening...")
# 		audio = robot_ear.listen(mic)
# 		print("Robot:...")
# 	try:
# 		you = robot_ear.recognize_google(audio,language="vi-VI")
# 		print("\nYou: " + you)
# 	except:
# 		robot_brain = "Tôi không hiểu bạn nói gì! ..."
# 		texttospeech("Robot:..." + robot_brain)
		


while True:
	robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening...")
		audio = robot_ear.listen(mic)
		print("Robot:...")
	try:
		you = robot_ear.recognize_google(audio,language="vi-VI")
		print("\nYou: " + you)
	except:
		robot_brain = "Tôi không hiểu bạn nói gì! ..."
		print("Robot:..." + robot_brain)

	if "Xin" in you:
		# texttospeech("chào bạn")
		robot_brain = "Chao ban!"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
	elif "meo" in you:
		# texttospeech("Bạn rất thích con mèo")
		robot_brain = "Ban rat thich con meo"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
	elif "123" in you:
		# texttospeech("tạm biệt, hẹn gặp lại")
		robot_brain = "Tam biet!"
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else: 
		robot_brain = "Tôi chưa hiểu bạn nói gì"
		print(robot_brain)
		robot_mouth.say(you)
		robot_mouth.runAndWait()
	