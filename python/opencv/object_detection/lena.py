import cv2 as cv

img = cv.imread('lena.PNG')

cv.imshow('Output', img)
cv.waitKey(0)
