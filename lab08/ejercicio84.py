import cv2
image_3chan = cv2.imread('../images/nut_bolt.png')
image_3chan_copy= image_3chan.copy()
cv2.imshow('Imagen Original', image_3chan)
cv2.waitKey(0)
cv2.destroyAllWindows()
gray_image = cv2.cvtColor(image_3chan, cv2.COLOR_BGR2GRAY)
ret,binary_im = cv2.threshold(gray_image,250,255,cv2.THRESH_BINARY)
cv2.imshow('Imagen Binaria', binary_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours_list,hierarchy = cv2.findContours(binary_im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print('Información de jerarquía de todos los contornos:')
print (hierarchy)
for i in range(0, len(contours_list)):
    contour_info= hierarchy[0][i, :]
    print('Información de jerarquía del contorno actual:')
    print(contour_info)
    # no parent, no child
    if contour_info[2]==-1 and contour_info[3]==-1:
        with_contours = cv2.drawContours(image_3chan_copy, contours_list,i,[0,255,0],thickness=3)
        print('Se detecta el contorno del perno')
    if contour_info[2]==-1 and contour_info[3]!=-1:
        with_contours = cv2.drawContours(with_contours,contours_list,i,[0,0,255],thickness=3)
        print('Se detecta un agujero de tuerca')

cv2.imshow('Contornos marcados en la imagen RGB', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()