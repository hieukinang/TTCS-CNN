import cv2
import mediapipe
import time

cap=cv2.VideoCapture("Video/soiguong.mp4")
pTimes=0
while True:
    success, img= cap.read()

    cTimes=time.time()
    fps=1/(cTimes-pTimes)
    pTimes= cTimes
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,10,10),2)
    cv2.imshow("Image",img)
    cv2.waitKey(20)