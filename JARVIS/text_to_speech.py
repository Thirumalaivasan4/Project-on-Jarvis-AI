from gtts import gTTS
import playsound
import os
language = "en-in"
text = "hi I am Jarvis"
speech = gTTS(text=text, lang=language, tld="com.au")
speech.save("temp.mp3")
playsound.playsound("temp.mp3")
os.remove("temp.mp3")
