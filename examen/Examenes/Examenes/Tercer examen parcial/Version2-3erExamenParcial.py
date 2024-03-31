'''
Segunda alternativa para realizar el seguimiento del objeto marcado
esto usando TrackerCSRT, y el resultado del seguimiento es mejor que al aplicar
meanShift, se uso codigo que se pudo encontrar en internet
'''

# Importar modulos
import cv2
import numpy as np

#incializamos el objeto tracker, que servira para seguir la imagen seleccionada
tracker = cv2.TrackerCSRT_create()
# Colocamos camara en true ya que trabajaremos con la camara
camera = True

#Obtenemos el video que en realidad sera lo que este capturando la camara en tiempo real
if camera:
    video = cv2.VideoCapture(0)
else:
    print('El video de camara no se puede realizar')

# leemos el primer frame del video
ret,frame = video.read()
# seleccionamos el objeto del cual queremos capturar su movimiento
BB = cv2.selectROI(frame, False)
#Inicializamos el tracker para que capture el movimiento
tracker.init(frame, BB)

while True:
    #Capturamos el siguiente frame del video
    ret,frame = video.read()
    #Obtenemos informacion para actualizar el tracker
    track_update, BB = tracker.update(frame)
    #actualizamos el valor del tracker
    if track_update:
        #calculamos las nuevas ubicaciones del objeto
        top_left = (int(BB[0]), int(BB[1]))
        bottom_right = (int(BB[0]+BB[2]), int(BB[1]+BB[3]) )
        #pintamos con un rectangulo al objeto en movimiento
        cv2.rectangle(frame, top_left, bottom_right, (255,0,0),2)
    #mostramos la captura de la camara guiando el mov del objeto
    cv2.imshow('Output', frame)

    k = cv2.waitKey(5)
    if k == 27:
        break 
video.release()
cv2.destroyAllWindows()
