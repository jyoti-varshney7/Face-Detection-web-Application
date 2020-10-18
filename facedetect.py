import cv2
faces_values= cv2.CascadeClassifier("C:\\Users\\Meghna\\Desktop\\OPENCV_IMG\\haarcascade_frontalface_default.xml")
eyes_values= cv2.CascadeClassifier("C:\\Users\\Meghna\\Desktop\\OPENCV_IMG\\haarcascade_eye.xml")
cam = cv2.VideoCapture(0)
while True:
    tf,img=cam.read()
    grayimg= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faces_values.detectMultiScale(grayimg)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(100,20,125),3)
        grayface =grayimg[y:y+h,x:x+h]
        colorface = img[y:y+h,x:x+w]
        eyes = eyes_values.detectMultiScale(grayface)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(colorface,(ex,ey), (ex+ew,ey+eh),(206,123,234),3)
    cv2.imshow("my image",img)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cam.release()
