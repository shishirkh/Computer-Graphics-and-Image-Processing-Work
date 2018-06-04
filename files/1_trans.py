import cv2
import numpy as np
s=4
image=cv2.imread('Untitled.png')
print(image)

height,width=image.shape[:2]

quarter_height,quarter_width=height/4,width/4
T=np.float32( 
            [ 
              [1,0,quarter_width] ,
              [0,1,quarter_height] 
            ]
            )
img_translation=cv2.warpAffine(image,T,(width,height))
cv2.imshow('translation',img_translation)
cv2.waitKey()
cv2.destroyAllWindows()
