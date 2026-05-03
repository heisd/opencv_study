import cv2
import numpy as np

# 创建一个 512x512 的黑色画布
image = np.zeros((512, 512, 3), dtype=np.uint8)

# 画一条直线：起点(0,0)，终点(255,255)，颜色蓝色(BGR)，线宽5
cv2.line(image, (0, 0), (255, 255), (255, 0, 0), 5)

# 画一个矩形：左上角(100,100)，右下角(400,400)，颜色绿色，线宽2
cv2.rectangle(image, (100, 100), (400, 400), (0, 255, 0), 2)

# 画一个圆形：圆心(256,256)，半径80，颜色红色，线宽3
cv2.circle(image, (256, 256), 80, (0, 0, 255), 3)

cv2.imshow("draw", image)
if cv2.waitKey(0) == ord("q"):
    print("success exit")
cv2.destroyAllWindows()
