# importing necessary libraries
import cv2
import numpy as np

# Read the image
image = cv2.imread('laser.jpg')

# Convert the image to grayscale for better detection 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold or edge detection (e.g., Canny)
_, binary = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

# Finding contours
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

# showing output
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
