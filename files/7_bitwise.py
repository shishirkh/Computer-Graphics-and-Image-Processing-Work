import cv2
import numpy as np

square=np.zeros( (300,300) , np.uint8 )
cv2.rectangle( square, (50,50) ,(250,250),255,-2 )
cv2.imshow("square",square)
cv2.waitKey()
cv2.destroyAllWindows()

ellipse=np.zeros( (300,300) , np.uint8 )
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",ellipse)
cv2.waitKey()
cv2.destroyAllWindows()

And=cv2.bitwise_and(square,ellipse)
cv2.imshow("and",And)
cv2.waitKey()
cv2.destroyAllWindows()

Or=cv2.bitwise_or(square,ellipse)
cv2.imshow("Or",Or)
cv2.waitKey()
cv2.destroyAllWindows()

Xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow("Xor",Xor)
cv2.waitKey()
cv2.destroyAllWindows()

Not_square=cv2.bitwise_not(square)
cv2.imshow("Not",Not_square)
cv2.waitKey()
cv2.destroyAllWindows()

Not_ellipse=cv2.bitwise_not(ellipse)
cv2.imshow("Not",Not_ellipse)
cv2.waitKey()
cv2.destroyAllWindows()

