import cv2

image=cv2.imread('./ball.png')
size=image.shape
height = int(size[1]/2) 
width = int(size[0]/2)

resized=cv2.resize(image,(height,width))
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
M=cv2.getRotationMatrix2D((width,height),45,1)
skewed=cv2.warpAffine(image,M,(400,400))

""" cv2.imshow("Image",image)
cv2.imshow("Resized Image",resized)
cv2.imshow("Rotated",rotated) """
cv2.imshow("Skewed",skewed)

cv2.waitKey()
cv2.destroyAllWindows()