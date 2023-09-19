import cv2 as cv

img = cv.imread('../Photos/group_photos/group.jpg')
cv.imshow('Group', img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Photo', gray)

haar_cascade = cv.CascadeClassifier('../haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# minNeighbors --> the number of neighbor rectangles should have to be called a face
# This function will return the rectangular coordinates of face as a list

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

cv.imshow('Faces Detected', img)

cv.waitKey(0)
