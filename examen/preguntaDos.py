import cv2
import numpy as np
video_path = "C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\examen\\video_carros.mp4"
vid = cv2.VideoCapture(video_path)
# Verificar si el video se abre correctamente
if not vid.isOpened():
    print("Error al abrir el video")
    exit()
    
count_line_position = 550
offset = 6 
counter = 0
#verificar dimensiones de los objetos
minWidthRect = 80
minHeightRect = 80

#Comeienza sustractor 
bgSub = cv2.bgsegm.createBackgroundSubtractorMOG()

def handle_centers(x,y,weight,height):
    x1 = int(weight/2)
    y1 = int(height/2)
    cx = x+x1
    cy = y+y1
    
    return cx, cy

detection = []

while True:
    ret,frame = vid.read() #--Leer fotograma
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #--imagen en escala de grises
    blur = cv2.GaussianBlur(grayFrame,(3,3),5) 
    #comenzamo procesamiento
    img_sub = bgSub.apply(blur)
    #aplicar operaciones
    dilates = cv2.dilate(img_sub,np.ones((5,5)))
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatesAda = cv2.morphologyEx(dilates,cv2.MORPH_CLOSE,kernal)
    dilatesAda = cv2.morphologyEx(dilatesAda,cv2.MORPH_CLOSE,kernal)
    #Buscamos contornos
    contour,height = cv2.findContours(dilatesAda,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Dibujamos contornos 
    cv2.line(frame,(10,count_line_position),(1600,count_line_position),(255,0,0),3)
    for (i,c) in enumerate(contour):
        (x,y,width,height) = cv2.boundingRect(c)
        #verificamos dimensiones
        val_contour = (width >= minWidthRect) and (height >= minHeightRect)

        if not val_contour:
            continue
        #dibujamos el rectangulo
        cv2.rectangle(frame,(x,y),(x+width,y+height),(180,150,255),2)
        #conteo de vehiculos
        cv2.putText(frame,"Vehiculos : "+str(counter),(x,y-20),cv2.FONT_HERSHEY_TRIPLEX,1,(255,100,255),2)
        center = handle_centers(x,y,width,height)
        detection.append(center)
        cv2.circle(frame,center,4,(0,255,0),-1)
        for (x,y) in detection:
            #Incrementamos si para el contado
            if y < (count_line_position+offset) and y > (count_line_position-offset):
                counter += 1
            
            cv2.line(frame,(10,count_line_position),(1600,count_line_position),(45,125,10),3)
            detection.remove((x,y))
            print("Vehiculo: ",counter)

    cv2.putText(frame,"VEHICULOS : "+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(14,100,120),5)
    
    cv2.imshow("Contador de Vehiculos",frame)
    if not ret:
        break
    
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
#cerrar el video
vid.release()
