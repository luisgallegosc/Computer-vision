import cv2
import numpy as np

img = cv2.imread('../images/waffle.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print(dst.shape)
height, width = dst.shape
color = (0, 255, 0)

for y in range(0, height):
    for x in range(0, width):
        if dst.item(y, x) > 0.1 * dst.max():
            cv2.circle(img, (x, y), 3, color, cv2.FILLED, cv2.LINE_AA)

cv2.imshow('Harris Result', dst)
cv2.imshow('Harris Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()