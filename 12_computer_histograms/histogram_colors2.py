import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Photos/fengshen.jpg')
cv.imshow('Fengshen', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank.copy(), center=(img.shape[1] // 2, img.shape[0] // 2), radius=100, color=255, thickness=-1)
# cv.imshow('Circle', circle)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked_img)

"""Color histogram with circle mask"""
plt.figure()
plt.title('Colors Histogram with the Circle Mask')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], channels=[i], mask=mask, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
