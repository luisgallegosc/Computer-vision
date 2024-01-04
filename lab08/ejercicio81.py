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
#--Encuentra los contornos en la imagen binaria 
contours,hierarchy = cv2.findContours(inverted_binary_im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
#--Marque todos los contornos detectados en la imagen BGR original en  cualquier color (digamos, verde).  
#--Estableceremos el grosor en 3: 
with_contours = cv2.drawContours(image, contours, -1,(0,255,0),3) 
cv2.imshow('Contornos detectados en la imagen RGB', with_contours) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
#--Finalmente, muestre el recuento total de los contornos detectados: 
print('El número total de contornos detectados es:') 
print(len(contours))  
