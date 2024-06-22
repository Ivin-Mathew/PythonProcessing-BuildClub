import cv2
path="./rdj.jpg"

image=cv2.imread(path)
image2=cv2.imread("./tom.jpg")
""" cv2.imshow("Output",image) """

image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Output1",image_gray)

image_gray2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
cv2.imshow("Output2",image_gray2)

cv2.imwrite("./rdj_gray.jpg",image_gray)
cv2.imwrite("./tom_gray.jpg",image_gray2)

cv2.waitKey()
cv2.destroyAllWindows()
