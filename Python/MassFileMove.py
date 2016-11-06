Program Title:      MassFileMove.py
Purpose:            Utilization of shutil module to effect moving all text files from one
                    folder to another by simply executing program.
Program Language:   Python
Language Version:   2.7.9
Platform Tested:    Windows 8.1 on x86 OS
Author:             Matt Kozlowski
Date Created:       October 13, 2016



import shutil
import os

print('contents of Origin Folder:')
for file in os.listdir('c:\\users\\matt\\desktop\\folder uno'):        
    print(os.path.join("c:\\users\\matt\\desktop\\folder uno", file))
    shutil.move(os.path.join("c:\\users\\matt\\desktop\\folder uno", file), os.path.join("c:\\users\\matt\\desktop\\dos", file))    

print('contents of Destination Folder:')
for file in os.listdir('c:\\users\\matt\\desktop\\dos'): 
    print(os.path.join("c:\\users\\matt\\desktop\\dos", file))

print('...and current contents of Origin Folder:')
print(os.listdir('c:\\users\\matt\\desktop\\folder uno'))
    
