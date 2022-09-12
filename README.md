# Pemrograman Berbasis Platform - Tugas 2
Nama: Calista Vimalametta Heryadi<br>
NPM: 2106630473<br>
Kelas: C

## Link App Heroku
<https://tugas-02-pbp.herokuapp.com/katalog>

## Bagan Request-Response Django
![Bagan Request-Response Django](bagan_django.jpg "Bagan Request-Response Django")

## Virtual Environment
Virtual environment berfungsi sebagai workspace bagi sebuah project Django yang terpisah dari project Django lainnya. Pengaturan dan package yang di-install di satu virtual environment tidak mempengaruhi environment lainnya, sehingga menjadi lebih terkontrol. Project Django dapat dibuat tanpa virtual environment, hanya saja package requirement yang dibutuhkan dapat berbentrokan dengan project lainnya.

## Implementasi Tugas 2

1. **Fungsi: folder `katalog` file `views.py`**
- Meng-import `CatalogItem` dari `katalog.models`.
- Membuat function `show_katalog` yang menerima parameter `request`.
- Membuat QuerySet `data_item_katalog` dalam function di atas dengan value `CatalogItem.objects.all()`.
- Membuat dictionary `context` dalam function di atas yang berisi pasangan key dan value untuk `item_list` (diisi `data_item_katalog`), nama, dan NPM.
- Membuat function di atas me-return function `render` dengan argument `request`, `"katalog.html"`, dan `context`.

2. **Routing: folder `katalog` file `urls.py`**
- Meng-import `path` dari `django.urls` dan `show_katalog` dari `katalog.views`.
- Membuat variable `app_name` dengan value `'katalog'`.
- Membuat list urls_pattern yang berisi function `path` dengan argument `''`, `show_katalog`, dan `name='show_katalog'`.

3. **Pemetaan Data: folder `katalog/templates` file `katalog.html`**
- Menggunakan syntax Django `{{}}` untuk memetakan nama dan NPM.
- Menggunakan syntax Django `{% %}` untuk membuat for loop untuk setiap item dalam `item_list`.
- Menggunakan syntax Django `{{}}` dan HTML `<tr>` `<th>` dalam loop untuk memetakan keterangan tiap item (dari folder `fixtures` file `initial_catalog_data.json`) pada tabel.

4. **Daftar App dan Deploy ke Heroku**
- Pada folder `project_django` file `urls.py`, menambahkan function `path` dengan argument `'katalog/` dan function `include` dengan argument `'katalog.urls'`.
- Lakukan add-commit-push ke repository GitHub.
- Di repository GitHub, menambahkan variable repository secret `HEROKU_APP_NAME` DAN `HEROKU_API_KEY`, kemudian jalankan kembali workflow.