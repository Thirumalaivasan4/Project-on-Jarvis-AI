import keyboard
import pyttsx3
import psutil
engine=pyttsx3.init('sapi5')#init means INIT
voices=engine.getProperty('voices')#from engine we need the voices 
#print(voices)
engine.setProperty('voice',voices[1].id)#to set voice-->(name: Any, value: Any)
print(voices[1].id)
battery = psutil.sensors_battery()
percent = battery.percent
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__ == "__main__":
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            speak(event.name)