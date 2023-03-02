import cv2 as cv

vod = cv.VideoCapture('../tyan.mp4')

ret, frame = vod.read()

scale = 0.5

gpu_frame = cv.cuda_GpuMat()

while ret:

    gpu_frame.upload(frame)

    resized = cv.cuda.resize(gpu_frame, (int(1280 * scale), int(720 * scale)))

    luv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2LUV)
    hsv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2HSV)
    gray = cv.cuda.cvtColor(resized, cv.COLOR_BGR2GRAY)
    
    # download new image(s) from GPU to CPU (cv2.cuda_GpuMat -> numpy.ndarray)
    resized = resized.download()
    luv = luv.download()
    hsv = hsv.download()
    gray = gray.download()

    ret, frame = vod.read()
