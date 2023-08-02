import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
cap = cv2.VideoCapture(r"C:\Users\Administrator\Desktop\1.mp4")
detector = FaceDetector(minconfidence=)
arduino = SerialObject("COM5")

while True:
    success, img = cap.read()
    if not success:
        break
    img, bboxs = detector.findFaces(img)

    if bboxs:
        arduino.sendData([1])
    else:
        arduino.sendData([0])
    cv2.imshow("Image", img)
    cv2.waitKey(100)
