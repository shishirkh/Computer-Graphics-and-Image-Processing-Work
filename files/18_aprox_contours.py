import cv2
import numpy as np

image1=cv2.imread('images/house.jpg')
image2=image1
height,width=image1.shape[:2]
gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(gray,50,200)
_,contours,_=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h=cv2.boundingRect(c)
    cv2.rectangle(image1,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('bounding rect',image1)
cv2.waitKey()    

for c in contours:
    accuracy=0.003*cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,accuracy,True)
    cv2.drawContours(image2,[approx],0,(0,255,0),2)
    cv2.imshow('approx poly DP',image2)
    
cv2.waitKey()
cv2.destroyAllWindows()

cv2.destroyAllWindows()
