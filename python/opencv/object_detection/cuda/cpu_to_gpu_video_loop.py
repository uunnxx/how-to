import cv2 as cv

vod = cv.VideoCapture('../tyan.mp4')

ret, frame = vod.read()

gpu_frame = cv.cuda_GpuMat()

# as long as the last frame was successfully read
while ret:

  # send current frame to GPU
  gpu_frame.upload(frame)

  # grab next frame with CPU
  ret, frame = vod.read()
