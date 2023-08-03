import numpy as np
from pydub import AudioSegment


song = AudioSegment.from_wav("../data/xTOk1Jz-F_g_0000015.wav")
backwards = song.reverse()
backwards.export(out_f="../data/reverse.wav", format='wav')
song = AudioSegment.append(song, backwards)  #把两段语音拼接在一起
song = AudioSegment.__add__(song, backwards) #把两段语音拼接在一起
song = AudioSegment.__mul__(song, backwards) #把两段语音叠加在一起
song.export(out_f="../data/reverse_add.wav", format='wav')

