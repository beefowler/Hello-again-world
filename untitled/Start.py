
__author__ = 'beefowler'

import wave

w = wave.open("Test.wav", "r")
print w.getparams()

w.close()