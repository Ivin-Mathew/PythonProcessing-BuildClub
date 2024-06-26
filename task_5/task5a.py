import cv2
import numpy as np

cam=cv2.VideoCapture('./ball.wmv')

while True:
    _,frame=cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound=np.array([110,80,134])
    upperBound=np.array([150,255,255])

    mask=cv2.inRange(frameHSV,lowerBound,upperBound)

    ballContours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for ballContour in ballContours:
        area=cv2.contourArea(ballContour)
        if area>500:
            x,y,w,h=cv2.boundingRect(ballContour)
            cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),2)
        cv2.imshow('mask',mask)
        cv2.imshow('Ball',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


cam.release()
cv2.destroyAllWindows()