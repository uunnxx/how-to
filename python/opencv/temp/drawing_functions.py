import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5px
img = cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv.imshow('Display window', img)


