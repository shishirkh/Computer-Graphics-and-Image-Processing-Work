import cv2
import numpy as np

image=cv2.imread('try123.jpg')

smaller=cv2.pyrDown(image)
larger=cv2.pyrUp(image)

#cv2.imshow('original',image)
#cv2.imshow('original',smaller)
cv2.imshow('original',larger)

cv2.waitKey()
cv2.destroyAllWindows()
