import cv2
import numpy as np
#--leer la imagen
img = cv2.imread('C:/Users/benito/OneDrive/Escritorio/UNSAAC/8vo/vision computacional/lab06/A_noise2.png', 0)#--elemento estructurante
#--elemento estructurante
#kernel = np.ones((7,7),np.uint8)
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#--realizar el cierre

cierre = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#--mostrar resultados
cv2.imshow("original", img)
cv2.imshow("cierre", cierre)

cv2.waitKey()

