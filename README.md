# Pendaftaran Siswa + Cetak PDF

Aplikasi web pendaftaran siswa: isi formulir, unggah foto profil, kelola data
(edit/hapus), lalu **cetak daftar siswa ke PDF**. Tugas mata kuliah Pemrograman Web.

![Form](https://github.com/user-attachments/assets/1c150a0b-c1ff-440e-b3f8-c5d819a32265)
![Laporan PDF](https://github.com/user-attachments/assets/96845c85-87d8-43e4-845c-580ab63a0c9d)

## Fitur
- Form pendaftaran dengan upload foto (nama file diacak dengan UUID)
- Daftar siswa dalam tabel, edit dan hapus data
- Ekspor laporan ke PDF (`app/utils/pdf_generator.py`, FPDF)

## Teknologi
Python · Flask · MySQL (`mysql-connector-python`) · FPDF · HTML/CSS

## Cara menjalankan
1. Jalankan MySQL (misalnya lewat XAMPP), lalu buat database sesuai konfigurasi di `app/__init__.py`.
2. Instal dependensi dan jalankan:
   ```bash
   python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   python app.py
   ```
3. Buka http://localhost:5000

## Struktur
```
├── app.py
├── app/
│   ├── routes.py
│   └── utils/pdf_generator.py
├── static/         # css, images, uploads/ (tidak di-commit)
└── templates/
```
