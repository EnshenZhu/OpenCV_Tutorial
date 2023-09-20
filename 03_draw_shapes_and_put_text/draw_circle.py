import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # shape(height,width,num_of_color_channels)
cv.imshow('Blank', blank)

"""3. Draw a circle"""
# Draw a red circle centered at the middle of the img with a radius of 40
cv.circle(blank, center=(blank.shape[1] // 2, blank.shape[0] // 2), radius=40, color=(0, 0, 255), thickness=3)
cv.imshow("Red Circle", blank)

# Draw a red circle centered at the middle of the img with a radius of 40
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.circle(blank, center=(blank.shape[1] // 2, blank.shape[0] // 2), radius=40, color=(0, 0, 255), thickness=-1)
cv.imshow("Red Circle Filled", blank)

cv.waitKey(0)
