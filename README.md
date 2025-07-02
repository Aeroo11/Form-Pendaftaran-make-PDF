# Aplikasi Pendaftaran Mahasiswa Baru - Tech Edition

Aplikasi web modern untuk pendaftaran mahasiswa baru, dilengkapi fitur upload foto dan cetak daftar siswa ke PDF. Dibangun dengan **Python Flask** dan **MySQL**.

---

## 🎓 Tugas Pemrograman Web: Sistem Laporan Siswa - Implementasi FPDF

![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## Deskripsi Proyek

Proyek ini merupakan implementasi sistem cetak laporan data siswa berbasis web dengan output PDF untuk SMK Negeri 2 Langsa. Sistem ini memungkinkan pengguna untuk menampilkan, menambah, dan mencetak data siswa kelas IX jurusan Rekayasa Perangkat Lunak dalam format PDF.

![image](https://github.com/user-attachments/assets/1c150a0b-c1ff-440e-b3f8-c5d819a32265)

![image](https://github.com/user-attachments/assets/6c8d8c71-99cb-4c93-b1aa-c7bd97052c25)


## 📋 Fitur

- ✅ Menampilkan daftar siswa dalam tampilan tabel
- ✅ Menambahkan data siswa baru ke dalam database
- ✅ Mencetak laporan daftar siswa dalam format PDF
- ✅ Antarmuka pengguna yang responsif dan mudah digunakan
- ✅ Upload foto profil siswa
- ✅ Pengelolaan data siswa (hapus & edit)

## 🛠️ Teknologi yang Digunakan

- **Backend:** PHP 7.4+
- **Database:** MySQL 5.7+
- **Library PDF:** FPDF
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Bootstrap 5
- **Antarmuka Responsif:** Media Queries

## 📁 Detail Implementasi

### Database

Database terdiri dari satu tabel yaitu `mahasiswa` dengan struktur sebagai berikut:

```sql
CREATE TABLE mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nim VARCHAR(20) NOT NULL,
    nama_lengkap VARCHAR(100) NOT NULL,
    no_hp VARCHAR(15) NOT NULL,
    tanggal_lahir DATE NOT NULL
);
```

### Koneksi Database

Koneksi database diimplementasikan di file `koneksi.php`:

```php
<?php
$server = "localhost";
$username = "root";
$password = "";
$database = "tutorial";

$connect = mysqli_connect($server, $username, $password, $database);

if (!$connect) {
    die("Connection failed: " . mysqli_connect_error());
}
?>
```

### Pembuatan PDF

Pembuatan PDF menggunakan library FPDF dengan implementasi sebagai berikut:

1. Membuat objek FPDF dan mengatur ukuran halaman A5 landscape
2. Menambahkan header dengan nama sekolah dan jurusan
3. Membuat tabel untuk menampilkan data siswa
4. Mengambil data dari database dan menampilkannya di tabel PDF
5. Output dokumen PDF ke browser

Contoh kode implementasi:

```php
// Buat objek FPDF
$pdf = new FPDF('L', 'mm', 'A5');
$pdf->AddPage();

// Header
$pdf->SetFont('Arial', 'B', 16);
$pdf->Cell(0, 10, 'SEKOLAH MENENGAH KEJURUAN NEGERI 2 LANGSA', 0, 1, 'C');
$pdf->SetFont('Arial', 'B', 12);
$pdf->Cell(0, 10, 'DAFTAR SISWA KELAS IX JURUSAN REKAYASA PERANGKAT LUNAK', 0, 1, 'C');

// Buat tabel
$pdf->SetFont('Arial', 'B', 10);
$pdf->Cell(25, 6, 'NIM', 1, 0, 'C');
$pdf->Cell(60, 6, 'NAMA MAHASISWA', 1, 0, 'C');
$pdf->Cell(35, 6, 'NO HP', 1, 0, 'C');
$pdf->Cell(30, 6, 'TANGGAL LHR', 1, 1, 'C');

// Isi tabel dari database
while ($row = mysqli_fetch_array($result)) {
    $pdf->Cell(25, 6, $row['nim'], 1, 0, 'C');
    $pdf->Cell(60, 6, $row['nama_lengkap'], 1, 0, 'L');
    $pdf->Cell(35, 6, $row['no_hp'], 1, 0, 'L');
    $pdf->Cell(30, 6, $row['tanggal_lahir'], 1, 1, 'C');
}

// Output PDF
$pdf->Output();
```

## 📥 Cara Instalasi

### Prasyarat
- Web server (XAMPP, WAMP, atau sejenisnya)
- PHP 7.4+
- MySQL 5.7+
- Library FPDF

### Langkah-langkah Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/username/sistem-laporan-siswa.git
   ```

2. **Pindahkan ke direktori web server**
   ```bash
   mv sistem-laporan-siswa /path/to/htdocs/
   ```

3. **Import database**
   - Buka phpMyAdmin
   - Buat database baru bernama `tutorial`
   - Import file `database/tutorial.sql`

4. **Konfigurasi koneksi database**
   - Buka file `koneksi.php`
   - Sesuaikan parameter koneksi dengan pengaturan server Anda

5. **Pastikan library FPDF terinstall**
   - Jika belum ada, download dari [fpdf.org](http://www.fpdf.org/)
   - Ekstrak dan letakkan di folder proyek

6. **Akses aplikasi**
   - Buka browser dan akses `http://localhost/sistem-laporan-siswa/`

## 🚀 Penggunaan

1. **Melihat Daftar Siswa**
   - Buka halaman utama aplikasi
   - Daftar siswa akan ditampilkan dalam bentuk tabel

2. **Menambah Data Siswa**
   - Klik tombol "Tambah Data Siswa"
   - Isi formulir dengan data siswa baru
   - Klik tombol "Simpan"

3. **Mencetak Laporan PDF**
   - Klik tombol "Cetak Laporan PDF"
   - Dokumen PDF akan dihasilkan dan diunduh otomatis

4. **Mengelola Data Siswa**
   - Untuk mengedit: Klik tombol "Edit" pada baris data yang ingin diubah
   - Untuk menghapus: Klik tombol "Hapus" pada baris data yang ingin dihapus

## 📄 Struktur File

/
├── app.py                  # File utama aplikasi Flask
├── /app                    # Paket aplikasi
│   ├── __init__.py         # Inisialisasi paket Flask
│   ├── routes.py           # Definisi rute aplikasi
│   └── /utils
│       └── pdf_generator.py # Utilitas pembuatan PDF (opsional)
├── /config
│   └── database.py         # Konfigurasi koneksi database
├── /static
│   ├── /css
│   │   └── style.css       # File styling utama
│   ├── /images             # Aset gambar (logo, dll)
│   └── /uploads            # Folder untuk menyimpan foto yang diunggah
├── /templates
│   ├── index.html          # Halaman utama (form pendaftaran)
│   ├── success.html        # Halaman notifikasi sukses
│   ├── daftar_siswa.html   # Halaman daftar siswa
│   └── /admin
│       └── pendaftar.html  # Halaman admin
└── README.md




