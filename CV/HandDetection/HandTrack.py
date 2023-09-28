import mediapipe as mp
#import mediapipe.python.solutions.drawing_utils as du
#import mediapipe.python.solutions.hands as h
import cv2
import time
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=5, trackCon=5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    # Rest of your class methods


    def findHandes(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)  # Use self.hands to access the attribute
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    

    '''for id,lm in enumerate(handLms.landmark):
                    #print(id,lm)
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    print(id,cx,cy)
                    if id==4:
                        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)'''
            



def main():
    ptime=0
    currenttime=0
    cap=cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success,img=cap.read()
        #img=cv2.flip(img,1)
        img=detector.findHandes(img)
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        currenttime=time.time()
        fps=1/(currenttime-ptime)
        ptime=currenttime
        cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0,5),3)
        cv2.imshow("Wedcam",img)
        cv2.waitKey(1)
    









if __name__=="__main__":
    main()