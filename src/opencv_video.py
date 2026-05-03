import os
import cv2

video_path = os.path.join(os.path.dirname(__file__), '..', 'video', 'video.mp4')

video = cv2.VideoCapture(video_path)
if not video.isOpened():
    print("视频文件打开失败")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        break
    # 将彩色帧转换为灰度帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("video_color", frame)
    cv2.imshow("video_gray", gray)
    if cv2.waitKey(1) == ord("q"):
        print("退出成功")
        break

video.release()
cv2.destroyAllWindows()
