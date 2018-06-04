import cv2
import numpy as np
template=cv2.imread('images/template.jpg')
cv2.imshow('template',template)
cv2.waitKey()
sample=cv2.imread('images/sample.jpg')
cv2.imshow('sample',sample)
cv2.waitKey()
cv2.destroyAllWindows()


edged1=cv2.Canny(template,127,255)
_,contours1,_=cv2.findContours(edged1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

sorted_contours=sorted(contours1,key=cv2.contourArea,reverse=True)

template_contour=sorted_contours[0]

edged2=cv2.Canny(sample,127,255)
_,contours2,_=cv2.findContours(edged2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print('length of contours 2 '+str(len(contours2)))

closest_matches=[]
for c in contours2:
    match=cv2.matchShapes(template_contour,c,1,0.0)
    print(match)
    if(match<0.07):
        closest_matches.append(c)
     

for c in closest_matches:
    cv2.drawContours(sample,[c],-1,(0,255,0),3)
    cv2.imshow('output',sample)
    cv2.waitKey()
    
cv2.destroyAllWindows()

