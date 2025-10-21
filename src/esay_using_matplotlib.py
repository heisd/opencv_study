# 导入头文件
import cv2
import numpy as np
from matplotlib import pyplot as plt
image=cv2.imread("/Users/liquanyan/PycharmProjects/YOLOTrain/image/img.png",1)
# cmap是重映射成灰色
# interpolation是插值
# bicubic是三次样条插值
plt.imshow(image,cmap='gray',interpolation='bicubic')
# xticks是x轴刻度
# yticks是y轴刻度
plt.xticks([])
plt.yticks([])
# 显示图片
plt.show()
if cv2.waitKey(0)==ord("q"):
    print("success exit")
cv2.destroyAllWindows()