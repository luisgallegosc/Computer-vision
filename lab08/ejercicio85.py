import cv2
image = cv2.imread('../images/basketball.jpg')
#--Haga una copia de esta imagen y guárdela en otra variable
imageCopy= image.copy()
cv2.imshow('imagen BGR', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Convierta la imagen a escala de grises y visualice
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Convierta esta imagen en escala de grises en una imagen binaria utilizando un umbral 
# tal que toda la región del límite blanco de la red de baloncesto se detecte como una sola mancha:
ret,binary_im = cv2.threshold(gray_image,100, 255, cv2.THRESH_BINARY)
cv2.imshow('Binario', binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Detecta todos los contornos
contours,hierarchy = cv2.findContours(binary_im, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#--Dibuje todos los contornos detectados en la imagen y luego muestre la imagen. 
contours_to_plot= -1
plotting_color= (0,255,0) #--verde
# si queremos rellenar con color los contornos dibujados
thickness= -1
with_contours = cv2.drawContours(image,contours, contours_to_plot, plotting_color,thickness)
cv2.imshow('Contornos', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--A continuación, debemos trazar cuadros delimitadores alrededor de todos los contornos.
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    image = cv2.rectangle(image,(x,y),(x+w,y+h), (0,255,255),2)
#--mostrar la imagen
cv2.imshow('Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Encuentra el contorno con el área más grande:
required_contour = max(contours, key = cv2.contourArea)
#--Encuentre las coordenadas x e y iniciales y el ancho y alto 
# de un cuadro delimitador rectangular que debe encerrar este contorno más grande
x,y,w,h = cv2.boundingRect(required_contour)
#--Dibuje este cuadro delimitador en una copia de la imagen en color original 
# que había guardado anteriormente:
img_copy2 = cv2.rectangle(imageCopy, (x,y),(x+w, y+h), (0,255,255),2)
#--mostrar el resultado
cv2.imshow('Contorno más grande', img_copy2)
cv2.waitKey(0)
cv2.destroyAllWindows()