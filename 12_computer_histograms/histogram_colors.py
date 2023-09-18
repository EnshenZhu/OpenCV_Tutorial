import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/fengshen.jpg')
cv.imshow('Fengshen', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# circle = cv.circle(blank.copy(), center=(img.shape[1] // 2, img.shape[0] // 2), radius=100, color=255, thickness=-1)
# # cv.imshow('Circle', circle)
#
# mask = cv.bitwise_and(img, img, mask=circle)
# cv.imshow('Mask', mask)

"""Color histogram"""
plt.figure()
plt.title('Colors Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)