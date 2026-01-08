import cv2

image = cv2.imread("../Images/documentscanner2.jpg")

# Setting the threshold values

t_lower = 100

t_higher = 120 # Al incrementar el numero de contornos se reducen

# Apply Canny Edge Detector

edge = cv2.Canny(image , t_lower, t_higher)

cv2.imshow("Original Image", image)

cv2.imshow("Canny Image ", edge)

cv2.waitKey(0)