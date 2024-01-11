import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('../images/board.png',0)
# Inicializar el objeto FAST con valores predeterminados
fast = cv.FastFeatureDetector_create()
 # Encuentra y dibuja puntos clave
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
 # Imprime todos los parámetros predeterminados
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
cv.imwrite('fast_true.png',img2)
 # Desactivar la supresión no máxima
fast.setNonmaxSuppression(0)
kp = fast.detect(img,None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
cv.imwrite('fast_false.png',img3)
 