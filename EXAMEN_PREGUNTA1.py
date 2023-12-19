#PRIMER EXAMEN PARCIAL
#Alumna: Diana Stephanie Puclla Huaman
#Codigo: 171567
#**********************************************************
#Librerias necesarias
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 1. Leer la imagen Bloom.jpg y visualizarla

#METODO PARA LEER LA IMAGEN CON OPENCV
'''# 1. Leer la imagen Bloom.jpg y visualizarla
image = cv2.imread('Bloom.jpg')
cv2.imshow('Imagen Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#METODO PARA LEER LA IMAGEN CON MATPLOTLIB
# Leer la imagen Bloom.jpg con la libreria Matplotlib para
#mostrar la imagen mas pequeña
image = cv2.imread('Bloom.jpg')
plt.imshow(image)
plt.title('Imagen Original')
plt.axis('off')
plt.show()


# 2. Convertir a RGB y mostrar la imagen
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('Imagen RGB')
plt.axis('off')
plt.show()


# 3. Convertir la imagen a HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# 4. Dividir la imagen en los planos h, s y v
h, s, v = cv2.split(image_hsv)


# 5. Graficar el histograma del plano v
plt.hist(v.ravel(), bins=256, range=[0, 256])
plt.title('Histograma del plano V')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.show()


# 6. Ecualizar el histograma en el canal v y graficar
v_equalized = cv2.equalizeHist(v)
plt.hist(v_equalized.ravel(), bins=256, range=[0, 256])
plt.title('Histograma Ecualizado del plano V')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.show()


# 7. Volver a mezclar los tres planos para obtener una imagen HSV actualizada y mostrarla

#MEZCLAR Y OSTRAR IMAGEN ACTUALIZADA CON OPENCV
'''image_hsv_updated = cv2.merge((h, s, v_equalized))
image_updated = cv2.cvtColor(image_hsv_updated, cv2.COLOR_HSV2BGR)
cv2.imshow('Imagen Actualizada', image_updated)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#MEZCLAR Y MOSTRAR IMAGEN ACTUALIZADA CON MATPLOTLIB
image_hsv_updated = cv2.merge((h, s, v_equalized))
image_updated = cv2.cvtColor(image_hsv_updated, cv2.COLOR_HSV2RGB)
plt.imshow(image_updated)
plt.title('Imagen Actualizada')
plt.axis('off')
plt.show()

# 8. Convertir a RGB nuevamente y mostrar la imagen
image_updated_rgb = cv2.cvtColor(image_updated, cv2.COLOR_BGR2RGB)
plt.imshow(image_updated_rgb)
plt.title('Imagen Actualizada RGB')
plt.axis('off')
plt.show()
