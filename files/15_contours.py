import cv2
import numpy as np

image=cv2.imread('images/contour.jpg')
cv2.imshow('original',image)
cv2.waitKey()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,30,200)
cv2.imshow('canny edges',edged)
cv2.waitKey()

_,contours,_=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('canny edges after contouring',edged)
cv2.waitKey()
print(contours)
print('no of contours found ' + str(len(contours)) )

cv2.drawContours(image,contours,-1,(0,255,0),3)

cv2.imshow('contours',image)
cv2.waitKey()
cv2.destroyAllWindows()
