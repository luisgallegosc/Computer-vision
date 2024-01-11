import cv2
import numpy as np
import sys

def onTrackbarChange(max_slider):
    cimg = np.copy(img)

    p1 = max_slider
    p2 = max_slider * 0.4

    #--Detectar circulos usando la transformada de Hough para detectar círculos
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, cimg.shape[0]/64, param1=p1, param2=p2, minRadius=25, maxRadius=50)

    #--Si por lo menos se ha detectado un círculo
    if circles is not None:
        cir_len = circles.shape[1] # almacenar la longitud de los círculos encontrados
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Dibuja el círculo exterior
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Dibuja el centro del círculo
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    else:
        cir_len = 0 # no se detectaron círculos
    
    # Mostrar imagen de salida
    cv2.imshow('Image', cimg)    

    # Imagen de borde para depuración
    edges = cv2.Canny(gray, p1, p2)
    cv2.imshow('Edges', edges)
   
if __name__ == "__main__":
    # Leer imagen
    img = cv2.imread("../images/brown-eyes.jpg", 1)

    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Crear ventanas de visualización
    cv2.namedWindow("Edges")
    cv2.namedWindow("Image")
        # La barra de seguimiento se utilizará para cambiar el umbral del borde
    initThresh = 105 
    maxThresh = 200 

    # Crear barra de seguimiento
    cv2.createTrackbar("Threshold", "Image", initThresh, maxThresh, onTrackbarChange)
    onTrackbarChange(initThresh)
    
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()

