#importar el módulo OpenCV
import cv2
# cargar imagen
img = cv2.imread("images/lion.jpg")
if img is None:
    print("Imagen no encontrada")
    # Display the image
cv2.imshow("Lion",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
