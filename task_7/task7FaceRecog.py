import cv2
import mediapipe as mp
import face_recognition as fr

cam=cv2.VideoCapture('./mrBean2.mp4')

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
faces=mp.solutions.face_detection.FaceDetection()

face=fr.load_image_file('./mrBean.png')
faceEncoding=fr.face_encodings(face)[0]

while True:
    _,frame=cam.read()
    if _:
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faceResults=faces.process(frameRGB)
        if faceResults.detections!=None:
            for face in faceResults.detections:
                bBox=face.location_data.relative_bounding_box
                x,y,w,h=int(bBox.xmin*width),int(bBox.ymin*height),int(bBox.width*width),int(bBox.height*height)
                face=frameRGB[y:y+h,x:x+w]
                if(face.shape[0]*face.shape[1])>0:
                    encoding=fr.face_encodings(face)
                    match=fr.compare_faces(encoding,faceEncoding)
                    if True in match:
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        cv2.putText(frame,'Mr Bean',(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Cam',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
