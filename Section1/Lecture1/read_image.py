# Import the Required Library
import cv2

# To read the image I will use imread function

image = cv2.imread("../Images/face.png")

# Display the Output Image

cv2.imshow("Output", image)

cv2.waitKey(0)