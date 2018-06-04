import cv2
import numpy as np

image=cv2.imread('images/text.jpg')
cv2.imshow('original',image)
cv2.waitKey()

kernel=np.ones( (5,5) , np.uint8 )

#EROSION
erosion=cv2.erode(image,kernel,iterations=1)
cv2.imshow('erosion',erosion)
cv2.waitKey()

#DILATION
dilation=cv2.dilate(image,kernel,iterations=1)
cv2.imshow('dilation',dilation)
cv2.waitKey()

#OPENING : erosion followed by dilatio
opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)
cv2.waitKey()

#CLOSING : dilation followed by erosion
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)
cv2.waitKey()

cv2.destroyAllWindows()

