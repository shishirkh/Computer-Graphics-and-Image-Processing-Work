import numpy as np
import cv2

face_classifier=cv2.CascadeClassifier('images/haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('images/haarcascade_eye.xml')
 
def face_detector(img,size=0.5):
    image=img
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces=face_classifier.detectMultiScale(gray,1.3,5)

    if faces is ():
        print('no face found')
    
    for (x,y,w,h) in faces:
        x=x-50
        w=w+50
        y=y-50
        h=h+50
        
        cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=image[y:y+h,x:x+w]
        eyes=eye_classifier.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    roi_color=cv2.flip(roi_color,1)
    return roi_color

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('our face extractor',face_detector(frame))
    if cv2.waitKey():
        break
    

cap.release()
cv2.destroyAllWindows()


    
    