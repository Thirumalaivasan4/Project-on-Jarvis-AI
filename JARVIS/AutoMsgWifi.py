import subprocess
import platform
import pywhatkit as pw
from datetime import datetime
myobj = datetime.now()
def get_wifi_name():
    system = platform.system()
    wifi_name = ""

    if system == "Windows":
        try:
            result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True, check=True)
            output = result.stdout
            lines = output.split('\n')
            for line in lines:
                if "SSID" in line:
                    wifi_name = line.split(":")[1].strip()
                    break
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    elif system == "Linux":
        try:
            result = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True, check=True)
            wifi_name = result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print("Error:", e)
    
    return wifi_name

if __name__ == "__main__":
    wifi_name = get_wifi_name()
    while True:
        if wifi_name=="VodafoneMobileWiFi-9918":
            i=1
            pw.sendwhatmsg("+919345973279","Thirumalaivasan was cconnected your WIFI.",myobj.hour,(myobj.minute+1),True,2)
            i=i+1
            if(i==2):
                break
        else:
            print("Unable to retrieve WiFi name.")
    
