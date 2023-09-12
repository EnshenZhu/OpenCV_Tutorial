import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""3. Edge Cascade (by Canny edge detection)"""
canny = cv.Canny(img, threshold1=125, threshold2=175)
cv.imshow('Canny', canny)

# We can reduce the edges by blurring the image
blur = cv.GaussianBlur(img, ksize=(7, 7), sigmaX=cv.BORDER_DEFAULT)  # to blur the image
canny_blur = cv.Canny(blur, threshold1=125, threshold2=175)
cv.imshow('Canny_blur', canny_blur)

cv.waitKey(0)
