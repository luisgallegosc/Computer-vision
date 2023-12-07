import cv2
img_BGR = cv2.imread("../images/cat.png")
 
cv2.imshow("img_BGR",img_BGR)

# Convertir al formato RGB
img_RGB = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2RGB)
cv2.imshow("img_RGB",img_RGB)

# Convertir de RGB a HSV
img_RGB2HSV = cv2.cvtColor(img_BGR,cv2.COLOR_RGB2HSV)
cv2.imshow("img_RGB2HSV",img_RGB2HSV)

# Convertir de BGR
img_BGR2HSV = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2HSV)
cv2.imshow("img_BGR2HSV",img_BGR2HSV)

img_BGR2GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_BGR2GRAY",img_BGR2GRAY)
# Esperar
cv2.waitKey(0)
cv2.destroyAllWindows()
