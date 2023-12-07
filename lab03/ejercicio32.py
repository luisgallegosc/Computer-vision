import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#--leer la imagen
img = cv.imread('../images/Fig1_a.jpg')
#--eliminar el ruido
dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
#--mostrara imágenes
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()
