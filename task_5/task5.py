import cv2
import numpy as np

def onTrack1(val):
    global hueLow
    hueLow=val

def onTrack2(val):
    global hueHigh
    hueHigh=val

def onTrack3(val):
    global satLow
    satLow=val

def onTrack4(val):
    global satHigh
    satHigh=val

def onTrack5(val):
    global valLow
    valLow=val

def onTrack6(val):
    global valHigh
    valHigh=val

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",400,300)

hueHigh,hueLow=0,0
satHigh,satLow=0,0
valHigh,valLow=0,0

cv2.createTrackbar('Hue Low','Trackbars',110,179,onTrack1)
cv2.createTrackbar('Hue High','Trackbars',150,179,onTrack2)

cv2.createTrackbar('Saturaion Low','Trackbars',80,255,onTrack3)
cv2.createTrackbar('Saturation High','Trackbars',255,255,onTrack4)

cv2.createTrackbar('Value Low','Trackbars',134,255,onTrack5)
cv2.createTrackbar('Value High','Trackbars',255,255,onTrack6)

image=cv2.imread("./ball.png")

while True:
    frameHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow,satLow,valLow])
    upperBound = np.array([hueHigh,satHigh,valHigh])
    
    mask = cv2.inRange(frameHSV,lowerBound,upperBound)
    masked = cv2.bitwise_and(image,image,mask=mask)

    cv2.imshow('mask',mask)
    cv2.imshow('Ball',image)
    cv2.imshow('masked',masked)

    print('Lowerbound = ',lowerBound)
    print('Upperbound = ',upperBound)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()

