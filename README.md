<h1> langkah-langkah</h1>
<h3> Pastikan semua keperluan tersimpan pada folder yang sama</h3>
<p>
	
1. Buat folder untuk penginstallan library env, dengan menggunakan cmd
	<p>'py -m venv [namafolder]'<p>

2. aktivasi environment env
   	<p>'[namafolder]\Scripts\activate'<p>

3. install opencv
	<p>'pip install opencv-python'<p>
	<p>'pip install opencv-contrib-python'<p>
	<p>'pip install pillow'<p>

5. ambil data .xml sesuaikan dengan kebutuhan program, simpan kode dalam
  format .xml (github: https://github.com/opencv/tree/master/data/haarcascades )

6. buat folder untuk menyimpan data wajah yang akan di daftarkan Default = Dataset.

7. Jalankan record.py untuk merekam wajah yang akan di daftarkan, data akan otomatis tersimpan pada folder Dataset.

8. jalankan training.py untuk mengubah data .jpg menjadi .xml agar dapat di baca oleh main.py

9. Jalankan main.py maka wajah yang terdaftar akan di identifikasikan sebagai "Admin".

</p>
