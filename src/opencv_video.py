import cv2
import numpy
video=cv2.VideoCapture("/Users/liquanyan/PycharmProjects/YOLOTrain/video/video.mp4")
if video.isOpened() is False:
    print("video is not opened")
    exit()
ret,frame=video.read()
while ret:
    if not ret:
        break
    # 将彩色视频转换为灰度视频,为啥我这里没有转换
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video_color",frame)
    cv2.imshow("video_gray",gray)
    if cv2.waitKey(1)==ord("q"):
        print("success exit")
        break


