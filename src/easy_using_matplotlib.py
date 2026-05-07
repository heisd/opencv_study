import os
import cv2
from matplotlib import pyplot as plt

img_path = os.path.join(os.path.dirname(__file__), '..', 'image', 'img.png')

# OpenCV 以 BGR 格式读取图片，matplotlib 使用 RGB，需要转换
image_bgr = cv2.imread(img_path, 1)
if image_bgr is None:
    print("图片读取失败")
    exit()

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# 使用 matplotlib 展示图片
plt.imshow(image_rgb)
# 隐藏坐标轴刻度
plt.xticks([])
plt.yticks([])
plt.title("使用 Matplotlib 展示图片")
plt.show()
