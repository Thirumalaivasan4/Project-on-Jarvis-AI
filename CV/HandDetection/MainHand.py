import cv2
import time
cap=cv2.VideoCapture(0)
##########################
wCam,hCam=640,480
ptime=0
##########################
cap.set(3,wCam)
cap.set(4,hCam)




while True:

    success,img=cap.read()
    currenttime=time.time()
    fps=1/(currenttime-ptime)
    ptime=currenttime
    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
    cv2.imshow("Wedcam",img)
    cv2.waitKey(1)