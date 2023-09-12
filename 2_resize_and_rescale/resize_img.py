import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # It works for Images, Videos and Live Videos
    """
    frame.shape[1] -> original width of the image
    frame.shape[0] -> original height of the image
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('../Photos/roshan.jpeg')
resized_img = rescaleFrame(img, scale=0.3)

cv.imshow('Cat', img)
cv.imshow('Resized_cat', resized_img)

cv.waitKey(0)
