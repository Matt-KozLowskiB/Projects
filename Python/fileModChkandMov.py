##Program Name:      fileModChkandMov.py
##Purpose:           Use datetime, shutil, and OS modules to effect movement of files from
##                   one folder to another based upon time since last modification
##Program Language:  Python
##Language Version:  2.7.9
##Platform Tested:   Windows 8.1, x86(32bit)
##Author:            Matt Kozlowski
##Date Created:      10/14/16


import sys
import os
import shutil
import datetime
import time

dt = time.time()                                                                      # assign current time function to var dt

for file in os.listdir('c:\\users\\matt\\desktop\\folder uno'):                       # Identify each file in target folder
    print(os.path.join("c:\\users\\matt\\desktop\\folder uno", file))
    filestats = os.stat(os.path.join("c:\\users\\matt\\desktop\\folder uno", file))   # Get file attribute tuple, assign to var filesstats
    if ((int(dt) - int(filestats[8]))/3600)<24:                                       # compare last modification time to current time; check if< 24 HR
        shutil.copy2(os.path.join("c:\\users\\matt\\desktop\\folder uno", file), os.path.join("c:\\users\\matt\\desktop\\dos", file))
        print('The file: '+ file + ' has been copied due to recent modification')     # If < 24 HR, copy file to dest folder + print conf message  
    print("\n")
    
