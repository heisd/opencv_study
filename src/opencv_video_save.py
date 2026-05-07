import os
import cv2

video_path = os.path.join(os.path.dirname(__file__), '..', 'video', 'video.mp4')
output_path = os.path.join(os.path.dirname(__file__), '..', 'video', 'saved_video.avi')

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("视频文件打开失败")
    exit()

# 获取视频的宽高
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"分辨率：{width} x {height}")

# FourCC 是指定视频编解码器的 4 字节代码，XVID 是常用的 AVI 编码格式
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# 参数：输出路径，编解码器，帧率，分辨率
saved_video = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
if not saved_video.isOpened():
    print("视频写入器初始化失败")
    cap.release()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("video", frame)
    saved_video.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
saved_video.release()
cv2.destroyAllWindows()
print(f"视频已保存至：{output_path}")
