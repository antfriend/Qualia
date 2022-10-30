# from asyncio.windows_events import NULL
import os
# from pickle import TRUE
# import this
# from tkinter import Variable
import keyboard
import time
# import subprocess
# subprocess.run('', shell=True)
from algoliasearch.search_client import SearchClient
os.system("cls")
#
# ansi color codes - aka "VT100" https://en.wikipedia.org/wiki/VT100
# more here https://wiki.bash-hackers.org/scripting/terminalcodes
#
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
# HIDE = '\033[25h'
    
client = SearchClient.create("UBHJRCJSD3", "")
index = client.init_index("qualia")

intype = ' '

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
    input()
    print(' ')

def input():
    global intype
    move(3,3)
    print(G + '[' + W + intype + G + ']' + W)


def interpreKey(thisKey):
    global intype
    match thisKey:
        case 'esc':
            move(5,1)
            print('escape')
            return False
        case 'enter':
            move(5,1)
            record = {"objectID": 1, "name": intype}
            index.save_object(record).wait()
            results = index.search(intype)
            print(results["hits"][0])
            return True
        case _:
            intype += thisKey
            return True

def loop():
    thisKey = keyboard.read_key()
    reloop = interpreKey(thisKey)
    input()
    return reloop

setup()
while loop():
    blink()

print('good')
print('bye')
print(' ')
