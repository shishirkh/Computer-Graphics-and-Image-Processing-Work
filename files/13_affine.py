import cv2
import numpy as np

image=cv2.imread('images/try123_b.jpg')

points_A=np.float32( [ [427,337] ,
                       [932,331] ,
                       [415,709] ,
                       [983,709] 
                     ] )

points_B=np.float32( [ [0,0] ,
                       [400,0] ,
                       [0,400] ,
                       [400,400] 
                     ] )

M=cv2.getPerspectiveTransform(points_A,points_B)
warped=cv2.warpPerspective(image,M,(400,400))

cv2.imshow('original',image)
cv2.waitKey()
cv2.imshow('warpPerspective',warped)
cv2.waitKey()
cv2.destroyAllWindows()


