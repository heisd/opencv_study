import cv2
# 调用本机摄像头
capture=cv2.VideoCapture(0)
if capture.isOpened() is False:
    print("capture is not opened")
    exit()
else:
    print("capture is opened")
    # 显示摄像头画面
    while True:
        ret,frame=capture.read()
        # 将彩色视频转换为灰度视频
        # frame是彩色视频
        # gray是灰度视频
        # COLOR_BGR2GRAY是转换方式
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("camera",frame)
        # 等待按键q按下
        if cv2.waitKey(1)==ord("q"):
            print("success exit")
            # 释放摄像头
            capture.release()
            cv2.destroyAllWindows()
            break


