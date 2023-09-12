import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')  # shape(height,width,num_of_color_channels)
cv.imshow('Blank', blank)

"""2. Draw a rectangle"""
# # Draw a hollow rectangle
# cv.rectangle(blank, pt1=(0, 0), pt2=(250, 500), color=(0, 250, 0), thickness=2)  # thickness->border thickness
# cv.imshow("Green Rectangle", blank)
#
# # Draw a filled rectangle
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.rectangle(blank, pt1=(0, 0), pt2=(250, 500), color=(0, 250, 0), thickness=cv.FILLED)  # thickness=cv.FILLED
# cv.imshow("Green Rectangle Filled", blank)
#
# # Alternative way to fill the rectangle
# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.rectangle(blank, pt1=(0, 0), pt2=(250, 500), color=(0, 250, 0), thickness=-1)  # thickness=-1
# cv.imshow("Green Rectangle Filled 2", blank)

# Draw a filled square
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank, pt1=(0, 0), pt2=(blank.shape[1] // 2, blank.shape[0] // 2), color=(0, 250, 0),
             thickness=-1)  # Recall: blank.shape[1]->img width | blank.shape[0]->img height
cv.imshow("Green Rectangle Filled 2", blank)

cv.waitKey(0)
