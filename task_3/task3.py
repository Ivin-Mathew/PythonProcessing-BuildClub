import cv2
import numpy as np

line = np.zeros((300,300,3),dtype=np.uint8)
arrow = line.copy()
polyLine = line.copy()
rectangle = line.copy()
circle = line.copy()
text = line.copy()

p1 = [100,100]
p2 = [200,200]
p3 = [200,100]
p4 = [100,200]
points = np.array([p1,p2,p3,p4]) 

cv2.line(line,p1,p2,(0,255,0),2)
cv2.arrowedLine(arrow,p1,p2,(0,255,0),2)
cv2.polylines(polyLine,[points],False,(0,255,0),2)
cv2.rectangle(rectangle,p1,p2,(0,255,0),2)
cv2.circle(circle,(150,150),50,(0,255,0),2)
cv2.putText(text,'sample_text', p4, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
(0,255,0))

cv2.imshow('line',line)
cv2.imshow('arrow',arrow)
cv2.imshow('polyLine',polyLine)
cv2.imshow('rectangle',rectangle)
cv2.imshow('circle',circle)
cv2.imshow('text',text)

cv2.waitKey()
cv2.destroyAllWindows() 