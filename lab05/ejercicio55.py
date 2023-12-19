import cv2
import numpy as np
import math
#--leer la imagen
src = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\lena.jpg")
#--obtener dimensiones
rows, cols = src.shape[:2]
print(rows, cols)
#--obtener las tangentes en ambos ejes
ix = math.tan(20 * math.pi / 180)
iy = math.tan(15 * math.pi / 180)
#--obtener la matriz de transformación
M = np.float32([[1, ix, 0], [iy, 1, 0]])
#--ejecutar la trasnformación
dst = cv2.warpAffine(src, M, (cols + 256, rows + 256))
#--mostrar las imágenes
cv2.imshow('lena.jpg', src)
cv2.imshow('Inclinar', dst)
cv2.waitKey()