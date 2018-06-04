import cv2
import numpy as np

image=cv2.imread('try123.jpg')

height,width=image.shape[:2]
start_row,start_col=int(height*0.25),int(width*0.25)
end_row,end_col=int(height*0.75),int(width*0.75)

cropped=image[start_row:end_row,start_col:end_col]

cv2.imshow('s',image)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('s',cropped)
cv2.waitKey()
cv2.destroyAllWindows()

