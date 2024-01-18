# importar los paquetes necesarios
import numpy as np
import glob
import os
import cv2
#Ruta a la plantilla
templatePath = 'template.jpeg'

#ruta a la carpeta de imágenes
imageFolderPath = 'images'

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# inicializar las dimensiones de la imagen que se cambiará de tamaño y
	# toma el tamaño de la imagen
	dim = None
	(h, w) = image.shape[:2]

	# si tanto el ancho como el alto son None, entonces devuelve la
	# imagen original
	if width is None and height is None:
		return image

	# compruebe si el ancho es None
	if width is None:
		# calcular la relación de la altura y construir las
		# dimensiones
		r = height / float(h)
		dim = (int(w * r), height)

	# de lo contrario, la altura es None
	else:
		# calcular la relación del ancho y construir las
		# dimensiones
		r = width / float(w)
		dim = (width, int(h * r))

	# cambiar el tamaño de la imagen
	resized = cv2.resize(image, dim, interpolation = inter)

	# devolver la imagen redimensionada
	return resized

#imagen de plantilla de lectura
template = cv2.imread(templatePath,0)

#aplicando transformación laplaciana a la plantilla
template = cv2.Laplacian(template,cv2.CV_64F)
template = np.float32(template)
#th y tw son la altura y el ancho de la plantilla
(tH, tW) = template.shape[:2]
i=0
# recorre las imágenes para encontrar la plantilla
for imagePath in glob.glob(imageFolderPath + "/*.jpg"):
	i+=1
	#lee la imagen
	image = cv2.imread(imagePath)
	
	#convierte la imagen a escala de grises
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#aplica desenfoque gaussiano con un tamaño de kernel de 3 en la imagen
	blur = cv2.GaussianBlur(gray,(3,3),0)
	gray = cv2.Laplacian(blur,cv2.CV_64F)
	gray = np.float32(gray)
	found = None
	pos=0
	# bucle sobre las escalas de la imagen
	for scale in np.linspace(0.5, 2, 30):
		# cambiar el tamaño de la imagen de acuerdo con la escala 
		# y realizar un seguimiento de la proporción del cambio de tamaño
		
		resized = resize(gray, width = int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])

		# si la imagen redimensionada es más pequeña que la plantilla, salir del bucle
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break

		# coincidencia para encontrar la plantilla en la imagen 
		result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF)
		(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

		# si hemos encontrado un nuevo valor máximo de correlación, 
		# entonces actualice encontrado
		if found is None or maxVal > found[0]:
			found = (maxVal, maxLoc, r)
			(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
			(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
			
			

	# descomprime la variable de contabilidad y calcula las coordenadas (x, y) 
	# del cuadro delimitador en función de la proporción redimensionada
	if found is not None:  # y pos>5:
		# dibujar un cuadro delimitador alrededor del resultado detectado y mostrar la imagen
		(maxVal, maxLoc, r) = found
		if(maxVal>350000):
			print(imagePath,'maxval=',maxVal,'Cursor detectado en la ubicacion:',(int(maxLoc[0] * r), int(maxLoc[1] * r)))
			(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
			(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
			cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
		else:
			print(imagePath,'Cursor no detectado')
	
	
	cv2.imshow(imagePath, image)
	cv2.waitKey(0)
	
	