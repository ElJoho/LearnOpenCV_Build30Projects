import cv2

image = cv2.imread("../../Images/image.jpg")

# --> 1000 ---> Resize image width
# --> 650 ---> Resize image height

image_resize = cv2.resize(image, (1000, 650) )
print("Resize Image Shape", image_resize.shape)

cv2.imshow("Original Image", image)

cv2.imshow("Resize Image", image_resize)

cv2.waitKey(0)