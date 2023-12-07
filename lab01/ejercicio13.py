import cv2
# ruta de la imagen
image_path = "../images/marsrover.png"
# Leer la imagen de esa dirección
image = cv2.imread(image_path)
# La imagen es un array NumPy
print("Dimensiones de la imagen: ", image.ndim)
print("Altura de la imagen: ", format(image.shape[0]))
print("Ancho de la imagen: ", format(image.shape[1]))
print("Canales de la imagen: ", format(image.shape[2]))
print("Tamaño en bytes del arreglo imagen: ", image.size)
# Mostrar la imagen y esperar hasta presionar una tecla
cv2.imshow("Mi imagen", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
