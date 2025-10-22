import cv2
import numpy as np
cap=cv2.VideoCapture("/Users/liquanyan/PycharmProjects/YOLOTrain/video/video.mp4")
# fourcc是four character code
# FourCC是用于指定视频编解码器的4字节代码。可用代码列表
# *"XVID"是保存视频的格式
fourcc=cv2.VideoWriter_fourcc(*"XVID")
if not cap.isOpened():
    print("video is not opened")
    exit()
# 获取视频的分辩率
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 720 *1280的视频宽度和高度
print(width,height)
# 保存视频
# 参数:保存视频的路径,保存视频的格式,保存视频的帧率,保存视频的分辨率
saved_video=cv2.VideoWriter("/Users/liquanyan/PycharmProjects/YOLOTrain/saved_video",fourcc,20.0,(width,height))
if not saved_video.isOpened():
    print("saved_video is not opened")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow("video",frame)
    # 写入帧率进入视频文件
    saved_video.write(frame)
    if cv2.waitKey(1)==ord("q"):
        break
# 释放资源
cap.release()
saved_video.release()
cv2.destroyAllWindows()

