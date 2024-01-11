import numpy as np
import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread('../images/board.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 500, 0.05, 10)
 
# El resultado devuelto es una matriz de [[311., 250.]] dos niveles de paréntesis.
corners = np.int0(corners)
 
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)
 
plt.imshow(img), plt.title('Destino'), plt.axis('off')
plt.show()