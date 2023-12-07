import cv2  
import numpy as np  
import matplotlib.pyplot as plt

# Leer la imagen original
img = cv2.imread("..\images\lena.jpg")

# Obtener altura y ancho
height = img.shape[0]
width = img.shape[1]
print('height : ',img.shape[0])
print('width : ', img.shape[1])
# Conversión de muestra en área de 16 * 16
numHeight = int(height/64)
numwidth = int(width/64)

# crea una nueva imagen
new_img = np.zeros((height, width, 3), np.uint8)

# bucle de muestreo de imagen en area de 16*16
for i in range(64):
    # Obtener coordenada Y
    y = i*numHeight
    for j in range(64):
        # Obtener coordenada X
        x = j*numwidth
        # Obtener los píxeles de color de relleno en la esq. sup. izq.
        b = img[y, x][0]  
        g = img[y, x][1]
        r = img[y, x][2]
        # Configuración de ciclo de muestreo de área pequeña
        for n in range(numHeight):
            for m in range(numwidth):
                new_img[y+n, x+m][0] = np.uint8(b)
                new_img[y+n, x+m][1] = np.uint8(g)
                new_img[y+n, x+m][2] = np.uint8(r)
        
# Mostrar imagenes
cv2.imshow("src", img)
cv2.imshow("", new_img)

# Esperar
cv2.waitKey(0)
cv2.destroyAllWindows()
