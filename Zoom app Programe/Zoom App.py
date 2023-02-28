import time
import webbrowser as w
from ZoomAppData import *
from pynput.keyboard import *
from threading import *
import datetime as dt


DATE=dt.date.today()
current_time = dt.datetime.now().strftime("%H:%M:%S")
# todo time counter methode

def comedown():
    while True:
        Time = details[2]

        time.sleep(1)

        # todo get current time
        current_time = dt.datetime.now().strftime("%H:%M:%S")

        print(current_time, Time)


        if Time == current_time:
            Zoomapp()
t=Thread(target=comedown)
t.start()

# todo zoom process

def Zoomapp():
    isStaretd = False
    keyword = Controller()
    while True:
        if isStaretd == False:
            w.open(details[0])
            isStaretd = True

        elif isStaretd == True:
            if details[3] == current_time:
                keyword.press('w')
                time.sleep(1)
                keyword.press(Key.enter)
                isStaretd = False
                break






