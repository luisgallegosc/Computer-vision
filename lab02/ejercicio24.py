import cv2 as cv
import numpy as np

imagen = cv.imread("../images/lion.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", imagen)

B, G, R = cv.split (imagen) # separación de canales
cv.imshow("blue", B)
cv.imshow("green", G)
cv.imshow("red", R)

zeros = np.zeros(imagen.shape[:2], dtype = "uint8")
cv.imshow("Red", cv.merge([zeros, zeros, R]))
cv.imshow("Green", cv.merge([zeros, G, zeros]))
cv.imshow("Blue", cv.merge([B, zeros, zeros]))
cv.waitKey(0)

# mezclar nuevamente los canales
imagen = cv.merge ([B, G, R]) # Combinación de canales
cv.imshow("imagen mezclada", imagen)

cv.waitKey(0)
cv.destroyAllWindows()
