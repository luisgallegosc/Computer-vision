import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer la imagen
img_kirsch = cv2.imread('images/mary.jpg', cv2.IMREAD_GRAYSCALE)
rgb_img_kirsch = cv2.cvtColor(img_kirsch, cv2.COLOR_BGR2RGB)

# Aplicar el operador de Kirsch
kirsch_x = cv2.filter2D(img_kirsch, cv2.CV_64F, np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]))
kirsch_y = cv2.filter2D(img_kirsch, cv2.CV_64F, np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]))

# Calcular la magnitud del gradiente
magnitude_kirsch = np.sqrt(kirsch_x**2 + kirsch_y**2).astype(np.uint8)

# Mostrar las imágenes
titles_kirsch = ['Imagen original', 'Operador de Kirsch', 'Magnitud del Gradiente']
images_kirsch = [rgb_img_kirsch, magnitude_kirsch]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images_kirsch[i], 'gray')
    plt.title(titles_kirsch[i])
    plt.xticks([]), plt.yticks([])

plt.show()
