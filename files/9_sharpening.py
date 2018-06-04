import cv2
import numpy as np

image=cv2.imread('images/try123.jpg')
cv2.imshow('original',image)
cv2.waitKey()
cv2.destroyAllWindows()

sharpening_kernel=np.array( [
                             [-1,-1,-1],
                             [-1,9,-1],
                             [-1,-1,-1]
                             ])
sharpened=cv2.filter2D(image,-1,sharpening_kernel)
cv2.imshow('image sharpening',sharpened)
cv2.waitKey()
cv2.destroyAllWindows()
