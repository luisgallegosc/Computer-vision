import cv2
import matplotlib.pyplot as plt
#--leer la imagen
img= cv2.imread('../images/sunflower.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('grayscale image', img)
#--calcular histograma y mostrar
#--El eje X del histograma de la imagen tendrá un rango de 0-255 
#--y el eje Y rastrea el recuento de píxeles contra cada intensidad.
ax = plt.hist(img.ravel(), bins = 256)
plt.show()
#--esperar
cv2.waitKey(0)
cv2.destroyAllWindows()