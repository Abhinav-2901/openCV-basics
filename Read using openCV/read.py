import cv2


# Read Image
"""img = cv2.imread('Abhinav.jpg')
cv2.imshow('Abhinav', img)
cv2.waitKey(0)"""

# Read Video

"""cap = cv2.VideoCapture('test.mp4')

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break"""
        
# Read Camera

"""cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success , img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break"""
