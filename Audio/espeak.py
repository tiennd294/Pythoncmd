# Text to speech in python


# Text to speech (TTS) is the conversion of written text into spoken voice.You can create TTS programs in python. The quality of the spoken voice depends on your speech engine.

# In this article you’ll learn how to create your own TTS program.

# Related course: Complete Python Programming Course & Exercises

# Text to speech in python
# Example with espeak
# The program ‘espeak’ is a simple speech synthesizer which converst written text into spoken voice. The espeak program does sound a bit robotic, but its simple enough to build a basic program.

import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

a = "Say something in natural language."

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix(c)


# TTS with Google
# Google has a very natural sounding voices. You can use their TTS engine with the code below.
# For this program you need the module gTTS installed as well as the program mpg123.

# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

# from gtts import gTTS
# import os

# # define variables
# s = "escape with plane"
# file = "file.mp3"

# # initialize tts, create mp3 and play
# tts = gTTS(s, 'en')
# tts.save(file)
# os.system("mpg123 " + file)


# This will output spoken voice / an mp3 file.