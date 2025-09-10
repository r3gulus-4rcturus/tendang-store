# ⚽ Tendang Store

**Tendang Store** adalah aplikasi football shop berbasis **Django**.  
Aplikasi ini dibuat sebagai salah satu tugas mata kuliah **Pemrograman Berbasis Platform**.  

🔗 **Aplikasi dapat diakses di link:**  
https://muhammad-lanang-tendangstore.pbp.cs.ui.ac.id/

---

## 👤 Identitas
- **Nama:** Muhammad Lanang Zalkifla Harits  
- **NPM:** 2406362860  
- **Kelas:** PBP A  

---

## ❓ Question & Answer

### Question:  
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Answer:  
1. **Membuat sebuah proyek Django baru.**  
   Saya membuat folder baru dan mengatur virtual environment di dalamnya, supaya semua dependency hanya terpasang di proyek ini, bukan di Python global. Setelah itu saya membuat proyek Django, mengatur `ALLOWED_HOSTS` agar bisa dijalankan di localhost, serta mengaktifkan `DEBUG=True` untuk memudahkan debugging. Saya juga menyiapkan repository Git lokal, menambahkan `.gitignore`, lalu menghubungkannya ke GitHub.  

2. **Membuat aplikasi dengan nama main pada proyek tersebut.**  
   Dengan command `startapp`, saya membuat aplikasi bernama main dan menambahkannya ke dalam `INSTALLED_APPS` di `settings.py`.  

3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**  
   Saya membuat file `urls.py` di dalam folder aplikasi main. Lalu, saya menghubungkan `urls.py` aplikasi tersebut ke `urls.py` di proyek utama dengan `include()`.  

4. **Membuat model pada aplikasi main dengan nama Product.**  
   Pada file `models.py`, saya menambahkan kelas `Product` yang mengextend `models.Model`. Di dalamnya saya mendefinisikan beberapa field yang wajib, sehingga Product bisa menjadi skema data di aplikasi.  

5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**  
   Di folder aplikasi main, saya membuat folder `templates` dan file `base.html` untuk menampilkan nama aplikasi, nama, dan kelas saya. Kemudian, di `views.py`, saya membuat fungsi `show_main()` dengan sebuah `context` berisi data tersebut. Fungsi ini merender template `main.html` menggunakan `render()`.  

6. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**  
   Pada `urls.py` aplikasi main, saya menambahkan `path('', show_main)` sehingga URL utama aplikasi mengarah ke fungsi `show_main()`.  

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**  
   Saya membuat file `.env.prod` untuk menyimpan environment variables dan mengonfigurasi database di `settings.py` berdasarkan variabel tersebut. Saya juga menambahkan domain PWS ke `ALLOWED_HOSTS`. Setelah membuat proyek baru di PWS dan memasukkan beberapa environment variables di PWS, saya menambahkan remote `pws` ke repository, lalu melakukan push. PWS secara otomatis membuild aplikasi, dan setelah selesai, proyek Django saya berhasil online di PWS.  

---

### Question:  
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

### Answer:  
https://drive.google.com/file/d/1jui-m9XHU4yl-0tsuzrL3wZGpw7iE7mc/view?usp=drive_link  

---

### Question:  
Jelaskan peran settings.py dalam proyek Django!

### Answer:  
`settings.py` befungsi sebagai tempat untuk menyimpan konfigurasi dalam proyek Django. Di dalamnya tersimpan berbagai variabel konfigurasi, seperti:  
- variabel `DATABASE` untuk menghubungkan proyek Django dengan remote database dengan cara menuliskan kredensial seperti nama, user, password, host, dan port dari database ke variabel tersebut.  
- `ALLOWED_HOSTS`, list nama host yang dapat melakukan hosting terhadap proyek django.  
- `INSTALLED_APPS`, list atas aplikasi apa saja yang terintegrasi pada proyek django tersebut.  

Selain itu, masih banyak lagi variabel konfigurasi lain yang ada di dalam `settings.py`.  

---

### Question:  
Bagaimana cara kerja migrasi database di Django?

### Answer:  
Migrasi adalah proses untuk menyimpan dan menerapkan perubahan struktur data dari `models.py` di django ke dalam database. Perubahan ini termasuk penambahan model baru maupun penambahan/modifikasi field pada model yang sudah ada sebelumnya. Migrasi dibutuhkan agar struktur database selalu sinkron dengan models.  

Cara melakukan migrasi database pada proyek Django terdiri dari dua langkah:  

> **1.** `python manage.py makemigrations`  
> Command ini dilakukan untuk membuat file migrasi. File ini berisi kode SQL yang dibutuhkan pada struktur database yang terbaru. File ini juga mencatat perubahan apa saja yang terjadi pada migrasi tersebut.  

> **2.** `python manage.py migrate`  
> Command ini dilakukan untuk benar-benar menerapkan migrasi kepada database. Program akan membaca file migrasi yang tadi telah dibuat dan menerapkannya pada database.  

---

### Question:  
Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

### Answer:  
Menurut saya, Django dipilih karena kesederhanaanya. Bahasa dari framework Django adalah python, bahasa pemrograman yang sangat mudah digunakan, sintaksnya simpel dan tidak verbose seperti bahasa pemrograman lain (baca: Java). Struktur file dalam framework ini pun mudah dimengerti, seperti `settings.py` untuk konfigurasi, `urls.py` untuk routing, `models.py` untuk membuat model pada database, dst. Pola arsitektur MTV pada Django juga mempermudah pemula memahami bagaimana flow Django bekerja. Walaupun dari sisi performa dan skalabilitas mungkin saja banyak framework lain yang lebih unggul, Django sangat ideal untuk pemula yang pertama kali belajar pemrograman web.  

---

### Question:  
Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

### Answer:  
Menurut saya, asisten dosen telah melakukan kerja yang cukup baik pada tutorial 1 kemarin. **Semangat kaka2 asdosss 🙌** 