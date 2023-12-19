
import cv2

# Leer la imagen
imagen_original = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\lena.jpg")

# Invertir la imagen verticalmente
imagen_invertida = cv2.flip(imagen_original, 0)

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen_original)
cv2.imshow('Imagen Invertida', imagen_invertida)
cv2.waitKey(0)
cv2.destroyAllWindows()
