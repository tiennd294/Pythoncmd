import sys
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import playsound
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


robot_brain = ""
robot_ear = sr.Recognizer()

you = ""


# text = "tôi có thể giúp gì cho bạn không" 
# output = gTTS(text,lang="vi", slow=False)
# output.save("output.mp3")
# playsound.playsound("output.mp3", True)
# print("demo ok")
# os.remove("output.mp3")
while True:
    robot_ear = sr.Recognizer()
    with sr.Microphone() as mic:
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
        robot_brain = "Chao ban!"
        # robot_mouth.say(robot_brain)
        # robot_mouth.runAndWait()
    elif "meo" in you:
        robot_brain = "Ban rat thich con meo"
        
    elif "123" in you:
        robot_brain = "Tam biet!"
        # robot_mouth.say(robot_brain)
        # robot_mouth.runAndWait()
        break
    else: robot_brain = "Error!"

    print(robot_brain)
    