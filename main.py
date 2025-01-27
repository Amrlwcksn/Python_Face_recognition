import cv2

recognition =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
pengenalan = cv2.face.LBPHFaceRecognizer_create()
pengenalan.read('Dataset/training.xml')

def deteksi_wajah(frame):
    CPU_detect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Camera_detect = recognition.detectMultiScale(CPU_detect, scaleFactor=1.1,)
    return Camera_detect

def drawer_box(frame):
    for x,y,w,h in deteksi_wajah(frame):
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,00),1)
        id = 'Admin'
        cv2.putText(frame,str(id),(x+40,y-10), cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0))

def close_window():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        __,frame = camera.read()
        drawer_box(frame)
        cv2.imshow("Deteksi wajah", frame)

        if cv2.waitKey(1) & 0xFF == ord ('q'):
            close_window()
if __name__ == '__main__':
    main()