import cv2
import numpy as np

img = cv2.imread('Abhinav.jpg')

# Functions

# 1 - Convert into Gray scale

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', imgGray)
cv2.waitKey(0)

# 2 - Blur Image using Gaussian Blur

imgBlur = cv2.GaussianBlur(imgGray,(21,21),0)
cv2.imshow('Blur Image', imgBlur)
cv2.waitKey(0)

# 3 - Edge Detector

imgCanny = cv2.Canny(img, 150, 200)
cv2.imshow('Canny Image', imgCanny)
cv2.waitKey(0)

# Dialation (Make Edges Thick)

kernel = np.ones((5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow('Dialation Image', imgDialation)
cv2.waitKey(0)

# Erode (Make edges Thin)

imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow('Erosion', imgEroded)
cv2.waitKey(0)




