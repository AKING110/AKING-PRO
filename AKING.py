import os
from platform import uname
arch=uname().machine.lower()
if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
    import pro
else:exit('\033[1;31m Sorry System or device not supported ')
    
