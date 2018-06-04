import cv2
import numpy as np

image=cv2.imread('images/hands.jpg')
gray=cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(image,176,255,0)
edged=cv2.Canny(thresh,50,200)
_,contours,_=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
N
n=len(contours)-1
contours=sorted(contours,key=cv2.contourArea,reverse=False)
for c in contours:
    hull=cv2.convexHull(c)
    cv2.drawContours(image,[hull],0,(0,255,0),2)
    cv2.imshow('convex hull',image)
    
cv2.waitKey()
cv2.destroyAllWindows()