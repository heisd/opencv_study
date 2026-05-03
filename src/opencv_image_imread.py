import os
import cv2 as cv

img_path = os.path.join(os.path.dirname(__file__), '..', 'image', 'img.png')

# imread flags: 1=color, 0=grayscale, -1=with alpha channel
image_color = cv.imread(img_path, 1)
image_gray = cv.imread(img_path, 0)
image_alpha = cv.imread(img_path, -1)

if image_color is None:
    print("image_color is None")
    exit()
if image_gray is None:
    print("image_gray is None")
    exit()
if image_alpha is None:
    print("image_alpha is None")
    exit()

cv.imshow("image_color", image_color)
cv.imshow("image_gray", image_gray)
cv.imshow("image_alpha", image_alpha)

if cv.waitKey(0) == ord("q"):
    print("success exit")
cv.destroyAllWindows()
