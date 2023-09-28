import cv2
import time
trained=cv2.CascadeClassifier("C:\\Users\\Thirumalaivasan\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
ptime=1
currenttime=1
while True:
    workingcorrectly,image=webcam.read()
    blackandwhite=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#to change the color as blackandwhite because our AI supports only thia color
    

    face=trained.detectMultiScale(blackandwhite)#this is for face detection
    
    for(x,y,w,h) in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),5)
        
        fps="This ELOM MUSK "
        fps1="CEO of Tesla Motors."
        cv2.putText(image,f'INFO:{fps}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
        cv2.putText(image,f'FROM:{fps1}',(60,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)

    cv2.imshow("Face Detection",image)#To display the image
    currenttime=time.time()
    fps=1/(currenttime-ptime)
    ptime=currenttime
    #cv2.putText(image,f'FPS: {fps}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
    #cv2.putText(image,f'FPS: {fps1}',(50,60),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
    cv2.waitKey(1)#no key press