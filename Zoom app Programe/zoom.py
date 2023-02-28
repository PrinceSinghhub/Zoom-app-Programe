import time
import webbrowser as w
import dateandtimemodule as a
from zoomdata import *
from pynput.keyboard import *

DATE=a.date
TIME = a.time
isStaretd = False
keyword = Controller()

for i in data:
    if TIME == data[2]:
        while True:
            if isStaretd == False:
                if data[2] == TIME and data[1] == DATE:
                    w.open(data[0])
                    isStaretd = True
            elif isStaretd == True:
                if data[3] == TIME and data[1] == DATE:
                    keyword.press('w')
                    time.sleep(1)
                    keyword.press(Key.enter)
                    isStaretd = False
                    break
    else:
        print("Sorry time is Not Correct")
        break
