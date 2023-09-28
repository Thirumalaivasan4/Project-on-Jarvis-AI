import pywhatkit as pw
from datetime import datetime
myobj = datetime.now()
while True:
    pw.sendwhatmsg("+919345973279","Thirumalaivasan was cconnected your WIFI.",myobj.hour,(myobj.minute)+1)
    