import cv2

# 调用本机摄像头（设备索引 0）
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("摄像头打开失败")
    exit()

print("摄像头已打开")
while True:
    ret, frame = capture.read()
    if not ret:
        break
    # 将彩色帧转换为灰度帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera", frame)
    # 按下 q 键退出
    if cv2.waitKey(1) == ord("q"):
        print("退出成功")
        break

capture.release()
cv2.destroyAllWindows()
