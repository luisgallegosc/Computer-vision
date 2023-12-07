import cv2  
import numpy as np  
import matplotlib.pyplot as plt

# Leer la imagen original
img = cv2.imread("../images/lena.jpg")

#Get image height and width
# Obtener alto y ancho de la imagen
height = img.shape[0]
width = img.shape[1]

# Crear imagenes nuevas
new_img1 = np.zeros((height, width, 3), np.uint8)
new_img2 = np.zeros((height, width, 3), np.uint8)
new_img3 = np.zeros((height, width, 3), np.uint8)

# Cuantización de la imagen nivel 2
for i in range(height):
    for j in range(width):
        for k in range(3): # Corresponmdiente a los comp. BGR 
            if img[i, j][k] < 128:
                gray = 0
            else:
                gray = 128
            new_img1[i, j][k] = np.uint8(gray)

# Cuantización de la imagen nivel 4
for i in range(height):
    for j in range(width):
        for k in range(3): # Correspondente a los comp. BGR
            if img[i, j][k] < 64:
                gray = 0
            elif img[i, j][k] < 128:
                gray = 64
            elif img[i, j][k] < 192:
                gray = 128
            else:
                gray = 192
            new_img2[i, j][k] = np.uint8(gray)

# Cuantización de la imagen nivel 8
for i in range(height):
    for j in range(width):
        for k in range(3): # Correspondente a los comp. BGR
            if img[i, j][k] < 32:
                gray = 0
            elif img[i, j][k] < 64:
                gray = 32
            elif img[i, j][k] < 96:
                gray = 64
            elif img[i, j][k] < 128:
                gray = 96
            elif img[i, j][k] < 160:
                gray = 128
            elif img[i, j][k] < 192:
                gray = 160
            elif img[i, j][k] < 224:
                gray = 192
            else:
                gray = 224
            new_img3[i, j][k] = np.uint8(gray)

# Mostrar las imagenes
titles = [u'(a) Imagen Original', u'(b) Cuantización-L2', u'(c) Cuantización-L4', u'(d) Cuantización-L8']  
images = [img, new_img1, new_img2, new_img3]  
for i in range(4):  
   plt.subplot(2,2,i+1), plt.imshow(images[i]), 
   plt.title(titles[i])  
   plt.xticks([]),plt.yticks([])  
plt.show()
