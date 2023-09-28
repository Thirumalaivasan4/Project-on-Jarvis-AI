
import pyttsx3#module for voice recogination and speaking
import datetime
import speech_recognition as sr#to understand our language by machine
import wikipedia
import webbrowser
import os
import pyautogui as pi
import time
import Wifi
#FOR METHOD SPEAKING 
engine=pyttsx3.init('sapi5')#init means INIT
voices=engine.getProperty('voices')#from engine we need the voices 
#print(voices)
engine.setProperty('voice',voices[0].id)#to set voice-->(name: Any, value: Any)
print(voices[1].id)
print(voices[0].id)
def changevoice(query):
    
    if 'luna' in query.lower():
        speak("Now i am going to call The Luna.")
        engine.setProperty('voice',voices[1].id)
        speak("Hi boss i am Luna speaking")
    elif 'jarvis' in query.lower():
        speak("Now i am going to call The Jarvis.")
        engine.setProperty('voice',voices[0].id)
        speak("Hi boss i am jarvis speaking")
   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#For Wishing
def wishme():
     hour=int(datetime.datetime.now().hour)
     if hour<=0 and hour>12:
          speak("Good Morning Sir!" )
     if hour<=12 and hour>18:
           speak("Good afternoon sir!")
     else:
          speak("Good Evening Sir!")
     speak("What can i do for you today sir?")

def takecommand():
      r = sr.Recognizer()
      with sr.Microphone() as source:#Michropone class as source
        print("Listening....")
        r.pause_threshold = 1#r.function(second of non speaking audio-->default 0.8 here 1s )
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)#listen from r through source 

      try:
        print("wait for few moments")    
        query = r.recognize_google(audio, language='en-in')#works on internet 
        print("user said: ", query)
      except Exception as e:
        #print(e)    
        speak("Say that again please...") 
        return "None"
      return query 

if __name__ == "__main__":
   speak("Please  Enter   the  username   and   password in  below  Terminal To Acess me Sir")
   user=input("Please The Username: ")
   password1=int(input("Please The Password: "))
   if(user=="Thiru" and password1==9225):
         #try:
               print("Press Ctrl+C To Exit")
               while True:
                  speak("Hi i am JARVIS")
                  wishme()
                  #query = takecommand().lower()
                  while True:
                              
                              query =takecommand().lower()
                              if 'wikipedia' in query.lower():
                                 speak("Searching in wikipedia")
                                 query=query.replace("wikipedia","")#miran""
                                 result=wikipedia.summary(query, sentences=2, chars=0, auto_suggest=True, redirect=True)
                                 speak("According to wikipedia")
                                 speak(result)
                                 print(result)
                              #Wanted to update
                              elif 'open youtube' in query:
                                 speak("opening youtube sir")
                                 webbrowser.open_new("youtube.com")#it is the function to open in web browser
                                 time.sleep(5)
                                 speak("what do you want to search sir?")
                                 a=takecommand().lower()
                                 pi.moveTo(549,124)
                                 pi.typewrite(a,interval=0.25)
                                 time.sleep(1)
                                 speak("pressing enter sir")
                                 pi.press('enter')
                                 a=takecommand().lower()
                                 if 'close'in a:
                                    pi.click(1885,15)
                                    

                              elif 'open google' in query:
                                 speak("opening google sir")
                                 webbrowser.open_new("google.com")

                              elif 'open gmail' in query:
                                 speak("opening Gmail sir")
                                 webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

                              elif 'open vi' in query:
                                 speak("opening VI website sir")
                                 webbrowser.open_new("https://www.myvi.in/account/login") 
                              elif 'call luna'in query:
                                 changevoice(query)
                              elif 'call jarvis'in query:
                                 changevoice(query)
                              elif 'open ai' in query:
                                 speak("opening chat GPT sir")
                                 webbrowser.open_new("https://chat.openai.com/auth/login?next=%2Fchat")#it is the function to open in web browser

                              elif 'open nptel' in query:
                                 speak("opening swayam NPTEL PROGRAM sir")
                                 webbrowser.open("https://swayam.gov.in/")
                              

                              elif 'email to ' in query:
                                 try:
                                    speak("What should I say?")
                                    content = takeCommand()
                                    to = "YourfriendEmail@gmail.com"    
                                    sendEmail(to, content)
                                    speak("Email has been sent!")
                                 except Exception as e:
                                    print(e)
                                    speak("Sorry my friend. I am not able to send this email")

                              elif 'open drive' in query:
                                 speak("opening Google            Drive       sir")
                                 webbrowser.open_new("https://drive.google.com/drive/u/0/my-drive")
                                 
                              elif 'open amazon' in query:
                                 speak("opening Amazon sir")
                                 webbrowser.open("https://www.amazon.in/")

                              elif 'open iot' in query:
                                 speak("opening your tinkercad Website  sir")
                                 webbrowser.open("https://www.tinkercad.com/dashboard")
                              elif 'open code' in query:
                                 speak("opening VScode sir")
                                 codepath=("C:\\Users\\Thirumalaivasan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                                 os.startfile(codepath)

                              elif 'open chrome' in query:
                                 codepath1=("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                                 speak("opening google chrome sir")
                                 os.startfile(codepath1)
                                 speak("now the chrome is opened which mail id i want to select?")
                                 
                                 while True:
                                    qu= takecommand().lower()
                                    if 'first' in qu:
                                       pi.click(768,626,1,button="left")
                                    if 'second' in qu:#click on second mail
                                       pi.click(955,608,1,button="left")
                                    elif 'searching' in qu:
                                       speak("what do you want to search ?")
                                       a= takecommand().lower()
                                       pi.moveTo(684,484)
                                       pi.typewrite(a,interval=0.25)
                                       time.sleep(3)
                                       pi.press('enter')
                                    elif 'close'in qu:
                                       pi.click(1885,15)
                                       break


                              elif 'wi-fi' in query: 
                                 speak("The wifi you have connected is "+Wifi.get_wifi_name())
                                 
                              elif 'open word' in query:
                                 cp=("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                                 speak("opening MS Word sir")
                                 os.startfile(cp)
                                 
                              elif 'open edge' in query:
                                 codepath2=("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                                 speak("opening microsoft Edge sir")
                                 os.startfile(codepath2)

                              elif 'open powerpoint' in query:
                                 codepath3=("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                                 speak("opening powerpoint sir")
                                 os.startfile(codepath3)

                              elif 'open excel' in query:
                                 codepath4=("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                                 speak("opening MS excel sir")
                                 os.startfile(codepath4)

                              elif 'open onenote' in query:
                                 codepath5=("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")
                                 speak("opening OneNote sir")
                                 os.startfile(codepath5)

                              elif 'time' in query:
                                 time=datetime.datetime.now().strftime("%H Hours:%M Minutes:%S Seconds")#which returns the time in string
                                 speak("The Current Time Is")
                                 speak(time)
                              elif 'shutdown' in query:
                                 speak("I am going to shutdown your system sir ")
                                 pi.hotkey('win','x')
                                 pi.press('u')
                                 pi.press('u')

                              elif 'play music' in query:
                                 speak("Okay sir! now playing music")
                                 music_dir = 'C:\\Users\\Thirumalaivasan\\Music\\Hit Songs'
                                 songs = os.listdir(music_dir)#to create the list 
                                 print(songs)    
                                 os.startfile(os.path.join(music_dir, songs[0]))#path() function has path related functions,join handle the backslash when we not put as correct\to choose anyone song we can use the randam.
                                 a=takecommand().lower()
                                 if 'close'in a:
                                    pi.click(1885,15)
                           

                              elif'exit'  in query:
                                 speak("good bye sir i going to sleep sir!")
                                 check=takecommand().lower()
                                 if 'okay bye'or'okay' in check:
                                    speak("good bye sir!")
                                    quit()
                                    #pi.click(1880,18)#which has the close of current screen value
                                 elif "please" in check:
                                    speak("ok i will be there for you!..")
                                    continue
                              
         #except KeyboardInterrupt:
               #print('\n')   
                     
                           
            
   else:
      speak("Unauthorized access. Try Again Sir")
      print("Unauthorized access.")
