# Importar modulos
import cv2
import numpy as np

# Crear un objeto VideoCapture
video = cv2.VideoCapture(0)
# Verificar si el video se abrio correctamente
if video.isOpened() == False:
    print("No se puede abrir el video!")
# tomamos el primer fotograma del video
ret, frame = video.read()
# Compruebe si el cuadro se lee correctamente
if ret == False:
    print("No se puede leer el video")  
# Especificar el cuadro delimitador inicial
bbox = cv2.selectROI(frame, False)
print('Se selecciono un bbox *****')
print("Este es un BBOX",bbox)
#print(bbox)
cv2.destroyAllWindows()
# Creacion del tracker GOTURN
tracker = cv2.legacy.TrackerCSRT_create()
# Inicializar rastreador
ret = tracker.init(frame,bbox)
# Crea una nueva ventana donde mostraremos los resultados
cv2.namedWindow("Tracker")
#Mostrar el primer cuadro
cv2.imshow("Tracker",frame)
while True:
    # Leer siguiente fotograma
    ret, frame = video.read()
    # Compruebe si se leyó el cuadro
    if ret == False:
        break
    # Iniciar timer
    timer = cv2.getTickCount()
    # Actualizar rastreador
    found, bbox = tracker.update(frame)
    # Calcular FPS
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    # Si se encuentra el objeto, dibuja bbox
    if found:
        # Esquina superior izquierda
        topLeft = (int(bbox[0]), int(bbox[1]))
        # Esquina inferior derecha
        bottomRight = (int(bbox[0]+bbox[2]),int(bbox[1]+bbox[3]))
        # Mostrar cuadro delimitador
        cv2.rectangle(frame, topLeft, bottomRight, (255,0,0), 2)
    else:
        # Mostrar estado
        cv2.putText(frame, "Objeto no encontrado", (20,70), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)

    # Mostrar FPSs
    cv2.putText(frame, "FPS : " + str(int(fps)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (200,0,0), 2);

    # Mostrar cuadro
    cv2.imshow("Tracker",frame)
    k = cv2.waitKey(5)
    if k == 27:
        break
cv2.destroyAllWindows()
