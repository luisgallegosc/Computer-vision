import cv2
# dirección de la imagen
image_path = "../images/marsrover.png"
# Leer o cargar la imagen de esa dirección
image = cv2.imread(image_path)

# Acceder al pixel en la ubicación (0,0)
(b, g, r) = image[0, 0]
print("Valores Red, Green y Blue del pixel (0,0): ", format((b, g, r)))

# Manipuar pixels y mostrar la imagen modificada
image[0:100, 0:100] = (255, 255, 0)
cv2.imshow("Imagen modificada", image)
cv2.waitKey(0)
