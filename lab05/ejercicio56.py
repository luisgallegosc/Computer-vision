import numpy as np
import matplotlib.pyplot as plt #carga la librería para graficar
import cv2
#--leer la imagen
img = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\lena.jpg")
#--obtener dimensiones
rows,cols,ch = img.shape

#--definir 3 puntos de la imagen original
pts1 = np.float32([[100,400],[400,100],[100,100]])
#--definir 3 puntos en la imagen de salida
pts2 = np.float32([[50,300],[400,200],[80,150]])

#--obtener la matriz de transformación 
M = cv2.getAffineTransform(pts1,pts2)
#--aplicar la transofrmación
dst = cv2.warpAffine(img,M,(cols,rows))
#--mostrar las imágenes
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
 