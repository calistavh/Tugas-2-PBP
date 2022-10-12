# Pemrograman Berbasis Platform - Tugas 5

Nama: Calista Vimalametta Heryadi<br>
NPM: 2106630473<br>
Kelas: C

---

## Link App Heroku

<https://tgs-pbp.herokuapp.com/todolist/>

---

## Inline, Internal, dan External CSS

| Perbedaan | Inline | Internal | External |
| - | - | - | - |
| Di file | .html | .html | .css |
| Dimasukkan ke .html dengan | attribute `style` dalam tag lain | tag `<style>` dalam tag `<head>` | tag `<link>` dalam tag `<head>` |
| Penulisan | `"property: value;"` | `selector {property: value;}` | `selector {property: value;}` |
| Prioritas | pertama | kedua | ketiga |
| Kelebihan | mudah dimasukkan dan di-test, kustomisasi tag spesifik | tidak harus membuat file .css, kustomisasi per selector | HTML dan CSS terpisah, dapat digunakan beberapa halaman sekaligus |
| Kekurangan | HTML dan CSS tercampur di file yang sama, berlaku untuk satu tag saja | HTML dan CSS masih di file yang sama walaupun terpisah, berlaku untuk satu halaman saja | harus membuat file .css, kustomisasi kurang spesifik |

---

## Beberapa Tag HTML5

1. `<html>`: root file, semua tag lain berada di dalam tag ini.
2. `<head>`: kepala halaman, semua tag yang berhubungan dengan informasi file berada di dalam tag ini.
3. `<body>`: isi halaman, semua tag yang menampilkan sesuatu berada di dalam tag ini.
4. `<title>`: memuat judul halaman yang ditampilkan di tab.
5. `<style>`: memuat styling (misal CSS) yang digunakan dalam halaman ini.
6. `<h1>` dst.: memuat heading (teks yang lebih besar dan tebal).
7. `<div>`: memuat bagian dari halaman, berisi tag-tag lain.
8. `<br>`: line break (newline).
9. `<hr>`: horizontal rule (garis).
10. `<a>`: memuat hyperlink (dengan attribute href).
11. `<span>`: memuat bagian dari teks, biasanya untuk styling.
12. `<p>`: memuat teks paragraf, otomatis diberi jarak.
13. `<table>`: memuat table dengan tag baris `<tr>` dan tag data `<td>` (juga `<th>` untuk header/cetak tebal).
14. `<form>`: memuat form, tag `<input>` untuk field berada di dalam tag ini.

---

## Tipe Selector CSS

1. **element:** style untuk satu jenis element/tag tertentu, ditulis misalnya `tag-html`.
2. **id:** style untuk satu element spesifik dengan id yang sama, ditulis misalnya `#id`.
3. **class:** style untuk element yang memiliki nilai attribute class yang sama, ditulis misalnya `.nilai-attribute`.
4. **universal:** style untuk semua element dalam file .html, ditulis `*`.
5. **group:** style untuk beberapa element sekaligus, ditulis misalnya `element-1, element-2` (selector di atas dapat digunakan).
6. **attribute:** style untuk element yang memiliki attribute yang sama, ditulis misalnya `[attribute]`.

---

## Implementasi Tugas 5

### base.html
1. Include Bootstrap CSS dengan menambahkan `<link>` di dalam `<head>`.

### login.html, register.html, dan create_task.html
1. Memindahkan `<h1>` ke `<div>` tersendiri di atas halaman untuk membuat header.
2. Mengeluarkan tombol submisi keluar dari `<table>` agar tombol terletak di tengah.
3. Mengubah tampilan message dari menggunakan poin `<ul>` menjadi `<span>` yang mengganti warna teks.
4. (`create_task.html` dan `views.py`) Mengubah tampilan form dari menggunakan `{{form.as_table}}` menjadi `<input>` manual untuk memperbaiki responsiveness halaman.

### todolist.html
1. Memindahkan `<h1>` ke `<div>` tersendiri di atas halaman untuk membuat header.
2. Menukar urutan tampilan objek menjadi username, message, tombol, dan task.
3. Menggabungkan tombol logout dan tambah task menjadi satu baris.
4. Mengubah tampilan task dari menggunakan `<table>` menjadi `<div class="card">`.
5. Menambahkan fitur animasi hover pada card.

### Style yang disamakan untuk objek tertentu
1. **header:** `<div class="bg-dark text-white text-center py-3">`
2. **isi halaman:** `<div class="container text-center py-3">`
3. **tabel form:** `<table class="table table-hover table-borderless align-middle">`
4. **tombol form:** `<input class="btn btn-dark" ...>`
5. **pesan:** `<span class="text-danger">` atau `<span class="text-success">`
6. **grid untuk tombol:** `<div class="row justify-content-center">` dan `<div class="col-6 col-sm-4 col-md-3">`
7. **tombol todolist:** `<a class="btn btn-dark">`
8. **grid untuk card:** `<div class="row justify-content-center px-3>` dan `<div class="col-sm-6 col-md-4 p-3">`
9. **card:** `<div class="card h-100 text-white bg-dark">`
10. **animasi hover card:** `.card{transition: all 0.2s ease;} .card:hover{opacity: 0.8, transform: scale(1.1);}`