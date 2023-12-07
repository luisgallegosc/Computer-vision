import cv2
import numpy as np
import matplotlib.pyplot as plt
#--leer la imagen
img= cv2.imread('../images/dark_image1.png', 0)
cv2.imshow('Imagen original', img)

#--obtener el histograma de la imagen original
ax = plt.hist(img.ravel(), bins= 256)
plt.title('Histograma de la imagen original')
plt.show()

#--aplicando la ecualización
histequ = cv2.equalizeHist(img)
#--muestra la imagen ecualizada
cv2.imshow('Histograma de la imagen ecualizada', histequ)
#--obtiene el histograma de la imagen ecualizada
ax = plt.hist(histequ.ravel(), bins= 256)
plt.title('Histogram of Histogram Equalized Image')
plt.show()

img_with_histequ = np.hstack((img,histequ))
cv2.imshow('Comparison', img_with_histequ)
cv2.waitKey(0)
cv2.destroyAllWindows()
