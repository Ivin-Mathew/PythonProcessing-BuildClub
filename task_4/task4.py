import cv2
import numpy as np

draw=False
p1=(0,0)
p2=p1

def mouseClick(event,xPos,yPos,flags,param):
    #print(event,xPos,yPos,flags,param)
    global draw,p1,p2
    if event==cv2.EVENT_LBUTTONDOWN:
        draw=True
        p1=(xPos,yPos)

    if event==cv2.EVENT_MOUSEMOVE & draw:
        p2=(xPos,yPos)
    
    if event==cv2.EVENT_LBUTTONUP:
        draw=False



cv2.namedWindow("Frame")

cv2.setMouseCallback('Frame',mouseClick)

while True:
    frame=np.zeros((500,500,3),np.uint8)
    cv2.rectangle(frame,p1,p2,(0,255,0),2)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()