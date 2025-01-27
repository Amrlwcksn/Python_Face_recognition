import cv2,time
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
recognition =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id =input('masukan id: ')

a=0

while True:
    a=a+1
    check, frame = camera.read()
    CPU_detect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Camera_detect = recognition.detectMultiScale(CPU_detect, 1.1,5)
    for (x, y, w, h) in Camera_detect:
        cv2.imwrite('Dataset/User.'+str(id)+'.'+str(a)+'.jpg',CPU_detect[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('Record', frame)
        if(a>29):
            camera.release()
            cv2.destroyAllWindows()