# pip install pydub
# download portable and set path ffmpeg

import os,sys
from os import path
from pydub import AudioSegment


# files                                                                         
src = sys.path[0] + "\\TestAudio\\CuTheRoiXa_Yentatoo.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
print("Convert Successfuly!")