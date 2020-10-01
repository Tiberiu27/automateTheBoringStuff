#!python3
#lookingBusy.py - Moving the cursor every 10 minutes so the IM does not go idle.

import pyautogui, time

try:
    while True:
        pyautogui.move(5,5, 0.25)
        time.sleep(600)

except KeyboardInterrupt:
    print('Bye')