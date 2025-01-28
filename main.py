#menambahkan library opencv
import cv2 

#memanggil file  xml yang disesuaikan dengan program yang akan dibuat 
recognition =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#mengidentifikasi kamera (bawaan laptop 0)
camera = cv2.VideoCapture(0)

#'cv2.face.LBPHFaceRecognizer_create()'
# modul dari opencv untuk mengenali wajah berbasis LBPHF
pengenalan = cv2.face.LBPHFaceRecognizer_create()

#memberikan perintah untuk membaca file dataset xml, berisi wajah yang telah ter rekam
pengenalan.read('Dataset/training.xml')

#fungsi mendeteksi wajah
def deteksi_wajah(frame):
    #'cv2.cvtColor()' fungsi opencv yang digunakan untuk mengonversikan citra dari 
    #satu ruang warna ke ruang warna lain
    #'(frame, cv2.COLOR_BGR2GRAY)' mengidentifikasi warna citra frame, dan diubah ke ruang warna lain Gray
    CPU_detect = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    #'recognition.detectMultiScale()' digunakan untuk mendeteksi objek dalam citra
    #'(CPU_detect,scaleFactor=1.1)' memberi tahu bawha citra yayng di deteksi bersumber dari var CPU_detect 
    #yang telah diubah citra warnanya
    #'scaleFactor=1.1,' Parameter ini menentukan seberapa besar ukuran skala citra akan diubah pada setiap langkah deteksi. 
    Camera_detect = recognition.detectMultiScale(CPU_detect, scaleFactor=1.1,)

    #mengembalikan hasil dari deteksi wajah
    return Camera_detect

#fungsi memberikan box pada wajah yang terdeteksi
def drawer_box(frame):
    #memberikan perulangan untuk mendeteksi wajah dan memberikan penanda
    #x, y, w, h: Variabel ini menyimpan nilai-nilai yang dikembalikan oleh fungsi deteksi_wajah.
    for x,y,w,h in deteksi_wajah(frame):

        #fungsi opencv untuk membuat garis persegi pada wajah yang terdeteksi
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,00),1)
        
        #memberikan nama pada id bertipe data string
        id = 'Admin'
        #fungsi opencv untuk menampilkan teks pada wajah yang terdeteksi
        cv2.putText(frame,str(id),(x+40,y-10), cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0))

#fungsi menutup window
def close_window():
    #memberikan perintah kepada var camera untuk menutup kamera
    camera.release()

    #fungsi opencv untuk menutup windows yang terbuka
    cv2.destroyAllWindows()

    #keluar
    exit()

#fungsi main
def main():

    #menggunakan perulangan while
    while True:

        #camera.read() digunakan untuk membaca frame dari (citra) dari objek kamera
        #__, Variabel ini biasanya digunakan untuk menampung nilai yang tidak diperlukan.
        # Dalam hal ini, camera.read() mengembalikan dua nilai: status (True jika frame
        #  berhasil dibaca, False jika tidak) dan frame itu sendiri. Dengan menggunakan __, 
        # Anda mengabaikan statusnya, hanya mengambil frame.
        __,frame = camera.read()

        #memanggil fungsi untuk mengambar kotak
        drawer_box(frame)

        #menampilkan citra pada window
        cv2.imshow("Deteksi wajah", frame)#frame mengidentifikasi citra yang akan di tampilkan

        #penkondisian
        #'cv2.waitkey(1)', fungsi dari opencv untuk menunggu input dari pengguna selama 1 milidetik,
        # '& 0xFF' tulis aja kalau ngga kodinganmu bakal error
        # '== ord ('q')' memberikan fungsi pada q ketika ditekan 
        if cv2.waitKey(1) & 0xFF == ord ('q'):

            #'close_window()' memanggil fungsi untuk menutup window
            close_window()

#kalau ngga di tulis kodingamnmu bakal merah merona          
if __name__ == '__main__':
    main()
    