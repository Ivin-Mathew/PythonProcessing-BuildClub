import cv2
import numpy as np

draw=False
reset=False
p1=(0,0)
p2=p1

def mouseClick(event,xPos,yPos,flags,param):
    #print(event,xPos,yPos,flags,param)
    global draw,reset,p1,p2

    if event==cv2.EVENT_LBUTTONDOWN:
        draw=True
        reset=False
        p1=(xPos,yPos)
        p2=p1

    if event==cv2.EVENT_MOUSEMOVE & draw:
        p2=(xPos,yPos)
    
    if event==cv2.EVENT_LBUTTONUP:
        draw=False
    
    if event==cv2.EVENT_RBUTTONDOWN:
        reset=True
        p1=(0,0)
        p2=p1

frame=np.zeros((500,500,3),np.uint8)
cv2.namedWindow("Frame")
cv2.setMouseCallback('Frame',mouseClick)

while True:

    if draw:
        cv2.line(frame,p1,p2,(0,255,0),2)
        p1 = p2
    
    cv2.imshow('Frame',frame)

    if reset:
        frame = np.zeros((500,500,3), np.uint8)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()