import cv2
thres = 0.45 # Threshold to detect object

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
cap.set(10,70)

class_names= []
class_files = 'coco.names'

with open(class_files, "rt") as f:
    class_names = f.read().rstrip('n').split('n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIds, confs, box = net.detect(img,confThreshold=thres)
    print(classIds, box)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), box):
            cv2.rectangle(img, box, color=(0,255,0), thickness=2)
            cv2.putText(img, class_names[classId-1].upper(), (box[0]+10, box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    cv2.imshow("Output", img)
    cv2.waitKey(1)
