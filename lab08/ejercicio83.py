import cv2
#--Lea la imagen como una imagen BGR:
image = cv2.imread('../images/sample shapes.png')
#--Conviértelo a escala de grises:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray' , gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Convertir a imagen binaria con Otsu
ret,binary_im = cv2.threshold(gray_image,0,255,cv2.THRESH_OTSU)
cv2.imshow('imagen binaria', binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

#--Invierta la imagen y muéstrela
inverted_binary_im= ~binary_im
cv2.imshow('inverso de la imagen binaria', inverted_binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--la imagen debe tener tres canales, replicaremos el plano único de la 
# imagen binaria tres veces y luego fusionaremos los tres planos para 
# extenderlo al espacio de color BGR.
bgr = cv2.merge([inverted_binary_im, inverted_binary_im, inverted_binary_im])
#--Encuentra los contornos en la imagen binaria
contours,hierarchy = cv2.findContours(inverted_binary_im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#--Marque todos los contornos detectados en la imagen BGR original en cualquier color (digamos, verde). 
#--Estableceremos el grosor en 3:

with_contours = cv2.drawContours(bgr, contours, 0,(0,0,255),10)
with_contours = cv2.drawContours(with_contours, contours, 1,(0, 255, 0),20)
with_contours = cv2.drawContours(with_contours, contours, 2, (255,0, 0), 30)

cv2.imshow('Contornos detectados', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Finalmente, muestre el recuento total de los contornos detectados:
print('El número total de contornos detectados es:')
print(len(contours))