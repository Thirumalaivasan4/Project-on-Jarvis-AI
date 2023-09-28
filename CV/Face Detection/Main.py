import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
imagebackgroud=cv2.imread("resource\\back3.jpg")




while True:
    success,img=cap.read()
    imagebackgroud[162:162+480,55:55+640]=img
    cv2.imshow("Face Attendance",imagebackgroud)
    #cv2.imshow("Wedcam",img)
    cv2.waitKey(1)