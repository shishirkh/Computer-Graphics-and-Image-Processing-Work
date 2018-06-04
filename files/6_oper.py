import cv2
import numpy as np

image=cv2.imread('try123.jpg')

M=np.ones(image.shape,dtype="uint8")*55
print(M)

added=cv2.add(image,M)
cv2.imshow("Added",added)

subtracted=cv2.subtract(image,M)
cv2.imshow("subtracted",subtracted)

cv2.waitKey()
cv2.destroyAllWindows()
