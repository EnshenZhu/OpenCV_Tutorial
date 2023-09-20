import cv2 as cv

img = cv.imread('../Photos/dota_silencer.jpg')
cv.imshow('Silencer', img)

"""5. Resize and crop images"""
# """A. Resize"""
# resized = cv.resize(img, (500, 500))  # resize the image and ignore the aspect ratio
# cv.imshow("Resized", resized)
#
# """
# interpolation=cv.INTER_AREA
# is mostly for shrinking the image
# """
# # a. interpolation=cv.INTER_AREA
# resized_INTER_AREA = cv.resize(img, (500, 500),
#                                interpolation=cv.INTER_AREA)
# cv.imshow("Resized_inter_area", resized_INTER_AREA)
#
# """interpolation=cv.INTER_LINEAR and interpolation=cv.INTER_CUBIC are mostly for enlarge the image; INTER_CUBIC is a
# slower process but have higher quality than the INTER_CUBIC"""
#
# # b. interpolation=cv.INTER_LINEAR
# resized_INTER_LINEAR = cv.resize(img, (500, 500),
#                                  interpolation=cv.INTER_LINEAR)
# cv.imshow("Resized_inter_linear", resized_INTER_LINEAR)
#
# # c. interpolation=cv.INTER_CUBIC
# resized_INTER_CUBLIC = cv.resize(img, (500, 500),
#                                  interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized_inter_cubic", resized_INTER_CUBLIC)

"""B. Cropping"""
# consider the image as an array and conduct array slicing
cropped = img[50:200, 20:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
