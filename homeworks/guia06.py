import cv2
import numpy as np
from matplotlib import pyplot as plt

# Rutas de las imágenes de los tableros de ajedrez
file_path1 = 'C:/Users/benito/OneDrive/Escritorio/UNSAAC/8vo/vision computacional/homeworks/board1.jpg'
file_path2 = 'C:/Users/benito/OneDrive/Escritorio/UNSAAC/8vo/vision computacional/homeworks/board2.jpg'

# Lee las imágenes
img1 = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)

# Verifica si las imágenes se cargaron correctamente
if img1 is not None and img2 is not None:
    # Establece un tamaño común (ajusta según sea necesario)
    common_size = (200, 200)

    # Redimensiona ambas imágenes al tamaño común
    img1_resized = cv2.resize(img1, common_size)
    img2_resized = cv2.resize(img2, common_size)

    # Calcula la diferencia absoluta entre las imágenes
    diferencia = cv2.absdiff(img1_resized, img2_resized)

    # Aplica umbral para resaltar las diferencias significativas
    umbral = 30  # Puedes ajustar este valor según tus necesidades
    _, umbral_dif = cv2.threshold(diferencia, umbral, 255, cv2.THRESH_BINARY)

    # Encuentra los contornos de las diferencias
    contornos, _ = cv2.findContours(umbral_dif, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibuja los contornos en una imagen en blanco (fondo)
    resultado = np.zeros_like(img1_resized)
    cv2.drawContours(resultado, contornos, -1, 255, thickness=cv2.FILLED)

    # Muestra las imágenes y resultados
    plt.subplot(131), plt.imshow(img1_resized, cmap='gray'), plt.title('Tablero 1')
    plt.subplot(132), plt.imshow(img2_resized, cmap='gray'), plt.title('Tablero 2')
    plt.subplot(133), plt.imshow(resultado, cmap='gray'), plt.title('Áreas con fichas movidas')
    plt.show(block=True)

    # Espera una tecla antes de cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error al cargar las imágenes.")
    