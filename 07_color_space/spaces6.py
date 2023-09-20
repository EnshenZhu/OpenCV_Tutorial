import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

# BGR to HSV
hsv = cv.cvtColor(img, code=cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# BGR to LAB
lab = cv.cvtColor(img, code=cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)
