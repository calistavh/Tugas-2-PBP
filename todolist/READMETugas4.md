# Pemrograman Berbasis Platform - Tugas 4

Nama: Calista Vimalametta Heryadi<br>
NPM: 2106630473<br>
Kelas: C

---

## Link App Heroku

<https://tgs-pbp.herokuapp.com/todolist/>

---

## {% csrf_token %} pada \<form\>

CSRF token adalah bentuk perlindungan terhadap serangan Cross Site Request Forgery (CSRF) berupa string random. CSRF token di-generate server ketika client mengakses form dengan `{% csrf_token %}`, kemudian token tersebut dimasukkan ke sebuah field tersembunyi dalam form dan disimpan oleh server. Saat client mengumpulkan form, server membandingkan token dari form dengan token yang disimpan. Jika sama, server memproses request client. Jika tidak sama atau tidak ada, server menolak request client dengan error 403 Forbidden.

---

## Membuat \<form\> secara Manual

Form dapat dibuat secara manual menggunakan tag `<input>` untuk setiap field. Attribute `<input>` diantaranya:
- `type`: jenis field seperti text, password (karakter disembunyikan), submit (tombol pengumpulan), dll.
- `name`: nama yang bersesuaian dengan attribute di class Form.
- `placeholder` atau `value`: teks yang ditampilkan pada field yang masih kosong atau tombol.
<p>Setelah dikumpulkan, data tersebut diperoleh dengan `request.POST` dan dimasukkan ke constructor class Form seperti biasa.</p>

---

## Alur Data dari Form ke Template

1. Setelah form dikumpulkan, data dari form dimasukkan ke constructor class Form dengan `<FormName>(request.POST)`.
2. Object tersebut dicek kevalidannya. Jika iya (dan semua data yang bersesuaian dengan attribute model lengkap), object tersebut dapat di-`.save()`.
3. `save` menyimpan object ke dalam database `model` yang tertera dalam class Form tersebut.
4. Semua object dalam database model dapat diambil dengan `<ModelName>.objects.all()` dan dimasukkan ke dalam context untuk ditampilkan di halaman.
5. Sintaks Django dalam file HTML seperti `{% for ... %}`, `{% if ... %} ` dsb. menentukan bagaimana object-object tersebut ditampilkan.

---

## Implementasi Tugas 4

### Membuat aplikasi todolist
1. **cmd:** `python manage.py startapp todolist`.
2. **project_django/settings.py:** tambah `todolist` di list `INSTALLED_APPS`.
3. **todolist:** buat folder `templates` dan file `todolist.html` di dalamnya.
4. **todolist/views.py:** buat function `show_todolist`.

### Menambahkan path todolist
1. **todolist:** buat file `urls.py`.
2. **todolist/urls.py:** tambah import, `app_name`, dan `urlpatterns` berisi path ke function `show_todolist`.
3. **project_django/urls.py:** tambah path ke aplikasi todolist di `urlpatterns`.

### Membuat model Task
1. **todolist/models.py:** tambah import dan class `Task` dengan attribute `user`, `date`, `title`, dan `description`.
2. **cmd:** `python manage.py makemigrations`.
3. **cmd:** `python manage.py migrate`.

### (NEW) Membuat fitur registrasi, login, dan logout
1. **todolist/views.py:** tambah import dan function `register`, `login_user`, dan `logout_user` (mengikuti petunjuk Lab 3).
2. **todolist/templates:** buat file `register.html` dan `login.html` (mengikuti petunjuk Lab 3).
3. **todolist/views.py:** tambah import dan `@login_required` di atas function `show_todolist` dan `create_task` (mengikuti petunjuk Lab 3).

### (NEW) Melengkapi halaman todolist
1. **todolist/templates/todolist.html:** tambah tag-tag Django dan HTML untuk menampilkan:
- username.
- tombol logout.
- tabel task (hanya menampilkan task buatan user yang sedang log in).
- tombol tambah task (saat ini belum berfungsi).
2. **todolist/views.py:** tambah dict `context` berisikan `user` dan `username` yang sedang log in dan semua `tasks` dari database untuk ditampilkan.

### (NEW) Membuat fitur tambah task
1. **todolist:** buat file `forms.py`.
2. **todolist/forms.py:** tambah import `ModelForm` dan `Task`, lalu tambah class `TaskForm`, yaitu form untuk model `Task` (mengikuti dokumentasi ModelForm Django):
- meminta input `title` dan `description`.
- `date` akan diisi secara otomatis.
- `user` tidak perlu diberi input (`exclude`).
3. **todolist/views.py:** tambah import `TaskForm` dan function `create_task` yang mirip seperti function `register` dengan tambahan:
- isi attribute `user` dengan user yang sedang log in.
4. **todolist/templates:** buat file `create_task.html` yang mirip seperti `register.html` (dengan `{{form.as_table}}`).
5. **todolist/templates/todolist.html:** menambahkan link pada tombol tambah task ke `create_task`.

### Routing
1. **todolist/urls.py:** tambah path ke `register`, `login`, `logout`, dan `create_task` di `urlpatterns`.