import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# BGR to HSV
hsv = cv.cvtColor(img, code=cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

cv.waitKey(0)
