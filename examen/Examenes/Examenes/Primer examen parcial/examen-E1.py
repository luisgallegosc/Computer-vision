import cv2
import matplotlib.pyplot as plt
import numpy as np

# -- Leer la imagen
imgenInicial = cv2.imread("images/Fig1_a.jpg")
cv2.imshow('imagen inicial', imgenInicial)

# -- Aplicar el filtro de mediana
imagenConFiltMediana = cv2.medianBlur(imgenInicial,5)
#mostrando la imagen sin ruido como la salida en la pantalla
cv2.imshow('imagen con filtro mediana', imagenConFiltMediana)
# de entre todos los filtros que se probo resulto ser el que mejor se
# acercaba al resultado requerido

# -- Aplicando Cuantizacion 
# --------------------------
# Obtener alto y ancho de la imagen
height = imgenInicial.shape[0]
width = imgenInicial.shape[1]
#Crear una imagen
imagenCuantificada = np.zeros((height, width, 3), np.uint8)

# Operación de cuantización de la imagen.
# el nivel de cuantización es 2
for i in range(height):
    for j in range(width):
        for k in range(3): #Corresponding to BGR three components
            if imgenInicial[i, j][k] < 190:
                gray = 0
            else:
                gray = 255
            imagenCuantificada[i, j][k] = np.uint8(gray)
cv2.imshow("imagen cuantizada", imagenCuantificada)
# Al aplicar cuantizacion obtenemos un resultado mas parecido al
# que se requiere

# -- Esperar
cv2.waitKey(0)
cv2.destroyAllWindows()