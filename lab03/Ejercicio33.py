import cv2
import numpy as np
# cargar las imágenes
img1 = cv2.imread("../images/Fig1_a.jpg")
img2 = cv2.imread("../images/lion.jpg")
cv2.imshow("ima1",img1)
cv2.imshow("ima2",img2)

# Realización de difuminado promedio de la primera imagen
# Filters - left (3,3), middle(5,5), right(9,9)
blurred_1 = np.hstack([
  cv2.blur(img1,(3,3)),
  cv2.blur(img1,(5,5)),
  cv2.blur(img1,(9,9))])  
cv2.imshow("blurred",blurred_1)
# Realización de difuminado promedio de la segunda imagen
# Filters - left (3,3), middle(5,5), right(9,9)
blurred_2 = np.hstack([
  cv2.blur(img2,(3,3)),
  cv2.blur(img2,(5,5)),
  cv2.blur(img2,(9,9))])  
cv2.imshow("blurred2",blurred_2)

cv2.waitKey(0)
