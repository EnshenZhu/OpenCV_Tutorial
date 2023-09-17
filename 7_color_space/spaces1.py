import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# BGR to Grayscale
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

cv.waitKey(0)
