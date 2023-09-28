import Jarvis
import time
import pyautogui
pyautogui.FAILSAFE=False
while True:
    time.sleep(10)
    Jarvis.speak("Hello ")
    time.sleep(10)
    pyautogui.typewrite("Amma@12345",interval=0.25)
    time.sleep(3)
    pyautogui.press('enter')
    break
