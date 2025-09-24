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

## 📑 Quick Access
- [2️⃣ Jawaban Tugas Individu 2](#2️⃣-jawaban-tugas-individu-2)
- [3️⃣ Jawaban Tugas Individu 3](#3️⃣-jawaban-tugas-individu-3)
- [4️⃣ Jawaban Tugas Individu 4](#4️⃣-jawaban-tugas-individu-4)

---

## 2️⃣ Jawaban Tugas Individu 2

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
<img width="873" height="717" alt="Screenshot 2025-09-09 133212" src="https://github.com/user-attachments/assets/cc8b315c-dbc8-43c5-8cf9-34bf1b38f916" />

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

---

## 3️⃣ Jawaban Tugas Individu 3

### Question:  
Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

### Answer:  
Setiap platform pasti butuh menyimpan data (misalnya data pengguna atau transaksi). Data tersebut ada di **database**.  
Untuk membaca atau menulis data ke database, kita memerlukan proses **data delivery** agar bisa berinteraksi dengan data tersebut.  

---

### Question:
Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

### Answer:
**XML** dan **JSON** memiliki kekurangan dan kelebihannya masing-masing. **XML** dapat mendeskripsikan struktur data dengan detail sehingga akan memudahkan apabila data yang dikirim kompleks. Namun, karena detail tersebut, XML menjadi sangat verbose. Di sisi lain, **JSON** merepresentasikan data dengan struktur yang sangat simpel, tetapi tidak cocok jika mengirim data yang kompleks. JSON lebih populer karena strukturnya yang simpel lebih cocok digunakan pada arsitektur yang umum digunakan seperti website app, mobile app, microservices, dsb.  

---

### Question:
Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? 

### Answer:  
Method ``is_valid()`` berfungsi untuk melakukan **validasi input form** dari pengguna. Django akan memeriksa apakah setiap field sudah sesuai tipe data dan aturan yang ditentukan. Dengan adanya method ini, data yang masuk lebih terjamin konsistensinya dan dapat meminimalkan potensi error, dan pengguna mendapat feedback langsung jika ada field yang tidak valid. Hal ini memudahkan developer karena tidak perlu lagi menulis kode validasi secara manual.  
 
---

### Question:
Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

### Answer:  
``csrf_token`` dibutuhkan untuk mencegah **CSRF attack (Cross Site Request Forgery)**. Tanpa token ini, penyerang bisa memanfaatkan cookie pengguna yang tersimpan di browser untuk mengirim request POST palsu ke server, misalnya dengan membuat form yang seolah-olah dikirimkan oleh user. Dengan menambahkan ``csrf_token``, setiap request dari form harus menyertakan token unik yang hanya diberikan ke browser asli pengguna. Akibatnya, walaupun penyerang memiliki cookie user, mereka tetap tidak bisa membuat request palsu tanpa token tersebut.  

---

### Question:
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Answer:  
1. **Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.**
   Saya menambahkan empat fungsi views baru untuk menampilkan data dalam format **XML** dan **JSON**, baik untuk seluruh data maupun berdasarkan ID. Untuk melakukannya saya mengimpor ``HttpResponse`` dan ``serializers`` dari Django, serta model ``Product`` yang akan digunakan. Pada fungsi ``show_xml`` dan ``show_json``, saya mengambil semua data produk menggunakan ``Product.objects.all()``, lalu mengubah hasilnya menjadi XML atau JSON dengan ``serializers.serialize()`` sebelum dikembalikan melalui response. Sementara itu, untuk versi by ID saya menggunakan ``Product.objects.filter(pk=product_id)`` dan menambahkan pengecekan jika data tidak ditemukan.  
2. **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.**
   Saya membuat routing URL untuk setiap views tersebut. Semua fungsi views yang sudah dibuat saya impor, kemudian saya tambahkan path baru di ``main/urls.py``. Untuk fungsi yang menampilkan data berdasarkan ID, saya menambahkan parameter ``<str:product_id>`` pada path sehingga ID produk bisa diteruskan langsung ke views.  
3. **Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.**
   Saya mengembangkan halaman utama yang menampilkan daftar produk dengan tombol **Add** untuk menambah produk baru dan tombol **Detail** untuk melihat informasi produk secara lengkap. Pada fungsi ``show_main`` saya mengambil seluruh produk dengan ``Product.objects.all()`` lalu mengirimkannya ke template melalui context. Template ``main.html`` kemudian saya modifikasi agar menampilkan daftar produk sekaligus menyediakan tombol Add Product yang mengarah ke halaman form, serta tombol Detail yang mengarah ke halaman detail produk.  
4. **Membuat halaman form untuk menambahkan objek model pada app sebelumnya.**
   Saya menambahkan halaman form untuk membuat produk baru. Untuk ini, saya membuat fungsi ``create_product`` di ``views.py``, lalu membuat file ``forms.py`` agar form bisa digenerate otomatis dari model. Saya juga menambahkan template ``create_product.html`` sebagai tampilan form. Tombol Add Product yang ada di halaman utama diarahkan ke halaman ini menggunakan ``{% url 'main:create_product' %}``. Supaya dapat diakses, saya juga menambahkan routing URL yang sesuai di ``main/urls.py``.  
5. **Membuat halaman yang menampilkan detail dari setiap data objek model.**
   Saya membuat halaman detail produk untuk menampilkan informasi lengkap berdasarkan ID produk. Saya menambahkan fungsi ``show_product_by_id`` di ``views.py`` dengan memanfaatkan ``get_object_or_404()`` agar lebih aman jika ID tidak ditemukan. Informasi produk yang diambil kemudian saya kirimkan ke template ``show_product.html``. Dari halaman utama, tombol **Lihat Detail Produk** pada tiap produk saya hubungkan ke halaman detail ini sehingga pengguna bisa melihat informasi lengkap dari produk yang dipilih.  

---

### Question:
Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

### Answer:  
Saran saya, apabila terdapat snippet kode yang perlu diimplementasikan oleh mahasiswa, bisa dijelaskan dengan lebih detail mengenai makna dari masing-masing line, apa yang ingin dicapai dengan kode tersebut, dan bagaimana memodifikasinya. Terima kasih. Semangat kaka asdosss🤩🤩🤩

---

### Question:
Buatlah screenshot dari hasil akses URL pada Postman, lalu tambahkan ke dalam README.md

### Answer:  
<img width="1920" height="1200" alt="Screenshot (206)" src="https://github.com/user-attachments/assets/4cbd7c36-561f-4688-b646-ee4bad0cfebf" />
<img width="1920" height="1200" alt="Screenshot (207)" src="https://github.com/user-attachments/assets/c81aa647-141d-47e5-ad08-f72600666d21" />
<img width="1920" height="1200" alt="Screenshot (204)" src="https://github.com/user-attachments/assets/5bde9c17-8fdb-4772-9205-07041910d50f" />
<img width="1920" height="1200" alt="Screenshot (205)" src="https://github.com/user-attachments/assets/f2150add-f9f7-4092-94f4-3f119a5f0e9a" />

---

## 4️⃣ Jawaban Tugas Individu 4

# Jawaban Tugas Individu 4

### Pertanyaan:
Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.

### Jawaban:
Django `AuthenticationForm` adalah sebuah *form* bawaan yang disediakan oleh *framework* Django untuk menangani proses autentikasi pengguna. *Form* ini secara spesifik dirancang untuk memvalidasi kredensial yang dimasukkan oleh pengguna, yaitu `username` dan `password`.

* **Kelebihan:**
    * *Form* ini secara otomatis menangani aspek keamanan penting, seperti proteksi terhadap serangan *timing attacks*.
    * `AuthenticationForm` tidak hanya memeriksa apakah *password* benar, tetapi juga memverifikasi apakah akun pengguna yang bersangkutan berstatus aktif.
    * Dapat dengan mudah diintegrasikan dengan sistem autentikasi Django lainnya, seperti fungsi `login()` dari modul `django.contrib.auth`.

* **Kekurangan:**
    * Secara *default*, *form* ini hanya menyediakan *field* untuk `username` dan `password`, sehingga kustomisasi lebih lanjut (misalnya, *login* menggunakan *email*) memerlukan pembuatan *form* turunan (*subclassing*).
    * Implementasinya memerlukan penulisan logika secara manual di dalam *view* untuk memproses data dan mengautentikasi pengguna.

---

### Pertanyaan:
Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?

### Jawaban:
**Autentikasi** adalah proses untuk memverifikasi identitas seorang pengguna, atau dengan kata lain, menjawab pertanyaan "Siapakah Anda?". Proses ini memastikan bahwa pengguna adalah benar-benar orang yang mereka klaim. Di sisi lain, **otorisasi** adalah proses untuk menentukan hak akses atau izin yang dimiliki oleh pengguna yang telah terautentikasi. Ini menjawab pertanyaan "Apa yang boleh Anda lakukan?".

Django mengimplementasikan kedua konsep ini melalui *framework* `django.contrib.auth` yang komprehensif:
* **Implementasi Autentikasi:** Django menangani autentikasi dengan menyediakan model `User` bawaan, serta *form* siap pakai seperti `AuthenticationForm` untuk proses *login* dan `UserCreationForm` untuk registrasi. *Framework* ini juga menyediakan fungsi-fungsi *helper* seperti `login()`, `logout()`, dan `authenticate()` untuk mengelola sesi pengguna di dalam *views*.
* **Implementasi Otorisasi:** Untuk otorisasi, Django menggunakan beberapa mekanisme. Yang paling umum adalah *decorator* `@login_required` yang berfungsi untuk membatasi akses ke sebuah *view* hanya bagi pengguna yang sudah *login*. Selain itu, Django juga memiliki sistem perizinan (*permissions*) yang lebih granular yang dapat dikaitkan dengan model `User` dan `Group` untuk mengontrol akses terhadap aksi atau data tertentu secara lebih spesifik.

---

### Pertanyaan:
Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

### Jawaban:
Penggunaan *cookies* tidak sepenuhnya aman secara *default* dan memiliki beberapa risiko potensial jika tidak dikelola dengan hati-hati. Beberapa risiko tersebut antara lain **Cross-Site Scripting (XSS)**, di mana penyerang dapat menyuntikkan skrip berbahaya untuk mencuri data *cookie*; **Cross-Site Request Forgery (CSRF)**, di mana penyerang memancing pengguna untuk melakukan tindakan yang tidak diinginkan di situs web tempat mereka terautentikasi; dan **Session Hijacking**, di mana penyerang mencuri *session ID* dari *cookie* untuk mengambil alih sesi pengguna.
Django mengatasi risiko-risiko ini dengan beberapa fitur keamanan bawaan yang kuat:
1.  **Proteksi CSRF:** Django menyediakan **CSRF Middleware** dan *template tag* `{% csrf_token %}` yang wajib disertakan dalam setiap *form* dengan metode `POST`. Token ini memastikan bahwa permintaan data hanya berasal dari situs Anda sendiri.
2.  **HttpOnly Flag:** *Cookie* sesi yang dibuat oleh Django secara *default* diatur dengan *flag* `HttpOnly`. *Flag* ini mencegah *cookie* diakses melalui JavaScript di sisi klien, sehingga secara signifikan mengurangi risiko pencurian *cookie* melalui serangan XSS.
3.  **Secure Cookies:** Django menyediakan pengaturan seperti `SESSION_COOKIE_SECURE` dan `CSRF_COOKIE_SECURE`. Jika diaktifkan, pengaturan ini memastikan bahwa *cookies* hanya akan dikirim melalui koneksi HTTPS yang terenkripsi, untuk mencegah penyadapan data (*man-in-the-middle attack*).

---

### Pertanyaan:
Jelaskan bagaimana cara Anda mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).

### Jawaban:
1.  **Mengimplementasikan Fungsi Registrasi, *Login*, dan *Logout***
    Saya memulai dengan membuat tiga fungsi pada `views.py`: `register`, `login_user`, dan `logout_user`.
    * Untuk fungsi `register`, saya memanfaatkan *form* bawaan Django, yaitu `UserCreationForm`. Ketika permintaan berjenis `POST` dan data yang dikirimkan valid, akun pengguna baru akan disimpan ke basis data menggunakan metode `form.save()`.
    * Pada fungsi `login_user`, saya menggunakan `AuthenticationForm`. Setelah validasi berhasil, pengguna akan dialihkan ke halaman utama. Pada momen ini, saya juga mengatur *cookie* untuk `last_login` dan `username` yang akan ditampilkan.
    * Fungsi `logout_user` bertugas untuk mengakhiri sesi pengguna, mengarahkan mereka kembali ke halaman *login*, serta menghapus *cookies* `last_login` dan `username`. Terakhir, saya menambahkan *routing* yang sesuai untuk ketiga *view* ini di `urls.py` dan membuat *template* HTML untuk halaman registrasi dan *login*.

2.  **Membuat Dua Akun Pengguna dengan Masing-Masing Tiga Data Dummy**
    Proses ini saya lakukan langsung melalui antarmuka aplikasi. Pertama, saya mendaftarkan akun pengguna pertama melalui halaman registrasi. Setelah berhasil *login* dengan akun tersebut, saya menambahkan tiga data produk menggunakan fungsionalitas tambah produk yang telah ada. Kemudian, saya keluar (*logout*), mendaftarkan akun kedua, *login*, dan mengulangi proses penambahan tiga data produk untuk pengguna kedua ini.

3.  **Menghubungkan Model `Product` dengan `User`**
    Untuk menghubungkan setiap produk dengan pemiliknya, saya memodifikasi `models.py`. Pertama, saya mengimpor model `User` dari `django.contrib.auth.models`. Selanjutnya, saya menambahkan sebuah *field* baru bernama `user` pada model `Product`. *Field* ini didefinisikan sebagai `ForeignKey` yang berelasi dengan model `User`, yang menandakan bahwa setiap entri produk terikat pada satu pengguna. Setelah model diperbarui, saya menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk menerapkan perubahan skema ini ke basis data.

4.  **Menampilkan Informasi Pengguna dan Menerapkan *Cookies***
    Untuk menampilkan informasi pengguna yang sedang *login* (seperti `username`), saya memanfaatkan objek `request` yang tersedia di dalam *view*. Informasi pengguna dapat diakses melalui `request.user`. Saya kemudian meneruskan data ini, misalnya `request.user.username`, ke *template* melalui *context*. Sementara itu, untuk `last_login`, saya mengimplementasikannya menggunakan *cookies*. Saat pengguna berhasil *login*, saya mengatur *cookie* `last_login` dengan *timestamp* saat itu. *Cookie* ini akan dihapus secara eksplisit ketika pengguna melakukan *logout* untuk memastikan data sesi tetap relevan.