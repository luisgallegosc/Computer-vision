import cv2
import numpy as np
face_classifier = cv2.CascadeClassifier('opencv_xml_files/haarcascade_frontalface_alt.xml')
resized = cv2.imread("images/varias_caras.jpg")
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
''' Nuestro clasificador devuelve el ROI de la cara detectada como una tupla, almacena 
    la coordenada superior izquierda y la coordenada inferior derecha'''
faces = face_classifier.detectMultiScale(gray, 1.08, 1)
'''Cuando no se detectan caras, face_classifier regresa y la tupla vacía'''
if faces is ():
    print("No se han encontrado caras")
'''Iteramos nuestra matriz de caras y dibujamos un rectángulo sobre cada cara en caras'''
for (x,y,w,h) in faces:
    cv2.rectangle(resized, (x,y), (x+w,y+h), (127,0,255), 2)
    cv2.imshow('Face Detection', resized)
    
cv2.waitKey(0)    
cv2.destroyAllWindows()