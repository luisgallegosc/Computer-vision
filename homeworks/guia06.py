import cv2
import numpy as np
from matplotlib import pyplot as plt

# Leer las dos imágenes
img1 = cv2.imread('vision computacional\homeworks\board1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('vision computacional\homeworks\board2.jpg', cv2.IMREAD_GRAYSCALE)

# Calcular la diferencia absoluta entre las dos imágenes
diferencia = cv2.absdiff(img1, img2)

# Aplicar umbral para resaltar las diferencias significativas
umbral = 30  # Puedes ajustar este valor según tus necesidades
_, umbral_dif = cv2.threshold(diferencia, umbral, 255, cv2.THRESH_BINARY)

# Encontrar los contornos de las diferencias
contornos, _ = cv2.findContours(umbral_dif, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en una copia de la segunda imagen (la imagen de destino)
resultado = img2.copy()
cv2.drawContours(resultado, contornos, -1, (0, 255, 0), 2)

# Mostrar las imágenes y resultados
plt.subplot(131), plt.imshow(img1, 'gray'), plt.title('Imagen 1')
plt.subplot(132), plt.imshow(img2, 'gray'), plt.title('Imagen 2')
plt.subplot(133), plt.imshow(resultado, 'gray'), plt.title('Diferencias Resaltadas')
plt.show(block=True)  # Mostrar la ventana y bloquear la ejecución hasta que se cierre

# Esperar una tecla antes de cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()