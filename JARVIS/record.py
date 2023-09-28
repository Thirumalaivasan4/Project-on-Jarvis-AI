from gtts import gTTS
import playsound
import os
language = "en-in"
text = "ASDFGF ;LKJHJ"
speech = gTTS(text=text, lang=language, tld="com.au")
# Save the speech to a temporary file (you can use any file name)
speech.save("temp1.mp3")