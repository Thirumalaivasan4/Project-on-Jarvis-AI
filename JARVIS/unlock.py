import pyautogui
import time
def unlock_laptop():
    # Get the current password from the user.
    #password = input("Enter your password: ")
    # Type the password into the lock screen.
    pyautogui.typewrite("Amma@12345",interval=0.25)
    # Press the enter key to unlock the laptop.
    pyautogui.press("enter")
# Wait for the lock screen to appear.
time.sleep(20)
# Unlock the laptop.
unlock_laptop()