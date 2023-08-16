'''
Task 2: Align(make the rectangle image straight) all the given images of the rectangle.
'''

import cv2
import numpy as np

#loading image
image = cv2.imread('image path')

#convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Apply canny edge detection
edges = cv2.Canny(gray, threshold1=50, threshod2=150)

#find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#loop through each contours
for contour in contours:
    epsilon = 0.05 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    if len(approx) == 4:
        rect_pts = approx.reshape(4, 2) #to get the coordinates of the rectangle's vertices

        # defining the target rectangle's corners for perspective transformation
        target_pts = np.array([[0, 0], [0, 300], [300, 300], [300, 0]], dtypes=np.float32)

        # for calculating the perspective transformation matrix
        matrix = cv2.getPerspectiveTransform(rect_pts, target_pts)

        # apply the perspective transformation
        aligned_image = cv2.warPerspective(image, matrix, (300, 300))

        cv2.imshow('Original Image', image)
        cv2.imshow('Aligned Image', aligned_image)

cv2.destoryAllWindows()



