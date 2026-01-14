import cv2

import numpy as np

#this is a gray scale image because we have only 512 x512 pixels or boxes


# If we want to add the color functionality , we have to give it the channels


image = np.zeros((512, 512, 3))

# add color

image[:] = 255, 0 , 0 

#drawing a line 

cv2.line(image, (0,0) ,(image.shape[1], image.shape[0]), (0,255,0) , 3 )

cv2.rectangle(image, (0,0) , (250, 350), (0,0,255), 3)#cv2.FILLED)

# Draw a circle

cv2.circle(image, (400,50), 30,(0,255,255), -1)

# Draw text on an image

cv2.putText(image, "OpenCV", (300,100), cv2.FONT_HERSHEY_SIMPLEX, 2 , (0, 150, 0), 5)


cv2.imshow("Ouput Image", image)

cv2.waitKey(0)