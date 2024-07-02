import cv2

image=cv2.imread("./rdj.jpg")
print("Image array dimension: ",image.shape)

newImage=image[:400,:400]
c=0
while True:
    for i in range(0,400,100):
        for j in range(0,400,100):
            if c%2==0:
                newImage[i:i+100,j:j+100]=(0,0,0)
            else:
                newImage[i:i+100,j:j+100]=(255,255,255)
            c=c+1
        c=c+1
    cv2.imshow("Image",newImage)
    if cv2.waitKey(1000) & 0xff==ord('q'):
        break
    c=c+1

cv2.destroyAllWindows()