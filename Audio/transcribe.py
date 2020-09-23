# Audio To Text

# Transcribe Audio
# You can transcribe an audio file automatically with Python.

# If you have an audio file with spoken words, the program will output a transcription of that audio file completely automatically.

# This example uses English as input language for the audio file, but technically any language can be used as long as the speech recognition engine supports it.

# Related course: Complete Python Programming Course & Exercises

# Example
# Start of by creating an audio file with some speech. This can be any audio file with English words. Save the file as transcript.mp3

# If you are unsure where to get an spoken words audio file, you can use Bluemix to generate one.

# Install prequisites
# To run the app you need several things installed:

# Python 3
# the module pydub
# the program ffmpeg
# the module SpeechRecognition
# You can install the Python modules with pip. ffmpeg can be installed with your package manager (apt-get, emerge, yum, pacman)

# Transcribe
# Audio transcription works by a few steps:

# mp3 to wav conversion,
# loading the audio file,
# feeding the audio file to a speceh recongition system.
# Copy the program below and save it as transcribe.py
import os,sys
import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav  
# urlMp3 = sys.path[0] + "\\TestAudio\\CuTheRoiXa_Yentatoo.mp3"                                                     
# sound = AudioSegment.from_mp3(urlMp3)
# dst = urlMp3.replace(".mp3",".wav")
# sound.export(dst, format="wav")


# transcribe audio file                                                         
AUDIO_FILE = sys.path[0] + "\\Audio.wav" 

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
		# r.adjust_for_ambient_noise(source)
        audio = r.listen(source)  # read the entire audio file                  
        data = r.recognize_google(audio,language="vi-VI")
        print("Transcription: " + data)

        
# Run the program with:

# python3 transcribe.py
# It will output the transcription of the original audio file.