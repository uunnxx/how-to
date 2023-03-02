import cv2 as cv

vod = cv.VideoCapture('../tyan.mp4')

ret, frame = vod.read()

# set scale of resized image
scale = 0.5

gpu_frame = cv.cuda_GpuMat()

while ret:

    gpu_frame.upload(frame)

    # resize image (numpy.ndarray -> cv2.cuda_GpuMat)
    resized = cv.cuda.resize(gpu_frame, (int(1280 * scale), int(720 * scale)))

    # apply luv, hsv, and grayscale filters to resized image
    luv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2LUV)
    hsv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2HSV)
    gray = cv.cuda.cvtColor(resized, cv.COLOR_BGR2GRAY)

    ret, frame = vod.read()
