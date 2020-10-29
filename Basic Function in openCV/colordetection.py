import cv2
import numpy as np

def empty(a):
    pass

# Importing the image

path = 'lambo.png'

# Creating Trackbar for all 6 values

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBard", 240, 640)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# Creating while loop

while True:

    # Resizing image
    
    img = cv2.imread(path)
    imgResize = cv2.resize(img, (600,270))
    
    # Converting image to HSV
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgHSV = cv2.resize(imgHSV, (600,270))
    
    # Catching Trackbar values of all 6
    
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    
    # Creating Mask
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    #Get Result
    
    imgResult = cv2.bitwise_and(imgResize, imgResize, mask=mask)
    
    
    
    cv2.imshow('Orgignal', imgResize)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', imgResult)
    cv2.waitKey(1)