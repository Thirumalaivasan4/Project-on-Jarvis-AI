import datetime
import time
while True:
    hour=int(datetime.datetime.now().hour)
    date=int(datetime.datetime.now().minute)
    sec=int(datetime.datetime.now().second)
    print(hour,':',date,':',sec)
    time.sleep(1)
   
