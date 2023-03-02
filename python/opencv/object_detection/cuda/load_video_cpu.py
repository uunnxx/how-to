import cv2 as cv

# load .mp4 video
vod = cv.VideoCapture('../tyan.mp4')

# grab 1st frame (ret is bool)
ret, frame = vod.read()
