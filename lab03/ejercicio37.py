import cv2
import numpy as np
# cargar las imágenes
img1 = cv2.imread("../images/cat.png",1)
# Creando un filtro de enfoque
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# Aplicando la función cv2.filter2D en la imagen
sharpen_img_1=cv2.filter2D(img1,-1,filter)
cv2.imshow("gato original",img1)
cv2.imshow("gato enfocado",sharpen_img_1)

img2 = cv2.imread("../images/lena.jpg",1)
# Creando un filtro de nitidez
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# Aplicando la función cv2.filter2D en la imagen
sharpen_img_2=cv2.filter2D(img2,-1,filter)
cv2.imshow("lena original",img2)
cv2.imshow("lena enfocado",sharpen_img_2)

cv2.waitKey(0)
