# SISTEM MANAJEMEN PERPUSTAKAAN

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk membantu pengelolaan data buku perpustakaan. Aplikasi ini menerapkan konsep Model-View-Controller (MVC) untuk memisahkan pengelolaan data, tampilan antarmuka, dan proses aplikasi.

Aplikasi menggunakan database MySQL sebagai tempat penyimpanan data dan CustomTkinter untuk membangun tampilan antarmuka.

## 2. Struktur Direktori MVC

```text
modul3/
├── controllers/
│   └── buku_controller.py
├── models/
│   └── buku_model.py
├── views/
│   └── ...
├── tests/
│   ├── test_buku.py
│   └── ...
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Penjelasan Struktur

- **Models:** Mengelola data dan komunikasi dengan database.
- **Views:** Mengatur tampilan antarmuka aplikasi.
- **Controllers:** Mengatur proses dan menghubungkan model dengan tampilan.
- **Tests:** Menyimpan kode pengujian aplikasi.
- **main.py:** File utama untuk menjalankan aplikasi.
- **requirements.txt:** Daftar library yang dibutuhkan aplikasi.

## 3. Instalasi dan Konfigurasi Database MySQL

### Persiapan

- Python
- Visual Studio Code
- Git
- Laragon
- MySQL

### Instalasi Dependensi

Jalankan perintah berikut pada terminal:

```bash
pip install -r requirements.txt
```

### Konfigurasi Database

1. Buka aplikasi Laragon.
2. Jalankan layanan MySQL.
3. Buka phpMyAdmin atau pengelola database MySQL.
4. Buat database dengan nama yang sesuai dengan konfigurasi aplikasi.
5. Pastikan konfigurasi host, username, password, dan database sudah benar.

## 4. Cara Menjalankan Aplikasi

Aktifkan virtual environment, kemudian jalankan:

```bash
python main.py
```

Pastikan MySQL sudah aktif sebelum membuka aplikasi.

## 5. Pengujian Aplikasi

Untuk menjalankan unit testing:

```bash
pytest -v
```

Untuk memeriksa kualitas kode menggunakan Flake8:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

## 6. Packaging Aplikasi

Aplikasi dapat dikemas menjadi file executable menggunakan PyInstaller:

```bash
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

Hasil aplikasi executable berada di folder `dist/`.
