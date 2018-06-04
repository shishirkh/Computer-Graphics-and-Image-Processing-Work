import cv2
import numpy as np

image=cv2.imread('images/try123_b.jpg')
height,width=image.shape[:2]

# S O B E L
sobel_x=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobel_y=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobel_or=cv2.bitwise_or(sobel_x,sobel_y)

cv2.imshow('original',image)
cv2.waitKey()
cv2.imshow('SOBEL horizontal',sobel_x)
cv2.waitKey()
cv2.imshow('SOBEL vertical',sobel_y)
cv2.waitKey()
cv2.imshow('sobel_or',sobel_or)
cv2.waitKey()
cv2.destroyAllWindows()

# L A P L A C I A N
laplacian = cv2.Laplacian(image,cv2.CV_64F)
cv2.imshow('laplacian',laplacian)
cv2.waitKey()
cv2.destroyAllWindows()

# C A N N Y
canny = cv2.Canny(image,20,170)
cv2.imshow('canny',canny)
cv2.waitKey()
cv2.destroyAllWindows()
