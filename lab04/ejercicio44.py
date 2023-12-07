import cv2
import numpy as np
from matplotlib import pyplot as plt

#--leer la imagen
img = cv2.imread('../images/lena.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('lena.jpg', img)
#--determinar el histograma
hist = cv2.calcHist([img], [0], None, [256], [0, 255])
#--plotear el histograma
plt.plot(hist, color='gray' )
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()
