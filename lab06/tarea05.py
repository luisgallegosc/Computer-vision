import numpy as np
import cv2
import imutils
image = cv2.imread('imagenes/cat.png')
cv2.imshow("Original", image)
shifted = imutils.translate(image, -120, 0)
cv2.imshow("Movida", shifted)
rotated = imutils.rotate(image, angle=45)
cv2.imshow("Original", image)
cv2.imshow("Rotada", rotated)
cv2.waitKey(0)