import cv2

import numpy as np

image = cv2.imread("../Images/shapes.png")


image_copy = image.copy()

#Step 1: Convert the Image into Gray Scale

image_grayscale = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY)

# Step 2: Apply Canny Edge Detector to Detect the edges

lower_threshold = 100

upper_threshold = 150

canny_edge = cv2.Canny(image_grayscale, lower_threshold, upper_threshold)

# Step 3: Find the contours

contours, hirearchy = cv2.findContours(canny_edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Step 4: Find the length of the Contours

print(f"Length of the contours = {str(len(contours))}")

for cnt in contours:

    area = cv2.contourArea(cnt)

    print("Area for each of the contours", area)

    # Step 5: Draw the contours

    cv2.drawContours( image_copy, cnt,-1, (0, 255, 0), 3)

    # Step 6: finde the arc lenght of our contours

    peri = cv2.arcLength(cnt, True)

    # Step 7: Finde the corner points for each of the shape in the image 

    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)

    # Step 8: Lenght of the corner points for each of the shape in the image

    print("Length of the corner points", len(approx))

    objcor = len(approx)

    # Step 9: Draw Bounding Boxes around each of the shape in the image

    x, y, w, h= cv2. boundingRect(approx)

    cv2.rectangle(image_copy, (x,y), (x+w,y+h), (0, 0, 255), 2)

    if objcor == 3:
        object_type = "Tri"

    elif  objcor == 4:
        aspect_ratio = w/float(h)
        if aspect_ratio > 0.98 and aspect_ratio  < 1.03:
            object_type = "Square"
        else:
            object_type="Rectangle"
    elif objcor > 4:
        object_type = "Circle"
    else:
        object_type="None"

    cv2.putText(image_copy, object_type, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7, (255,144,30),2 )


cv2.imshow("Original Image", image)

cv2.imshow("Gray Scale Image", image_grayscale)

cv2.imshow("Edge detector", canny_edge)

cv2.imshow("Final output image", image_copy)

cv2.waitKey(0)