import cv2

cam=cv2.VideoCapture(1)

""" width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cam.get(cv2.CAP_PROP_FPS)

print("Resolution=",width,"x",height)
print("FPS=",fps)
 """

cam.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
cam.set(cv2.CAP_PROP_FPS,60)

width=cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cam.get(cv2.CAP_PROP_FPS)

print("Resolution=",width,"x",height)
print("FPS=",fps)

output_file = './recording.MP4'
output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(width), int(height)))


while True:
    _,frame= cam.read()
    cv2.imshow("Webcam", frame)
    output.write(frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cam.release()
output.release()
cv2.destroyAllWindows()