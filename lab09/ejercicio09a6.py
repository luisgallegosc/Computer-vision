# -*- coding: utf-8 -*-
'''
Introducción a SIFT (Transformación de características invariables de escala)
 El algoritmo SIFT implica principalmente cuatro pasos:
 1. Detección extrema de espacio de escala (detección de extremo de espacio de escala)
 2. Localización de puntos clave.
 3. Asignación de dirección
 4. Descriptor de punto clave
 5. Coincidencia de puntos clave
 La siguiente demostración es la función SIFT en OpenCV: cv2.SIFT ()
'''
 
import cv2
 
img = cv2.imread('../images/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
'''
 Cuando se usa OpenCV con Python para SIFT, la compilación tiene estos problemas:
AttributeError: module 'cv2' has no attribute 'SIFT'
 El código de error es el siguiente:
sift = cv2.SIFT()
 Motivo: opencv ha integrado SIFT y otros algoritmos en la colección xfeatures2d. La redacción modificada es la siguiente:
sift=cv2.xfeatures2d.SIFT_create()
'''
# sift = cv2.SIFT()
sift = cv2.xfeatures2d.SIFT_create()
 
 #La función # sift.detect () es encontrar puntos clave en la imagen. Si solo desea reducir parte de la imagen, puede pasar la máscara
 # Cada punto clave es una estructura especial con muchos atributos. Como coordenadas (x, y), tamaño de campo significativo, especificar el ángulo de su dirección, especificar la respuesta de la intensidad de los puntos clave, etc.
kp = sift.detect(gray, None)
 
 # drawKeypoints: la primera imagen de entrada del parámetro, el segundo punto clave del parámetro, la tercera imagen de salida del parámetro
 # cv2.drawKeypoints () se usa para dibujar círculos pequeños en la posición de los puntos clave. Si le pasa una bandera cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
 # Se dibujará un círculo con un tamaño como punto clave, e incluso se mostrará su dirección.
# img = cv2.drawKeypoints(gray, kp, img)
img = cv2.drawKeypoints(gray, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
cv2.imwrite('sift_keypoints.jpg', img)
 
'''
 Ahora para calcular el descriptor, OpenCV proporciona dos métodos:
 1. Ahora que se ha encontrado el punto clave, puede usar sift.compute () para calcular el descriptor del punto clave, por ejemplo: kp, des = sift.compute (gris, kp)
 2. Si no se encuentra el punto clave, puede usar la función sift.detectAndCompute () para buscar directamente el punto clave y el descriptor en un solo paso: de la siguiente manera:
'''
 # El kp que se encuentra aquí será una lista de puntos clave, y des es una matriz numpy de forma Number_of_Keypoints * 128
kp, des = sift.detectAndCompute(gray, None)
 
cv2.imshow('sift_keypoints', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()