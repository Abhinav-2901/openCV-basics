import cv2
import numpy as np

img = cv2.imread('Abhinav.jpg')
img = cv2.resize(img, (200,200))

imgHor = np.hstack((img,img,img))
imgVer = np.vstack((img,img,img))

cv2.imshow('Horzontal',imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0)