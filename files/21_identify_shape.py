import cv2
import numpy as np

image=cv2.imread('images/start.jpg')
#cv2.imshow('original image',image)
#cv2.waitKey()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray=cv2.Canny(gray,127,255)

#cv2.imshow('grayscale of image',gray)
#cv2.waitKey()

_,contours,_=cv2.findContours(gray.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

print(len(contours))

for c in contours:
    approx=cv2.approxPolyDP(c,0.1*cv2.arcLength(c,True),True)
    if(len(approx)==3):
        shape_name="triangle"
        cv2.drawContours(image,[c],0,(0,255,0),-1)
        M=cv2.moments(c)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    elif(len(approx)==4):
        x,y,w,h=cv2.boundingRect(c)
        M=cv2.moments(c)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        if( abs(w-h) <= 3 ):
            shape_name="square"
            cv2.drawContours(image,[c],0,(255,0,0),-1)
            cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
        else:
            shape_name="rectangle"
            cv2.drawContours(image,[c],0,(0,0,255),-1)
            cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    elif(len(approx)==10):
        shape_name="star"
        cv2.drawContours(image,[c],0,(255,255,0),-1)
        M=cv2.moments(c)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    elif(len(approx)>=15):
        shape_name="circle"
        cv2.drawContours(image,[c],0,(0,255,255),-1)
        M=cv2.moments(c)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.putText(image,shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
    print(shape_name)
    cv2.imshow('identifying shape',image)
    cv2.waitKey()
    
cv2.destroyAllWindows()

        
        
            