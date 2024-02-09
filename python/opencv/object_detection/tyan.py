import cv2 as cv

# img = cv.imread('lena.PNG')

cap = cv.VideoCapture()
cap.open('tyan.mp4')

cap.set(3, 720)
cap.set(4, 480)


class_names = []
class_file = 'coco.names'

with open(class_file, 'rt') as f:
    class_names = f.read().rstrip('\n').split('\n')


config_path = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weights_path = "frozen_inference_graph.pb"

net = cv.dnn_DetectionModel(weights_path, config_path)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


while True:
    success, img = cap.read()
    class_ids, confs, bbox = net.detect(img, confThreshold=0.6)

    if len(class_ids) != 0:
        for class_id, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):
            cv.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv.putText(img, class_names[class_id-1], (box[0] + 10, box[1] + 30), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

            cv.putText(
                img,
                f"{str(round(confidence * 100, 2))}%",
                (box[0] + 200, box[1] + 30),
                cv.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 255),
                2,
            )

    cv.imshow('Tyanochki', img)
    cv.waitKey(1)
