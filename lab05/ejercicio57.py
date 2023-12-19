import math
import numpy as np
import cv2
#--leer la imagen
src = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\left.jpg")
#--obtener dimensiones
rows, cols = src.shape[:2]

#--definir los 4 puntos en la imagen original
pts1 = np.float32([[113, 137], [256, 136], [270, 337], [140, 377]])
#--definir los 4 puntos en la imagen de salida
pts2 = np.float32([[0, 0], [165, 0], [165, 223], [0, 223]])

#--obtener la matriz de transformación
M = cv2.getPerspectiveTransform(pts1, pts2)

#--ejecutar la transformación
dst = cv2.warpPerspective(src, M, (165, 223))
#--mostrar las imágenes
cv2.imshow('Imagen con perspectiva', src)
cv2.imshow('Transform.', dst)
cv2.waitKey()