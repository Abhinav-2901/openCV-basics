import cv2
import numpy as np

img = cv2.imread('cards.png')


width, height = 250,350
pts1 = np.float32([[1327,140],[2449,442],[901,1701],[2028,2012]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

imgResize = cv2.resize(img, (600,400))


cv2.imshow("Image", img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)
