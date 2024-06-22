import cv2

image=cv2.imread("./rdj.jpg")
image0=cv2.imread("./tom.jpg")

image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_gray2=cv2.cvtColor(image0,cv2.COLOR_BGR2GRAY)

image1=cv2.cvtColor(image_gray,cv2.COLOR_GRAY2BGR)
image2=cv2.cvtColor(image_gray2,cv2.COLOR_GRAY2BGR)

row1=cv2.hconcat([image,image0])
row2=cv2.hconcat([image1,image2])

combined=cv2.vconcat([row1,row2])

cv2.namedWindow("Assignment 1 output",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Assignment 1 output",500,500)
cv2.imshow("Assignment 1 output",combined)
result=cv2.imwrite("./result.jpg",combined)

cv2.waitKey()
cv2.destroyAllWindows()
