# Pemrograman Berbasis Platform - Tugas 6

Nama: Calista Vimalametta Heryadi<br>
NPM: 2106630473<br>
Kelas: C

---

## Link App Heroku

<https://tgs-pbp.herokuapp.com/todolist/>

---

## Asynchronous dan Synchronous Programming

* Synchronous programming adalah paradigma pemrograman yang memproses satu persatu, sehingga user harus menunggu hingga response diberikan agar dapat menggunakan webapp atau mengirim request lagi. Kelebihannya adalah implementasi yang mudah.

* Asynchronous programming adalah paradigma pemrograman yang menerima request saat memproses request lain, sehingga user tidak perlu menunggu response dan dapat terus menggunakan webapp. Kelebihannya adalah meningkatkan kualitas user experience.

---

## Event-Driven Programming

Event-driven programming adalah paradigma pemrograman yang merespon terhadap suatu kejadian atau event. Event dapat dipicu oleh user atau dapat terjadi secara otomatis. Contoh impelemntasi user event-driven programming pada tugas ini adalah tombol "Add Task" yang membuka modal pengisian form saat ditekan.

---

## Asynchronous Programming pada AJAX

AJAX (Asynchronous JavaScript and XML) adalah teknik implementasi JavaScript agar program berjalan secara asynchronous. AJAX mengurus request dengan mengirim dan menerima data yang berubah saja, bukan seluruh halaman, sehingga halaman yang menampilkan data berubah tanpa harus di-reload oleh user. AJAX tidak harus menggunakan XML untuk mengirim data, contohnya tugas ini yang menggunakan JSON.

---

## Implementasi Tugas 6

### Implementasi AJAX GET
1. **base.html:** Tambah `<script>` AJAX JQuery dalam `<head>` agar dapat menggunakan function get dan post.
2. **views.py:** Buat view `show_todolist_json` yang mengembalikan data task dalam bentuk JSON response.
3. **views.py:** Tambah variable `user_id` dalam context view `show_todolist` untuk membandingkannya dengan user pada data JSON.
4. **urls.py:** Tambah path yang menunjuk pada view `show_todolist_json`.
5. **todolist.html:** Buat `<script>` berisi function JS `appendCard` dalam `{% block meta %}` yang menambahkan tag HTML pada `card-grid`.
6. **todolist.html:** Pindahkan tag-tag untuk membuat card dari `<body>` ke dalam function `appendCard`.
7. **todolist.html:** Buat get dalam `<script>` yang mengambil data JSON dari view `show_todolist_json` dan memanggil `appendCard` untuk setiap task dalam data.

### Implementasi AJAX POST
1. **base.html:** Tambah `<script>` Bootstrap JavaScript dalam `<head>` agar dapat menggunakan modal.
2. **todolist.html:** Buat tombol `Add Task` di barisan tombol-tombol untuk memunculkan modal.
3. **todolist.html:** Buat modal menggunakan sekumpulan `<div>` dan masukkan `<form>` yang sama dengan form di `create_task.html`.
4. **views.py:** Buat view `add_task` yang menerima request POST berisi isian form, menyimpannya dalam database model, dan mengembalikan data tersebut dalam bentuk JSON response.
5. **urls.py:** Tambah path yang menunjuk pada view `add_task`.
6. **todolist.html:** Buat post dalam `<script>` yang menngirimkan isian form ke view `add_task` dan memanggil `appendCard` untuk task yang dikembalikan dalam JSON.