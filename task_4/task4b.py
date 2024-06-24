import cv2
import numpy as np

R = 0
G = 0
B = 0

def redValue(value):
    global R
    R = value
def greenValue(value):
    global G 
    G = value
def blueValue(value):
    global B 
    B = value

frame = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('FRAME')

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',500,130)

cv2.createTrackbar('RED','Trackbars',R,255,redValue)
cv2.createTrackbar('GREEN','Trackbars',G,255,greenValue)
cv2.createTrackbar('BLUE','Trackbars',B,255,blueValue)

while True:
    frame[:,:,2] = R
    frame[:,:,1] = G
    frame[:,:,0] = B
    cv2.imshow('FRAME',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()