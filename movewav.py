
open('/Users/beefowler/desktop/Test.wav')
wav1 = '/Users/beefowler/desktop/Test.wav'
import os
import shutil

open (wav1, "w").close ()
wav2 = '/Users/beefowler/desktop/TestCopy.wav'
print wav1, "=>", wav2

shutil.copy (wav1, wav2)

if os.path.isfile (wav2): print "Success"

