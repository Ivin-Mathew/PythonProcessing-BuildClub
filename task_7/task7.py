import cv2
import mediapipe as mp

cam=cv2.VideoCapture("./mrBean2.mp4")

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

faces=mp.solutions.face_detection.FaceDetection()
while True:
    _,frame=cam.read()
    if _:
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faceResults=faces.process(frameRGB)
        if faceResults.detections!=None:
            for face in faceResults.detections:
                bBox=face.location_data.relative_bounding_box
                x,y,w,h=int(bBox.xmin*width),int(bBox.ymin*height),int(bBox.width*width),int(bBox.height*height)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imshow('Webcam',frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()