
import cv2 as cv
#leyendo la imagen cuyo ruido se eliminará usando la función imread()
imageread = cv.imread('../images/die.png')
#usando la función medianBlur() para eliminar el ruido de la imagen dada
imagenormal = cv.medianBlur(imageread, 7)
#mostrando la imagen sin ruido como la salida en la pantalla
cv.imshow('original:', imageread)
cv.imshow('imagen con ruido disminuido',imagenormal)
cv.waitKey(0)
cv.destroyAllWindows()