#importar el módulo OpenCV 
import cv2
img = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab01\\lion.jpg")
if img is None:
    print ("imagen no encontrada")
cv2.imshow("Lion",img)
cv2.waitKey(0)
cv2.destroyAllWindows