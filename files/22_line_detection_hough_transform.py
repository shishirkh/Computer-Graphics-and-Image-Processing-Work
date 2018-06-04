import cv2
import numpy as np

image=cv2.imread('images/suduku.jpg')
cv2.imshow('before canny',image)
cv2.waitKey()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,30,255)

cv2.imshow('after canny',edges)
cv2.waitKey()

lines=cv2.HoughLines(edges,1,np.pi/180,20)

for rho,theta in lines[0]:
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+2000*(-b))
    y1=int(y0+2000*(a))
    x2=int(x0-2000*(-b))
    y2=int(y0-2000*(a))
    cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2)
    
cv2.imshow('hough lines',image)
cv2.waitKey()
cv2.destroyAllWindows()
