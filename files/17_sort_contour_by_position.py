import cv2
import numpy as np

def x_cor_coordinate(contours):
    if(cv2.contourArea(contours) > 0):
        M=cv2.moments(contours)
        return (int(M['m10']/M['m00']))
        
image=cv2.imread('images/cont.jpg')
cv2.imshow('original image',image)
cv2.waitKey()
original_image=image
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(gray,50,200)
_,contours,_=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)    
contours_left_to_right=sorted(contours,key=x_cor_coordinate,reverse=False)
print(contours_left_to_right)

for(i,c) in enumerate(contours_left_to_right):
    cv2.drawContours(original_image,[c],-1,(0,0,255),3)
    M=cv2.moments(c)
    cx=int(M['m10']/M['m00'])
    cy=int(M['m01']/M['m00'])  
    cv2.putText(original_image,str(i+1),(cx,cy),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    cv2.imshow('image',original_image)
    cv2.waitKey()
    
    (x,y,w,h)=cv2.boundingRect(c)
    cropped_contour=original_image[y:y+h,x:x+w]
    image_name="output_shape_"+str(i+1)+".jpg"
    print(image_name)
    cv2.imwrite(image_name,cropped_contour)
    
cv2.destroyAllWindows()
