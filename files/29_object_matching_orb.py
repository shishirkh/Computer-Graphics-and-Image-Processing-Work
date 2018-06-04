import numpy as np
import cv2

def orb_detector(new_image,image2):
    image1=cv2.cvtColor(new_image,cv2.COLOR_BGR2GRAY)
    
    orb=cv2.ORB_create(1000,1.2)
    
    (kp1,des1)=orb.detectAndCompute(image1,None)
    (kp2,des2)=orb.detectAndCompute(image2,None)
    
    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches=bf.match(des1,des2)
    matches=sorted(matches,key=lambda val:val.distance)
    return (len(matches))
    
    
cap=cv2.VideoCapture(0)
image_template=cv2.imread('images/phone_front.jpg')
image_template=cv2.cvtColor(image_template,cv2.COLOR_BGR2GRAY)

while True:
    _,frame=cap.read()
    
    height,width=frame.shape[:2]


    top_left_x=int(width/3)
    top_left_y=int(height/3)
    bottom_right_x=int((width/3)*2)
    bottom_right_y=int((height/2)-(height/4))
    
    cv2.rectangle(frame,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(0,255,0),2)
    
    cropped=frame[bottom_right_y:top_left_y,top_left_x:bottom_right_x]
    frame=cv2.flip(frame,1)

    matches=orb_detector(cropped,image_template)
    cv2.putText(frame,str(matches),(450,450),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
    
    threshold=350
    if(matches>threshold):
        cv2.rectangle(frame,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(0,0,255),3)
        cv2.putText(frame,'object found',(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
    cv2.imshow('object detection using sift',frame)
    if cv2.waitKey():
        break
cap.release()
cv2.destroyAllWindows()


    
    