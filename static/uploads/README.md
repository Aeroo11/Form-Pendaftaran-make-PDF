# 📁 Folder Uploads

Folder ini digunakan untuk menyimpan foto profil siswa yang diunggah melalui form pendaftaran.

## 📋 Informasi Penting

- Pastikan folder ini memiliki permission yang tepat (writable oleh web server)
- Hanya file gambar yang diizinkan (.jpg, .jpeg, .png, .gif)
- Ukuran maksimum file: 2MB
- File akan direname secara otomatis dengan format: [random-id]_[original-filename]

## 🔧 Troubleshooting

Jika terjadi error saat upload:

1. Periksa permission folder: `chmod 755 uploads` (Linux/Mac)
2. Pastikan `php.ini` mengizinkan file upload:  
   ```
   file_uploads = On
   upload_max_filesize = 2M
   post_max_size = 8M
   ```
3. Pastikan folder ini ada di struktur proyek

## 🧹 Maintenance

File upload yang tidak terpakai akan dibersihkan secara otomatis ketika data siswa dihapus dari database.
