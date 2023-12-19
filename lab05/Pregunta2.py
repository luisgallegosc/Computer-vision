import cv2
import numpy as np
#--leer imagen
image = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\lena.jpg")
#--obtener dimensiones de la imagen
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas
#--define la matriz de rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),45,0.7)
k= cv2.getRotationMatrix2D((ancho//2,alto//2),45,1.2)
#--ejecuta la rotación
imageOut = cv2.warpAffine(image,M,(ancho,alto))
imageOut2 = cv2.warpAffine(image,k,(ancho,alto))
# Invertir la imagen verticalmente
imagen_invertida = cv2.flip(image, 0)
#--muestra las imágenes
imageOut3 = image[200:400,200:420 ]
alto_original, ancho_original = image.shape[:2]
# Redimensionar la imagen de salida al tamaño original
imageOut_resized = cv2.resize(imageOut3, (ancho_original, alto_original))

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida 1', imageOut_resized)
cv2.imshow('Imagen de salida 2',imageOut)
cv2.imshow('Imagen de salida 3',imageOut2)
cv2.imshow('Imagen de salida 4', imagen_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()


