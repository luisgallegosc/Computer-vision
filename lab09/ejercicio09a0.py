import numpy as np
import cv2 as cv
img = cv.imread('../images/waffle.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#el resultado es dilatado para marcar las esquinas 
dst = cv.dilate(dst,None)

# el umbral optimo puede variar dependiendo de la imagen
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
 cv.destroyAllWindows()