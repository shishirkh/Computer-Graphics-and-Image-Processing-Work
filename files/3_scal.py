import cv2
import numpy as np

image=cv2.imread('try123.jpg')
print(image)

image_scaled=cv2.resize(image,None,fx=0.75,fy=0.75)
cv2.imshow('scaling-linear interpolation',image_scaled)
cv2.waitKey()

image_scaled=cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('scaling-cubic interpolation',image_scaled)
cv2.waitKey()

image_scaled=cv2.resize(image,(900,400),interpolation=cv2.INTER_AREA)
cv2.imshow('scaling-skewed size',image_scaled)
cv2.waitKey()

cv2.destroyAllWindows()
