import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# BGR to LAB (L*a*b)
lab = cv.cvtColor(img, code=cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

cv.waitKey(0)
