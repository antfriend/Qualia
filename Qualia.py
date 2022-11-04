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

intype = ''

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
    render_Inputbox()
    print(' ')

def render_Inputbox():
    global intype
    move(3,1)
    print(G + '[' + W + intype + G + ']   ' + W)
    # time.sleep(.3)

def interpreKey(thisKey):
    global intype
    match thisKey:
        case 'esc':
            move(5,1)
            print('escape')
            return False
        case 'backspace':
            intype = intype[:-len(intype)-1]
            # blink()
            # time.sleep(.5)
            return True
        case 'space':
            intype += ' '
            return True
        case 'shift':
            return True
        case 'enter':
            blink()
            what_is_the_meaning_of_this(intype)
            intype = ''
            return True
        case _:
            intype += thisKey
            return True

def what_is_the_meaning_of_this(statement):

    record = {"objectID": statement.replace(" ", "_"), "statement": statement}
    index.save_object(record).wait()
    results = index.search(statement)

    move(5,1)
    print(results["hits"][0])

def loop():
    statement = input("your words") 
    what_is_the_meaning_of_this(statement)
    thisKey = keyboard.read_key()
    reloop = interpreKey(thisKey)

    return reloop

setup()
while loop():
    render_Inputbox()
    # blink()

print('good')
print('bye')
print(' ')
