import cv2
import matplotlib.pyplot as plt
#--leer la imagen
imagenInicial = cv2.imread("images/fig1.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow('grayscale image', imagenInicial)

# ecualizar la imagen
imagenEcualizada = cv2.equalizeHist(imagenInicial)
# show image input vs output
cv2.imshow('imagen requerida', imagenEcualizada)

#--esperar
cv2.waitKey(0)
cv2.destroyAllWindows()