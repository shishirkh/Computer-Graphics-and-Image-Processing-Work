import cv2
import numpy as np

image=cv2.imread('images/try123.jpg')
cv2.imshow('original',image)
cv2.waitKey()
cv2.destroyAllWindows()

kernel_3by3=np.ones( (3,3) , np.float32)/9

blurred=cv2.filter2D(image,-1,kernel_3by3)
cv2.imshow("blurred by 3 by 3",blurred)
cv2.waitKey()
cv2.destroyAllWindows()


kernel_7by7=np.ones( (7,7) , np.float32)/49

blurred_1=cv2.filter2D(image,-1,kernel_7by7)
cv2.imshow("blurred by 7 by 7",blurred_1)
cv2.waitKey()
cv2.destroyAllWindows()

#BOX BLURRING:CENTRAL ELEMENT IS REPLACES BY THE AVERAGES
blur=cv2.blur(image,(3,3))
cv2.imshow('averaging : box blurring',blur)
cv2.waitKey(0)

#GAUSSIAN BLURRING USING GAUSSIAN FILTER
Gaussian=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("gaussian blurring",Gaussian)
cv2.waitKey(0)

#MEDIAN BLURRING:central element is replaced by median of all elements
median=cv2.medianBlur(image,5)
cv2.imshow('median bluring',median)
cv2.waitKey(0)

bilateral=cv2.bilateralFilter(image,9,75,75)
cv2.imshow("bilateral blurring",bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

####image denoising : non local means denoising
#dst=cv2.fastN1MeansDenoisingColored(image,None,6,6,7,21)
#cv2.imshow('fast means denoising',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

