import cv2
import numpy as np

inputImagePath = "images/face.jpg"
haarCascadePath = "opencv_xml_files/haarcascade_frontalface_default.xml"
inputImage = cv2.imread(inputImagePath, cv2.COLOR_BGR2RGB)
grayInputImage = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
haarCascade = cv2.CascadeClassifier(haarCascadePath)
detectedFaces = haarCascade.detectMultiScale(grayInputImage, 1.15, 1)
for face in detectedFaces:
    # Cada cara es un rectángulo que representa 
    # el cuadro delimitador alrededor de la cara detectada
    x, y, w, h = face
    cv2.rectangle(inputImage, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow("Faces Detected", inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()