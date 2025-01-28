<h1> langkah-langkah</h1>
<h3> Pastikan semua keperluan tersimpan pada folder yang sama</h3>
<p>
1. Buat folder untuk penginstallan library env
	py -m venv [namafolder]

2. aktivasi environment env
	[namafolder]\Scripts\activate

3. install opencv
	py -m pip install opencv-python
	py -m pip install opencv-contrib-python
	py -m pip install pillow

4. ambil data .xml sesuaikan dengan kebutuhan program, simpan kode dalam
  format .xml (github: https://github.com/opencv/tree/master/data/haarcascades

5. buat folder untuk menyimpan data wajah yang akan di daftarkan Default = Dataset.

6. Jalankan record.py untuk merekam wajah yang akan di daftarkan, data akan otomatis tersimpan pada folder Dataset.

7. jalankan training.py untuk mengubah data .jpg menjadi .xml agar dapat di baca oleh main.py

8. Jalankan main.py makan wajah yang terdaftar akan di identifikasikan sebagai "Admin".

</p>
