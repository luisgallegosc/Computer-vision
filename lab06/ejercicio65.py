import cv2
import numpy as np
#--leer la imagen
img = cv2.imread('C:/Users/benito/OneDrive/Escritorio/UNSAAC/8vo/vision computacional/lab06/A.png', 0)#--elemento estructurante
#kernel = np.ones((7,7),np.uint8)
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

dilatacion = cv2.dilate(img,kernel,iterations = 1)
#--mostrar resultados
cv2.imshow("original", img)
cv2.imshow("erosion", dilatacion)

cv2.waitKey()
