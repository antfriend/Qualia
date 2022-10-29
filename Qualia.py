
import os
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
    loopies = 0q
    while True:
        loopies = loopies + 1
        time.sleep(.01)
        if loopies > 100:
            loopies = 0
            blink()

        if keyboard.is_pressed("q"):
            print("You pressed q")
            break

setup()
loop()

print(W+'i r Qualia ')
print(' ')
