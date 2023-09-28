import pyautogui as pi
import datetime
hour=int(datetime.datetime.now().hour)
date1=int(datetime.datetime.now().minute)
sec=int(datetime.datetime.now().second)
print("The Current time is: ",hour,':',date1,':',sec)
h=int(input("Enter the time to shutdown in 24 hours: "))
m=int(input("Enter the minutes to shutdown: "))
while True:
    hour=int(datetime.datetime.now().hour)
    date=int(datetime.datetime.now().minute)
    sec=int(datetime.datetime.now().second)
    
    if(m>=30):
            if(h==hour and m==date):
                pi.press('win')
                pi.press('win')
                pi.hotkey('win','x')
                pi.press('u')
                pi.press('u')
    else:
            if(h==hour and m==date):
                pi.hotkey('win','x')
                pi.press('u')
                pi.press('u')
 

    
