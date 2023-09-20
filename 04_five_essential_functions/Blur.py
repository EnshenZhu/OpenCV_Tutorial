import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""2. Blur the image (by Gaussian Blur)"""
blur = cv.GaussianBlur(img, ksize=(3, 3), sigmaX=cv.BORDER_DEFAULT)
# ksize -> kernel size (aka. 卷积核，其必须为奇数行列的n*n矩阵)
cv.imshow('Blur', blur)

# increasing the blur
increaded_blur = cv.GaussianBlur(img, ksize=(7, 7), sigmaX=cv.BORDER_DEFAULT)
cv.imshow('Increased Blur', increaded_blur)

cv.waitKey(0)
