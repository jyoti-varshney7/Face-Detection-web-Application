from PIL import Image
from cv2.face import LBPHFaceRecognizer_create as lrc
import os
import numpy as np
import cv2
faces_values = cv2.CascadeClassifier(
    "C:\\Users\\Meghna\\Desktop\\OPENCV_IMG\\haarcascade_frontalface_default.xml")
eyes_values = cv2.CascadeClassifier(
    "C:\\Users\\Meghna\\Desktop\\OPENCV_IMG\\haarcascade_eye.xml")


def createdataset(uid):

    cam = cv2.VideoCapture(0)
    sam = 0

    while True:
        tf, img = cam.read()
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faces_values.detectMultiScale(grayimg)
        for x, y, w, h in faces:
            sam += 1
            cv2.rectangle(img, (x, y), (x+w, y+h), (100, 20, 125), 3)

            colorface = img[y:y+h, x:x+w]

            cv2.imwrite('Dataset/user.'+str(sam) +
                        '.'+str(uid)+'.jpg', colorface)
        if sam == 35:
            break
    cam.release()


createdataset(9)


def TrainMachineWithFace():
    li = os.listdir('Dataset')
    faceNP = []
    ids = []
    for i in li:
        a = os.path.join('Dataset', i)
        face = Image.open(a).convert('L')
        faceNP.append(np.array(face))
        idd = i.split('.')[1]
        ids.append(int(idd))

    ids = np.array(ids)
    model = lrc()
    model.train(faceNP, ids)
    model.save('training.yml')


TrainMachineWithFace()


def Detect():
    cam = cv2.VideoCapture(0)

    model = lrc()
    model.read('training.yml')
    while True:
        tf, img = cam.read()
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faces_values.detectMultiScale(grayimg)
        for x, y, w, h in faces:

            colorface = img[y:y + h, x:x + w]
            grayface = grayimg[y:y+h, x:x+w]
            idd, dis = model.predict(grayface)
            if dis < 70:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.waitKey(2)
        cv2.imshow("my image", img)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

    cam.release()


Detect()
