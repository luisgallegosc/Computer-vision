'''
Primera alternativa para realizar el seguimiento del objeto marcado
esto usando meanShift, el seguimiento no es el mas optimo, pero de cierta
manera cumple en la medida de lo posible, es por eso qeu se construyo una segunda
version, se uso el codigo desarrollado en el laboratorio del curso
'''

# Importar modulos
import cv2
import numpy as np

# Crear un objeto VideoCapture
video = cv2.VideoCapture(0)
# Verificar si el video se abrio correctamente
if video.isOpened() == False:
    print("No se puede abrir el video!")


# tomar el primer fotograma del video : extraemos una region a la que le haremos seguimiento
ret, frame = video.read()
# Compruebe si el cuadro se lee correctamente
if ret == False:
    print("No se puede leer el video")  

# Especificar el cuadro delimitador inicial
roi = cv2.selectROI(frame, False)

#Se inicializa el tracking
track_window = (roi)

hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Configure los criterios de terminación, ya sea 10 iteraciones o mueva al menos 1 punto
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

# comienza a rodar el video
while(1):
    ret ,frame = video.read()

    if ret == True:
        #convertir la imagen a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # aplicar meanshift para obtener la nueva ubicación
        ret, track_window = cv2.meanShift(dst, track_window, term_crit) #term_crit terminos de determinacion del seguim

        # Dibujar en la imagen un rectangulito
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)    #255 : color, 2 : grosor
        cv2.imshow('img2',img2)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)

    else:
        break

cv2.destroyAllWindows()
