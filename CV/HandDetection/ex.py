import mediapipe as mp
import cv2
import time
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
while True:
    
    success,img=cap.read()
    img=cv2.flip(img,1)
 
    cv2.imshow("Wedcam",img)
    cv2.waitKey(1)