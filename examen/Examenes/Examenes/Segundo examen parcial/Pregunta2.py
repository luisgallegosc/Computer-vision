import cv2
import matplotlib.pyplot as plt
frase_escrita = cv2.imread('frase_escrita.png')
B = cv2.imread('letra_b.png')

frase_esc_cpia = frase_escrita.copy()
#conversion
frase_escrita_gris = cv2.cvtColor(frase_escrita, cv2.COLOR_BGR2GRAY)
B_gris = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)
#binarizamos
frase_escrita_bin = cv2.threshold(frase_escrita_gris, 0, 255, cv2.THRESH_OTSU)
B_bin = cv2.threshold(B_gris, 0, 255, cv2.THRESH_OTSU)
#hallamos los contornos
contornos, parentesco = cv2.findContours(frase_escrita_bin[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#Obtenemos los contornos de la letra B
contornos_B, parentesco_B = cv2.findContours(B_bin[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contExterior_B = contornos_B[0]

metricasSimilitud = []

for contorno in contornos:
    metricSimilitud_contorno = cv2.matchShapes(contorno, contExterior_B, cv2.CONTOURS_MATCH_I1, 0)
    metricasSimilitud.append(metricSimilitud_contorno)
#mejor aproximacion
min_MetricaSim = min(metricasSimilitud)
indice_min_metric = metricasSimilitud.index(min_MetricaSim)
contorno_deseado = contornos[indice_min_metric]
x,y,w,h = cv2.boundingRect(contorno_deseado)

#Dibujamos la caja 
imagen_resultado = cv2.rectangle(frase_esc_cpia, (x,y),(x+w,y+h), (255,0,0), 2)

cv2.imshow('frase escrita con la B detectada', imagen_resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()