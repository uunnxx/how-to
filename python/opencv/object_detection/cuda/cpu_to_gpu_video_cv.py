import cv2 as cv

vod = cv.VideoCapture('../tyan.mp4')

ret, frame = vod.read()

# create a frame on GPU for images
gpu_frame = cv.cuda_GpuMat()

# send 1st frame to GPU
gpu_frame.upload(frame)
