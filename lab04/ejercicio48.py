# import Opencv
import cv2
  
# import Numpy
import numpy as np
  
# leer la imagen
img = cv2.imread('../images/calle_oscura.png', 0)
cv2.imshow('original', img)  
# ecualizar la imagen
equ = cv2.equalizeHist(img)
   
# show image input vs output
cv2.imshow('imagen ecualizada', equ)
  
cv2.waitKey(0)
cv2.destroyAllWindows()