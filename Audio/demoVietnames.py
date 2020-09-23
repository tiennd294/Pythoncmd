import sys, os
import speech_recognition as sr
# import pyaudio
from gtts import gTTS
# import playsound
from pydub import AudioSegment

#Python 2
# sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
# sys.stdin = codecs.getreader('utf_8')(sys.stdin)
#Python 3
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Moi ban noi: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            print("Bạn -->: {}".format(text))
        except:
            print("Xin lỗi! tôi không nhận được voice!")
    return text



# text = "tôi có thể giúp gì cho bạn" 
def texttospeech(text):
    output = gTTS(text,lang="vi", slow=False)
    output.save("output.mp3")
    os.system("mpg123 " + "output.mp3")
    # playsound.playsound('output.mp3', True)
    os.remove("output.mp3")
    print(text)


# Main
while True:
    text = speechtotext()
    if "in" in text:
        texttospeech("chào bạn")
    elif "tên" in text:
        texttospeech("tôi là trợ lý ảo quán trà ai")
    elif "Bye" in text:
        break
    else:
        texttospeech("xin lỗi tôi chưa thông minh nên không hiểu câu này")