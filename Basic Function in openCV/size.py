import cv2
import numpy as np

# Resizing Image

img = cv2.imread('Abhinav.jpg')
print(img.shape)

imgResize = cv2.resize(img, (600,400))
print(imgResize.shape)



#Cropping Image

imgCropped = img[0:500, 200:800]
cv2.imshow('Image Cropped', imgCropped)
cv2.imshow('Image', img)
cv2.imshow('Image Resize', imgResize)
cv2.waitKey(0)
