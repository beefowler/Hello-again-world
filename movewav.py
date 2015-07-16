
open('/Users/beefowler/desktop/0324.DSG_RAWD_HMS_12_55_ 0__DMY_19_ 1_11.wav')
wav1 = '/Users/beefowler/desktop/0324.DSG_RAWD_HMS_12_55_ 0__DMY_19_ 1_11.wav'
import os
import shutil

open (wav1, "w").close ()
wav2 = wav1 + ".copy"
print wav1, "=>", wav2

shutil.copy (wav1, wav2)

if os.path.isfile (wav2): print "Success"
