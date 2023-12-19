import cv2

# Leer la imagen
image = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab05\\lena.jpg")

# Recortar una región de la imagen
imageOut = image[200:400,200:420 ]

# Obtener dimensiones originales de la imagen
alto_original, ancho_original = image.shape[:2]

# Redimensionar la imagen de salida al tamaño original
imageOut_resized = cv2.resize(imageOut, (ancho_original, alto_original))

# Mostrar las imágenes
cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imageOut_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
