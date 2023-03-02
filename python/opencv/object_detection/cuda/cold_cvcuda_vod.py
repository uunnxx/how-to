import cv2 as cv

vod = cv.VideoCapture('../tyan.mp4')

ret, frame = vod.read()

gpu_frame = cv.cuda_GpuMat()

while ret:
    gpu_frame.upload(frame)

    frame = cv.cuda.resize(gpu_frame, (852, 480))
    frame.download()

    ret, frame = vod.read()
