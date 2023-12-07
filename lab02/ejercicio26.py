import cv2 as cv
import numpy as np
def color_space_demo (imagen): # conversión de color
    #Convertir a escala de grises
    gray = cv.cvtColor (imagen, cv.COLOR_BGR2GRAY) 
    cv.imshow("gray", gray)
    #Convertir imagen en formato HSV
    hsv = cv.cvtColor (imagen, cv.COLOR_BGR2HSV) 
    cv.imshow("hsv", hsv) 
    #Convertir imagen en formato YUV (más común)
    yuv = cv.cvtColor (imagen, cv.COLOR_BGR2YUV) 
    cv.imshow("yuv", yuv)
    #Convertir imagen en formato Ycrcb
    Ycrcb = cv.cvtColor (imagen, cv.COLOR_BGR2YCrCb) 
    cv.imshow("ycrcb", Ycrcb)
    #Convertir imagen en formato Ycrcb
    XYZ= cv.cvtColor(imagen, cv.COLOR_BGR2XYZ)
    cv.imshow("xyz", XYZ)

src = cv.imread("../images/lena.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
color_space_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
