import cv2
import numpy as np

# Leer la imagen
imagen_original = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\lena.jpg")

# Realizar zoom en la imagen manteniendo el tamaño original
factor_escala_zoom = 1.5
imagen_zoom = cv2.resize(imagen_original, None, fx=factor_escala_zoom, fy=factor_escala_zoom)

# Rotar la imagen 45 grados
angulo_rotacion = 45
filas, columnas = imagen_zoom.shape[:2]
centro = (columnas // 2, filas // 2)
matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1)
imagen_rotada = cv2.warpAffine(imagen_zoom, matriz_rotacion, (columnas, filas))

# Voltear verticalmente la imagen (inversión hacia abajo)
imagen_invertida = cv2.flip(imagen_rotada, 0)

# Mostrar las imágenes
cv2.imshow("Imagen Original", imagen_original)
cv2.imshow("Imagen con Zoom", imagen_zoom)
cv2.imshow("Imagen Rotada", imagen_rotada)
cv2.imshow("Imagen Invertida", imagen_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()
