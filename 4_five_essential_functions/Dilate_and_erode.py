import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""4. Dilating and erode images"""

# turn the image into wireframes previously
canny = cv.Canny(img, threshold1=125, threshold2=175)
cv.imshow('Canny', canny)

dilate = cv.dilate(canny, kernel=(7, 7), iterations=3)
cv.imshow('Dilated', dilate)

# Erode dilated image to get back to the structured elements
eroded = cv.erode(dilate, kernel=(7, 7), iterations=3)
cv.imshow('Eroded', eroded)

cv.waitKey(0)
