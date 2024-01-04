import cv2
image = cv2.imread('../images/many fruits.png')
cv2.imshow('Imagen original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--convertir a escala de grises
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Convertir a binario con un umbral adecuado
ret,binary_im = cv2.threshold(gray_image,245, 255,cv2.THRESH_BINARY)
cv2.imshow('binario', binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--invertir la imagen
binary_im= ~binary_im
cv2.imshow('binario invertido', binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--encontrar los contornos externos
contours,hierarchy = cv2.findContours(binary_im, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#--dibujar los contornos
with_contours = cv2.drawContours(image,contours, -1,(0,0,255),3)
cv2.imshow('contornos marcados en la imagen RGB', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()