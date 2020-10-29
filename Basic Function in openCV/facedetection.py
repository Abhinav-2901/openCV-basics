import cv2
import numpy as np

path = 'Abhinav2.jpg'

# Importing the cascade xmlfile

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Importing the image and converting it into grayimage

img = cv2.imread(path)
#img = cv2.resize(img, (600,600))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting the faces using cascade files and iterating overall faces find

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y , w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    
#Visualising the result

cv2.imshow("Image", img)
cv2.waitKey(0)


