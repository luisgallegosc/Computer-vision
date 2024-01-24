import cv2
import numpy as np
#--leer el video
video = cv2.VideoCapture("../videos/video.mp4")
##video=cv2.VideoCapture(0)

i = 0
while True:
    #--leemos las imagenes del video que se almacenaran en frame
	ret, frame = video.read()
    #--en caso de que no se haya podido tomar una imagen ret=false
	if ret == False: break
    #--convertimos a escala de grises
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #--Ahora usaremos el contador i, este nos permitirá guardar una imagen del fondo
    #  de la escena a la veinteava iteración con el objetivo de asegurar que se encienda
    #  correctamente la cámara y evitar tomar una imagen oscura en un principio. 
    #  Cuando la iteración es mayor a 20 en cambio podremos seguir con el proceso de sustracción de imágenes.

    #--Cuando el contador llega a 20, entonces se graba la imagen gray en bgGray, 
    # que será la imagen del fondo de la escena. Esta nos servirá para restarla de la imagen actual.
	if i == 20:
		bgGray = gray

    #-- Una vez que el contador es mayor a 20, se procede a usar cv2.absdiff, 
    #   para poder restar la imagen actual y la del fondo.
	if i > 20:
		dif = cv2.absdiff(gray, bgGray)
        #--convertir la la imagen dif a binaria, 
		_, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
	    #--encontrar los contornos
		cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(frame, cnts, -1, (0,0,255),2)		
		
        #--Una vez que tenemos todos los contornos encontrados, 
        # es necesario descartar aquellos que sean muy pequeños y que no representen movimiento. 
        # Para ello es necesario estudiar cada uno de estos contornos por lo que emplearemos el bucle for.
		for c in cnts:
			area = cv2.contourArea(c)
			if area > 9000:
				x,y,w,h = cv2.boundingRect(c)
				cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)

	cv2.imshow('Frame',frame)

	i = i+1
	if cv2.waitKey(30) & 0xFF == ord ('q'):
		break
video.release()