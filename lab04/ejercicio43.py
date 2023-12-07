import cv2
import matplotlib.pyplot as plt
#--leer la imagen
img= cv2.imread('../images/sunflower.jpg')
cv2.imshow("color image",img)

im= img[:, :, 2]
plt.hist(im.ravel(), bins = 256, color = 'Red', alpha = 1.0)
im= img[:, :, 1]
plt.hist(im.ravel(), bins = 256, color = 'Green', alpha = 0.5)
im= img[:, :, 0]
plt.hist(im.ravel(), bins = 256, color = 'Blue', alpha = 0.5)
plt.show()
#--esperar
cv2.waitKey(0)
cv2.destroyAllWindows()
