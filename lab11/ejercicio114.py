import cv2
#--Especifique la ruta de los archivos XML OpenCV que se 
# utilizarán para detectar personas y automóviles en cada imagen.
haarcascade_car = 'opencv_xml_files/haarcascade_car.xml'
haarcascade_fullbody = 'opencv_xml_files/haarcascade_fullbody.xml'
#--cargue el archivo XML que se utilizará para detectar automóviles.
car_classifier = cv2.CascadeClassifier(haarcascade_car)
#--para detectar peatones use el archivo
#'opencv_xml_files/haarcascade_fullbody.xml'
#classifier = cv2.CascadeClassifier(haarcascade_fullbody)
cap = cv2.VideoCapture('cars.avi')
#--para detectar peatones
#cap = cv2.VideoCapture('walking.avi')
count = 0
while cap.isOpened():
    count +=1
    # here 20 means every 20th frame.
    if count % 20==0:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        car=car_classifier.detectMultiScale(gray,1.1, 3)
        for (x,y,w,h) in car:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'car', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255))
        cv2.imshow('car', frame)
    #--para peatones
    #cv2.imshow('person', frame)
    #--presione 'q' para cerrar la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()