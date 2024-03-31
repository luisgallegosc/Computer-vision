import cv2

# Cargar las dos imágenes
imagen1 = cv2.imread('frase_escrita.png')  # Primera imagen en escala de grises
imagen2 = cv2.imread('letra_b.png', 0)  # Segunda imagen en escala de grises

# Realizar el umbralizado en ambas imágenes
_, umbral1 = cv2.threshold(imagen1, 127, 255, cv2.THRESH_BINARY)
_, umbral2 = cv2.threshold(imagen2, 127, 255, cv2.THRESH_BINARY)

# Encontrar los contornos en ambas imágenes
contornos1, _ = cv2.findContours(umbral1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contornos2, _ = cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Variables para almacenar la mejor coincidencia
mejor_coincidencia = None
mejor_diferencia = float('inf')

# Recorrer los contornos de la primera imagen y encontrar el mejor ajuste
for contorno1 in contornos1:
    # Realizar el ajuste de formas con cada contorno de la segunda imagen
    for contorno2 in contornos2:
        diferencia = cv2.matchShapes(contorno1, contorno2, cv2.CONTOURS_MATCH_I2, 0)
        
        # Actualizar la mejor coincidencia
        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_coincidencia = contorno1

# Dibujar el contorno de la mejor coincidencia en la primera imagen
resultado = cv2.cvtColor(umbral1, cv2.COLOR_GRAY2BGR)
cv2.drawContours(resultado, [mejor_coincidencia], -1, (0, 255, 0), 2)

# Mostrar la imagen resultante
cv2.imshow('Resultado', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()