import matplotlib.pyplot as plt
import numpy as np
import cv2

# Leer la imagen
image = cv2.imread('../images/waffle.png')
cv2.imshow('original', image)
# Hacer una copia de la imagen
image_copy = np.copy(image)

# Cambiar al RGB
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

cv2.imshow('RGB',image_copy)

# Convertir a escala de crises
gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)

# Detectar esquinas 
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
cv2.imshow('resultado',dst)
# Dilatar la imagen de las esquinas para mejorar los puntos de las esquinas
dst = cv2.dilate(dst,None)

cv2.imshow('imagen dilatada',dst)
# Este valor varía según la imagen y la cantidad de esquinas que desee detectar.
# Intente cambiar este parámetro libremente, 0.1, para que sea más grande o más pequeño y vea qué sucede
thresh = 0.1*dst.max()
print (dst.max())
# Crea una copia de la imagen para dibujar esquinas
corner_image = np.copy(image)

# Iterar por todas las esquinas y dibujarlas en la imagen (si pasan el umbral)
for j in range(0, dst.shape[0]):
    for i in range(0, dst.shape[1]):
        if(dst[j,i] > thresh):
            # image, center pt, radius, color, thickness
            cv2.circle( corner_image, (i, j), 1, (0,255,0), 1)

cv2.imshow('esquinas',corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()