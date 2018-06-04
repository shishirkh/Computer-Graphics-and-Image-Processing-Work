import cv2
import numpy as np

image=cv2.imread('images/cont.jpg')
cv2.imshow('original',image)
cv2.waitKey()

height,width=image.shape[:2]

blank_image=np.zeros( (height,width , 3) )

original_image=image

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged=cv2.Canny(gray,50,200)
cv2.imshow('canny edges',edged)
cv2.waitKey()

_,contours,_=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print('no of contours found ' + str(len(contours)) )

cv2.drawContours(blank_image,contours,-1,(0,255,0),3)
cv2.imshow('all contours over black bg',blank_image)
cv2.waitKey()

cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('all contours over original bg',image)
cv2.waitKey()

sorted_contours=sorted(contours,key=cv2.contourArea,reverse=True)

for c in sorted_contours:
    cv2.drawContours(original_image,[c],-1,(255,0,0),3)
    cv2.waitKey()
    cv2.imshow('contours by size',original_image)

cv2.waitKey()    
cv2.destroyAllWindows()
