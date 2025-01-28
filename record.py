#memanggil library opencv, time
import cv2,time

#mengidentifikasi kamera (bawaan laptop 0) 'cv2.CAP_DSHOW' Parameter kedua ini 
# menentukan backend yang digunakan untuk menangkap video. Dalam hal ini, 
# 'cv2.CAP_DSHOW' merujuk pada DirectShow, yang merupakan framework multimedia 
# di Windows untuk menangani video dan audio. Ini memberikan cara untuk menggunakan 
# driver kamera yang mendukung DirectShow.
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#memanggil file  xml yang disesuaikan dengan program yang akan dibuat 
recognition =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#memberikan input id
id =input('masukan id: ')

# var a = 0
a=0

#perulangan while
while True:
    #a=a+1
    a=a+1
    
    #cek,frame=camera.read() digunakan untuk membaca frame dari (citra) dari objek kamera
    check, frame = camera.read()

    #'cv2.cvtColor()' fungsi opencv yang digunakan untuk mengonversikan citra dari 
    #satu ruang warna ke ruang warna lain
    #'(frame, cv2.COLOR_BGR2GRAY)' mengidentifikasi warna citra frame, dan diubah ke ruang warna lain Gray
    CPU_detect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #'recognition.detectMultiScale()' digunakan untuk mendeteksi objek dalam citra
    #'(CPU_detect,scaleFactor=1.1)' memberi tahu bawha citra yayng di deteksi bersumber dari var CPU_detect 
    #yang telah diubah citra warnanya
    #'scaleFactor=1.1,' Parameter ini menentukan seberapa besar ukuran skala citra akan diubah pada setiap langkah deteksi.
    Camera_detect = recognition.detectMultiScale(CPU_detect, 1.1,5)

    #perulangan for
    #memberikan perulangan untuk mendeteksi wajah dan memberikan penanda
    #x, y, w, h: Variabel ini menyimpan nilai-nilai yang dikembalikan oleh fungsi deteksi_wajah.
    for (x, y, w, h) in Camera_detect:

        #fungsi opencv untuk menulis file
        cv2.imwrite('Dataset/User.'+str(id)+'.'+str(a)+'.jpg',CPU_detect[y:y+h,x:x+w])

        #fungsi openc untuk mengidentifikasi objek
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        #fungsi opencv untuk menampilkan window
        cv2.imshow('Record', frame)

        #pengkondisian 
        #jika var a lebih dari 29, maka kamera akan di tutup
        if(a>29):
            camera.release()
            cv2.destroyAllWindows()