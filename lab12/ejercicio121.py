from skimage import feature
import cv2
import matplotlib.pyplot as plt
 
image = cv2.imread('../images/flower.jpg')
(hog, hog_image) =  feature.hog(image, orientations=9,
                    pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                    block_norm='L2-Hys', visualize=True, transform_sqrt=True,channel_axis=-1)
 
cv2.imshow('HOG Image', hog_image)
cv2.imwrite('hog_flower.jpg', hog_image*255.)
cv2.waitKey(0)
