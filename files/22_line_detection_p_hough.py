import cv2
import numpy as np

image=cv2.imread('images/suduku1.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,100,170,apertureSize=3)

lines=cv2.HoughLinesP(edges,1,np.pi/180,10,5,10)
print(lines.shape)

for (x1,y1,x2,y2) in lines[0]:
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),3)
cv2.imshow('p hough lines',image)
cv2.waitKey()
cv2.destroyAllWindows()
