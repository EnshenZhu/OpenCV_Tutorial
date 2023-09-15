# OpenCV_Tutorial

This tutorial is developed from the
freeCodeCamp.org OpenCV Tutorial

https://youtu.be/oXlwWbU8l2o?si=53PRghV4ch3mmd2g

## What you will learn

### Basic

1. Reading Images and Video
2. Image Transformations
3. Drawing Shapes
4. Putting Text

### Advanced

1. Color Spaces
2. BITWISE operations
3. Masking
4. Histogram Computation
5. Edge Detection and Thresholding

### Faces:

1. Face Detection
2. Face Recognition
3. Deep Computer Vision (Classify the Simpsons)

## What is Computer Vision

A computer vision is an application of deep
earning that primarily focuses on deriving
insights from media files (images and videos).

## What is OpenCV

It is a computer vision library that is available
in Python, C++ and Java.

## Install the OpenCV library

### OpenCV

1. Open the terminal
2. ```pip install opencv-contrib-python```
3. This library includes the **main model** and the **contribution module** of the OpenCV library
4. The OpenCV library installation will also install the **numpy package** (for scientific computing).

### Caer

1. ```pip install caer```
2. This is the package to help speed up the workflow with a set of utility functions.

## Basics

### Reading Images & Video

import the library ```import cv2 as cv```

1. Read images
    * read the image file ```cv.imready(<file_path>)```
    * display the image ```cv.imshow(<display_window_name>,<img_file_variable>)```
    * OpenCV does not have the in-built way for ```cv.imshow()``` to deal with the image that far bigger than the
      screen. But there are other ways to mitigate the issue.

2. Read videos
    * read the video ```cv.VideoCapture([camera_idx],<file_path>)```
    * It uses a while loop to read the video frame by frame.
    * ```(-215:Assertion failed)``` This error means that the OpenCV cannot find any more frames after finish reading
      the entire video. (In general, the OpenCV cannot find the image or the video frame)

### Resize & Rescale

We resize or rescale image or video files to **prevent computation strain**. Large media files tend to store a lot of
information in it and displaying it takes up a lot of processing needs for the computer. So resizing and rescaling can
get rid of some of that information. Rescaling video implies modifying its height and width to **a particular height and
width**.

* This can resize images, videos and live
  videos ```cv.resize(<frame variable>, <dimensions[tuple]>, interpolation=cv.INTER_AREA)```.
* This can only resize live videos ```cv.set(<propid>,<scale>)```. For the ```propid```, 3 is for the width and 4 is for
  the height.

### Drawing Shapes & Putting Text

1. Paint color
2. Draw rectangles
3. Draw circles
4. Draw lines
5. Add texts

### Five Essential Functions in OpenCV

1. Grayscale the image *(you will only see the **color intensity** instead of BGR colors)*
2. Blur the image *(remove the **noise** in the image; **noise** means some elements in the image caused by the bad
   lighting or camera sensor issues)*
3. Edge cascade *(Find the **edge** in the image)*
4. Dilate and erode the image (via structuring elements)
5. Resize and cript the image

### Image Transformations

1. Translation *(shift the image along the x and y axis)*
2. Rotation *(rotate the image by some angle)*
3. Resize
4. Flip
5. Crop

### Contour Detection

Contours are the boundary of objects. --> The line or curve that joins the continues points along the boundary of an
object. *(In mathematical scopt, contours are **NOT** same to the edges.)*

```contours, hierarchies = cv.findContours(canny, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_NONE)```

1. ```contours```--> list of all the coordinates of contours that are found in the image.
2. ```hierarchies```--> hierarchical representation of contours.
3. ```mode params```:
    * ```RETR_LIST``` returns all the contours that are found in the image
    * ```RETR_EXTERNAL``` only returns the external contour of the image
    * ```RETR_TREE``` returns all the hieratical contours in the system
4. ```method params```  --> how we want to approximate the contour
    * ```CHAIN_APPROX_NONE``` --> does nothing, just return the all the contours
    * ```CHAIN_APPROX_SIMPLE``` --> compress all contours into two end points only

You can visualize the image contour in the OpenCV *by exactly drawing the contour over the
image:* ```cd ./5_contour_dectection./contour3.py ```

**RECALL:** *In the OpenCV color system, the order of color is BGR (Blue-Green-Red)*

Try to distinguish the difference to the Canny.