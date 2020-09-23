# Convert MP3 to WAV
# You can convert MP3 directly to WAV in Python. In this article we’ll use a Python 3 to do the conversion. For this tutorial, any file will work.

# To start, first install ffmpeg. ffmpeg is a free program for audio, video and multimedia processing. The program has a console interface, but except from installing it there’s not much neccessary.

# Related course: Complete Python Programming Course & Exercises

# Example
# Pydub
# Install the module pydub. This is an audio manipulation module for Python. This module can open many multimedia audio and video formats. You can install this module with pip.

# pip install pydub
# If you have not installed ffmpeg yet, install it. You can use your package manager to do that.

# For Ubuntu / Debian Linux:

# apt-get install ffmpeg
# MP3 to WAV conversion
# You can convert an mp3 file (src) to a wav file (dst) by changing the variable names.

# The mp3 file must exist in the same directory as the program (.py). If you want to use custom directories, add a path to the filename.

from os import path
from pydub import AudioSegment

# files                                                                         
src = sys.path[0] + "\\TestAudio\\"+"transcript.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


# The program above uses the module pydub to do the conversion. That module uses ffmpeg itself, meaning ffmpeg must be installed for this to succeed.

# Run with:

# python3 convert.py
# Wait for the program the complete.

# You should have another file in your directory:

# convert mp3 to wav