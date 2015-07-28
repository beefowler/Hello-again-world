
wav1_path = '/Users/beefowler/desktop/0324.DSG_RAWD_HMS_12_55_ 0__DMY_19_ 1_11.wav'
# wav1_path = '/Users/mfowler/Desktop/test.txt'

wav1_file = open(wav1_path)
# you could read the file and do stuff with it here, but we're just going to close it
wav1_file.close()

import os
import shutil

wav2_path = '/Users/beefowler/desktop/test_name.wav'
# wav2_path = '/Users/mfowler/Desktop/test2.txt'

# we store the boolean (true or false) in a variable here
is_wav2_already_a_file = os.path.isfile(wav2_path)
if is_wav2_already_a_file:
    print "wav2 was already a file: " + wav2_path
else:
    print "wav2 was not already a file before copying: " + wav2_path

# this command copies a file
shutil.copy(wav1_path, wav2_path)

wav2_file = open(wav2_path)
# you could read the file and do stuff with it here, but we're just going to close it
wav2_file.close()

if os.path.isfile(wav2_path): print "Success"
