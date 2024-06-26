import cv2

image=cv2.imread("./ball.png")
edges=cv2.Canny(image,200,300)

contours,heirarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
contoured=image.copy()

cv2.drawContours(contoured,contours,-1,(0,255,0),3)

cv2.imshow("original",image)
cv2.imshow("edges drawn",contoured)

cv2.waitKey()
cv2.destroyAllWindows()