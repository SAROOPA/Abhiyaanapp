import cv2 as cv
import numpy as np

# Reading the original image
image = cv.imread("photos/abhiyaan_opencv_qn1.png")
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Reading the target image(obstacle)
target = cv.imread("photos/crop.png")
hsvt = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# Histogram and Backprojection
hist = cv.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])
backProj = cv.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)

# Filtering 
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
fil = cv.filter2D(backProj, -1, kernel)
threshold, result = cv.threshold(fil, 50, 255, cv.THRESH_BINARY)

# Finding contours
contours, hier = cv.findContours(result, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for c in contours:
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.imshow("Original image", image)
cv.waitKey(0)