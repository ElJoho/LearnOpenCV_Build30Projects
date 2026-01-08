import cv2
import numpy as np

image = cv2.imread("../Images/documentscanner2.jpg")

kernel = np.ones((5,5), np.uint8)


# Setting the threshold values

t_lower = 100

t_higher = 120 # Al incrementar el numero de contornos se reducen

# Apply Canny Edge Detector

imgCanny = cv2.Canny(image , t_lower, t_higher)

# Dialation of Image

imageDilation = cv2.dilate(imgCanny, kernel, iterations = 1)


cv2.imshow("Original Image", image)

cv2.imshow("Canny Image ", imgCanny)

cv2.imshow("Image Dilation", imageDilation)

cv2.waitKey(0)