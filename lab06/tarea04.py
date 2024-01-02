import cv2
import numpy as np
from matplotlib import pyplot as plt
imagen = cv2.imread('imagenes/ave.jpg')
cv2.imshow('Fwen.jpg', imagen)
imagen_red= imagen[:, :, 2]
plt.hist(imagen_red.ravel(), bins = 256, color = 'Red', alpha = 0.5)
imagen_green= imagen[:, :, 1]
plt.hist(imagen_green.ravel(), bins = 256, color = 'Green', alpha =
0.5)
imagen_blue= imagen[:, :, 0]
plt.hist(imagen_blue.ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.show()
img_red_equ = cv2.equalizeHist(imagen_red)
img_green_equ = cv2.equalizeHist(imagen_green)
img_blue_equ = cv2.equalizeHist(imagen_blue)
image_ecualizada = cv2.merge ([img_blue_equ,img_green_equ,img_red_equ])
cv2.imshow('imagen ecualizada', image_ecualizada)
im1= image_ecualizada[:, :, 2]
plt.hist(im1.ravel(), bins = 256, color = 'Red', alpha = 0.5)
im2= image_ecualizada[:, :, 1]
plt.hist(im2.ravel(), bins = 256, color = 'Green', alpha = 0.5)
im3= image_ecualizada[:, :, 0]
plt.hist(im3.ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.show()