import os,sys
from os import path
from pydub import AudioSegment
from pydub.playback import play

# files                                                                         
src = sys.path[0] + "\\TestAudio\\CuTheRoiXa_Yentatoo.mp3"
print("____Playing......")
play(AudioSegment.from_mp3(src))
print("____Playing Successfuly!")