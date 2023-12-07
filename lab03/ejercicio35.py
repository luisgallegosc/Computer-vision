import cv2
import numpy
  
# leer imagen
src = cv2.imread('../images/lena_ruido.jpg', cv2.IMREAD_UNCHANGED)
 

# aplicar el filtro gaussiano
dst = cv2.GaussianBlur(src,(9,9),cv2.BORDER_DEFAULT)
 
# mostrar la imagen original y la imagen filtrada
cv2.imshow("Gaussian Smoothing",numpy.hstack((src, dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image