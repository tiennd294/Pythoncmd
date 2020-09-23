import sys, os
import speech_recognition
from os import path
from gtts import gTTS
from datetime import date,datetime
from pydub import AudioSegment
from pydub.playback import play

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

robot_brain = ""
robot_ear = speech_recognition.Recognizer()
you = ""

def texttospeech(text):
    output = gTTS(text,lang="vi", slow=False)
    output.save(sys.path[0] + "\\TestAudio\\output.mp3")
    mp3 = AudioSegment.from_mp3(sys.path[0] + "\\TestAudio\\output.mp3")
    play(mp3)
    # os.system("mpg123 " + sys.path[0] + "\\TestAudio\\output.mp3")
    os.remove(sys.path[0] + "\\TestAudio\\output.mp3")
    print("Robot:..." + text + "\n")

def speechtotext(you = ""):
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
			texttospeech(robot_brain)
	return you

while True:

	you = speechtotext()
	if "Xin" in you:
		texttospeech("chào bạn")
		

	elif "meo" in you:
		texttospeech("Bạn rất thích con mèo")

	elif "123" in you:
		texttospeech("tạm biệt, hẹn gặp lại")
		break

	else: 
		robot_brain = "Tôi chưa được training câu hỏi này"
		texttospeech(robot_brain)


