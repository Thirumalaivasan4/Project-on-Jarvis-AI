import mediapipe as mp
#import mediapipe.python.solutions.drawing_utils as du
#import mediapipe.python.solutions.hands as h
import cv2
import time
ptime=0
currenttime=0
cap=cv2.VideoCapture(0)
#hands=h.Hands()
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
while True:
    
    success,img=cap.read()
    img=cv2.flip(img,1)
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id==4 :
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    currenttime=time.time()
    fps=1/(currenttime-ptime)
    ptime=currenttime
    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
    cv2.imshow("Wedcam",img)
    cv2.waitKey(1)