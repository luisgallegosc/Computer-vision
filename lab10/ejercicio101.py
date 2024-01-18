import cv2
import numpy as np
from matplotlib import pyplot as plt

template = cv2.imread("template1.jpg")
template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
img = cv2.imread("image1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.imshow(template)
#--dimensiones de la plantilla
template.shape
#--lista con los nombres de diferentes métodos de coincidencia de plantillas.
methods =["cv2.TM_CCOEFF" , "cv2.TM_CCOEFF_NORMED", "cv2.TM_CCORR" , "cv2.TM_CCORR_NORMED" , "cv2.TM_SQDIFF" , "cv2.TM_SQDIFF_NORMED"]

#--obtener los resultados para cada metodo
for m in methods:
  img_copy = img.copy()
  method = eval(m)
  res = cv2.matchTemplate(img_copy,template,method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
  else:
    top_left = max_loc
  print(top_left)    

  height, width, channels = template.shape  
  bottom_right = (top_left[0]+width, top_left[1]+height)

  cv2.rectangle(img_copy, top_left, bottom_right, (0,255,0),3)

  plt.subplot(121)
  plt.imshow(res)
  plt.title("TEMPLATE MATCHING MAP")
  plt.subplot(122)
  plt.imshow(img_copy)
  plt.title("TEMPLATE DETECTION")
  plt.suptitle(m)

  plt.show()
  print("\n")
  print("\n")