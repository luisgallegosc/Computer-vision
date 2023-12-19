#PRIMER EXAMEN PARCIAL
#Alumna: Diana Stephanie Puclla Huaman
#Codigo: 171567
#**********************************************************

#Librerias necesarias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Matriz dada que representa la imagen
imagen_matriz = np.array([[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]])

# Factor de escala
factor_escala = 3

# Dimensiones de la matriz inicial (alto y ancho)
alto_inicial, ancho_inicial = imagen_matriz.shape

# Dimensiones de la matriz final escalada
alto_final = alto_inicial * factor_escala
ancho_final = ancho_inicial * factor_escala

# Matriz final escalada
imagen_final = np.zeros((alto_final, ancho_final))

#La interpolación del vecino más cercano se realiza en el siguiente fragmento de código:
# Escalado utilizando el método del vecino más cercano
for i in range(alto_final):
    for j in range(ancho_final):
        # Obtener la posición correspondiente en la matriz inicial
        x = int(i / factor_escala)
        y = int(j / factor_escala)

        # Asegurar que las coordenadas estén dentro de los límites de la matriz inicial
        x = min(max(x, 0), alto_inicial - 1)
        y = min(max(y, 0), ancho_inicial - 1)
        
        # Copiar el valor del vecino más cercano
        imagen_final[i, j] = imagen_matriz[x, y]

# Mostrar la matriz final
print(imagen_final)
