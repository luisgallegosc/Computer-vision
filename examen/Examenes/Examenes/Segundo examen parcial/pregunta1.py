import cv2
import matplotlib.pyplot as plt
import numpy as np

#leer la imagen
imagen = cv2.imread('Cambiar-rueda.png')

#Convertir imagenes e escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#detectamos bordes
#aplicamos Canny
canny = cv2.Canny(imagen_gris, 70, 120)
cv2.imshow('Bordes de la imagen mediante Canny', canny)
#contar las líneas encontradas y dibujarlas de color azul
#nos devuelve un vector con las lineas que encontro
imagen_copy = imagen.copy()
lines = cv2.HoughLinesP(canny, 1, np.pi/180, 100, minLineLength=60, maxLineGap=4)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(imagen_copy, (x1,y1), (x2,y2), (255,0,0), 2, cv2.LINE_AA)

cv2.imshow('Bordes de Iamgen', imagen_copy)

# aplicamos los filtros para eliminar el ruido
imagen_copy2 = imagen.copy()
img_con_filtro = cv2.medianBlur(imagen_gris, 5)
# Obtener los circulos probando parametros
circulos = cv2.HoughCircles(img_con_filtro, cv2.HOUGH_GRADIENT, 1.2, 250  )
circulos = np.uint16(np.around(circulos))
for i in circulos[0,:]:
    # dibujar circulo 
    cv2.circle(imagen_copy2, (i[0], i[1]), i[2], (0,0,255), 2)
    # dibujar centro
    cv2.circle(imagen_copy2, (i[0], i[1]), 2, (0,255,255), 30)
cv2.imshow('Imagenes con circulos', imagen_copy2)

cv2.waitKey(0)
cv2.destroyAllWindows()