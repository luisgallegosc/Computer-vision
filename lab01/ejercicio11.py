#importar el módulo OpenCV 
import cv2 
# cargar imagen 
img = cv2.imread("C:\\Users\\benito\\OneDrive\\Escritorio\\UNSAAC\\8vo\\vision computacional\\lab01\\lion.jpg",0) 
if img is None: 
    print("Imagen no encontrada") 
# Display the image 
cv2.imshow("lion",img) 
cv2.imwrite('campo_gray.jpg',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()