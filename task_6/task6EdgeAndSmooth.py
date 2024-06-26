import cv2

image=cv2.imread('./ball.png')

median=cv2.medianBlur(image,7)
gaussian=cv2.GaussianBlur(image,(7,7),cv2.BORDER_DEFAULT)

edges=cv2.Canny(image,200,300)#image, minIntensity, maxIntensity

cv2.imshow("Original",image)
cv2.imshow("Edges",edges)
cv2.imshow("Median blur",median)
cv2.imshow("Gaussian blur",gaussian)


cv2.waitKey()
cv2.destroyAllWindows()