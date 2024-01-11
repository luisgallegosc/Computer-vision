import cv2

# Ruta completa del archivo
file_path = 'C:/Users/benito/OneDrive/Escritorio/UNSAAC/8vo/vision computacional/lab08/sample shapes.png'

# Intenta cargar la imagen en color
image = cv2.imread(file_path)

# Imprime un mensaje para verificar si se cargó la imagen
if image is not None:
    print("La imagen se cargó correctamente.")
else:
    print("No se pudo cargar la imagen. Verifica la ruta y el nombre del archivo.")

# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow('gray', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertir a imagen binaria con Otsu
ret, binary_im = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)

# Mostrar la imagen binaria
cv2.imshow('imagen binaria', binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Invertir la imagen y mostrarla
inverted_binary_im = ~binary_im
cv2.imshow('inverso de la imagen binaria', inverted_binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Encontrar los contornos en la imagen binaria
contours, hierarchy = cv2.findContours(inverted_binary_im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Marcar todos los contornos detectados en la imagen BGR original en cualquier color (digamos, verde)
# Estableceremos el grosor en 3
with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)

# Mostrar la imagen con contornos
cv2.imshow('Contornos detectados en la imagen RGB', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar el recuento total de contornos detectados
print('El número total de contornos detectados es:')
print(len(contours))
