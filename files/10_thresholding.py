import cv2
import numpy as np

image=cv2.imread('images/img.jpg')
cv2.imshow('original',image)
cv2.waitKey()

#THRESHOLD BINARY
ret,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imshow('1 threshold binary',thresh1)
cv2.waitKey()
#cv2.destroyAllWindows()

#THRESHHOLD BINARY INVERSE
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('2 threshold binary inverse',thresh2)
cv2.waitKey()

#values above 127 are truncated at 127
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow('3 threshold truncate',thresh3)
cv2.waitKey()

#value below 127 are assigned 0 rest are unchanged
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow('4 threshold to zero',thresh4)
cv2.waitKey()

ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('5 threshold to zero inverse',thresh5)
cv2.waitKey()

cv2.destroyAllWindows()

#ADAPTIVE MEAN THRESHOLDING


                          
