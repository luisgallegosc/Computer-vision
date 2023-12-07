import cv2
import numpy as np
from skimage.util import random_noise
 
# cargar la imagen
img = cv2.imread("..\images\lena.jpg")
cv2.imshow('sin ruido',img)

# agregar diferentes tipos de ruido a la imagen
#noise_img = random_noise(img, mode='gaussian', clip=True) 
#noise_img = random_noise(img, mode='salt', amount=0.005)
#noise_img = random_noise(img, mode='pepper', amount=0.005)
#noise_img = random_noise(img, mode='speckle', var=0.005, clip=True)
#noise_img = random_noise(img, mode='poisson', seed=1)
noise_img = random_noise(img, mode='s&p',amount=0.01)

#Las funciones anteriores devuelven una imagen de punto flotante
#en el rango de [0,1], los cambiamos a 'uint8'
#y de [0,255]

noise_img = np.array(255*noise_img, dtype = 'uint8')
 
# mostrar el ruido en la imagen
cv2.imshow('ruidos',noise_img)
cv2.waitKey(0)
