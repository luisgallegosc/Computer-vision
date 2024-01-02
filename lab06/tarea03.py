import cv2
import numpy as np
img= cv2.imread("../images/lena_ruido.jpg",1)
filtro_media = np.ones((31, 31), np.float32) / 961
imagen_filtrada = cv2.filter2D(img, -1, filtro_media)
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen Filtrada', imagen_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()