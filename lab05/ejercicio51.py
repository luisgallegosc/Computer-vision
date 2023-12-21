import cv2
import numpy as np
#--leer la imagen 
img = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\ave.jpg")
#--obtenemos ancho y alto de la imagen
rows = img.shape[0]
cols = img.shape[1]
#--desplazamiento
tx = 210
ty = 150
#--crea la matriz de traslación
M = np.float32([[1,0,tx],
                [0,1,ty]])
#--realiza la traslación
dst = cv2.warpAffine(img,M,(cols,rows))
#--muestra la imagen
cv2.imshow('ave', img)
cv2.imshow('traslación',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()