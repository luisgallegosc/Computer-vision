import cv2
import numpy as np
#--leer la imagen
img = cv2.imread('C:/Users/benito/OneDrive/Escritorio/UNSAAC/8vo/vision computacional/lab06/A_noise1.png', 0)#--elemento estructurante
#kernel = np.ones((7,7),np.uint8)
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#--realizar la apertura
apertura = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#--mostrar resultados
cv2.imshow("original", img)
cv2.imshow("apertura", apertura)

cv2.waitKey()
