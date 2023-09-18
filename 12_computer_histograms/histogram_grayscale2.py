import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""Grayscale histogram"""
gray_hist = cv.calcHist([gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# image and channels should be lists
# histSize --> number of bins that we want ot use for computing histogram (in the list format)
# ranges --> ranges of all possible pixel values

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
