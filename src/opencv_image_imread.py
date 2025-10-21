import cv2 as cv
# imread的三种参数
# 第一个参数:图片路径
# 第二个参数:1代表彩色图片,0代表灰度图片,-1代表带透明度的图片
# 使用绝对路径
image_color=cv.imread("/Users/liquanyan/PycharmProjects/YOLOTrain/image/img.png",1)
image_gray=cv.imread("/Users/liquanyan/PycharmProjects/YOLOTrain/image/img.png",0)
image_alpha=cv.imread("/Users/liquanyan/PycharmProjects/YOLOTrain/image/img.png",-1)
if image_color is None:
    print("image_color is None")
    exit()
if image_gray is None:
    print("image_gray is None")
    exit()
if image_alpha is None:
    print("image_alpha is None")
    exit()
# 显示图片
# 第一个参数:窗口名称
# 第二个参数:图片cv.imread的返回值
cv.imshow("image_color",image_color)
cv.imshow("image_gray",image_gray)
cv.imshow("image_alpha",image_alpha)
# 等待按键,0代表一直等待,下面表示按下q键退出
if cv.waitKey(0)==ord("q"):
    print("success exit")
# 关闭客户端
cv.destroyAllWindows()


