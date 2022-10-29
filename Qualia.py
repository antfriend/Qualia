
import os
from pickle import TRUE
import this
import keyboard
import time
import subprocess
subprocess.run('', shell=True)

os.system("cls")

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

def move (y, x):
    print('\033[%d;%dH' % (y, x))

def blink():
    move(1,1)
    print(G+'-_-'+W)
    time.sleep(.1)
    move(1,1)
    print(G+'o_o'+W)
    print(' ')
    time.sleep(.1)

def setup():
    blink()
    print(' ')

def loop():
    thisKey = keyboard.read_key()
    if thisKey == 'esc':
        print('escape')
        return False
    
    return True

setup()
while loop():
    blink()

print('good')
print('bye')
print(' ')
