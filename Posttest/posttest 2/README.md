# Laporan Posttest 1 PBO

**Nama:** Muhammad Ancel Prinata  
**NIM:** 2509106099  
**Judul:** Sistem Reservasi Jadwal Potong Rambut Barbershop (RapiJaya Barbershop)

### Penjelasan Program:
Program ini merupakan pembaruan dari sistem reservasi jadwal potong rambut RapiJaya Barbershop yang menerapkan konsep Pemrograman Berorientasi Objek (OOP) secara komprehensif. Pada versi ini, alur pengujian dirancang menggunakan blok simulasi otomatis di dalam fungsi utama (__main__). Program mendemonstrasikan secara langsung kapabilitas sistem—mulai dari pendaftaran kapster dan layanan, simulasi reservasi pelanggan, pengaturan diskon promo, hingga laporan pendapatan admin—tanpa memerlukan input interaktif manual di terminal.

### Fitur:
1. Kelola Layanan & Promo: Menambah layanan baru, mengubah harga dengan validasi, menghapus layanan, dan menetapkan diskon promo secara global untuk seluruh layanan.

2. Manajemen Kapster: Menyimpan data kapster (nama, spesialisasi, rating), mengelola jadwal yang terisi, serta mengatur hari libur masing-masing kapster.

3. Simulasi Reservasi: Memproses booking pelanggan dengan validasi ketat (hari valid, format jam HH:MM, metode pembayaran, dan ketersediaan slot kapster) serta mencetak struk transaksi otomatis.

4. Sistem Poin & Membership: Pelanggan mengumpulkan poin dari kunjungan yang diselesaikan, yang secara otomatis dapat meningkatkan status keanggotaan menjadi VIP.

 5. Dashboard Admin: Fitur kontrol tingkat lanjut bagi admin untuk mengubah jam operasional barbershop, menetapkan hari libur kapster, melihat seluruh data dan riwayat pelanggan, serta menghasilkan laporan pendapatan transaksi lunas.

### Cara Menjalankan:
1. Pastikan Python sudah terinstal di komputer.
2. Buka terminal, arahkan ke folder tempat file berada.
3. Jalankan perintah `python 2509106099-M-Ancel-Prinata-PT-1.py`.
4. Pilih menu 1 untuk booking (pelanggan) atau 2 untuk dashboard admin, ikuti instruksi input yang muncul di layar.

### Struktur Class:

**1. Layanan**

Atribut: nama, kategori, harga (private, menggunakan property), kategori_valid (class attribute), registry (class attribute), diskon_promo_persen (class attribute)

Method: harga_setelah_promo(), tampilkan()

Class Method: tambah_layanan(), ubah_harga(), hapus_layanan(), set_promo(), daftar_semua()

Static Method: validasi_harga()

**2. Kapster**

Atribut: nama, spesialisasi, jadwal_terisi, hari_libur, rating (private, menggunakan property), nama_barbershop (class), jam_operasional (class), total_kapster (class)

Method: tambah_jadwal(), tambah_hari_libur(), cek_ketersediaan(), slot_kosong(), tampilkan_profil()

Class Method: dari_dict(), ubah_jam_operasional()

Static Method: generate_slot_jam()

**3. Pelanggan**

Atribut: nama, no_hp, status_member, preferensi_gaya, riwayat_kunjungan, saldo_poin (private, menggunakan property), total_pelanggan (class), syarat_poin_redeem (class), member_default (class)

Method: tambah_poin(), catat_kunjungan(), tampilkan_info(), tampilkan_riwayat()

Class Method: dari_dict(), ubah_syarat_poin_redeem()

Static Method: validasi_no_hp()

**4. Reservasi**

Atribut: pelanggan, kapster, layanan, hari, jam, metode_pembayaran, status_pembayaran, status (private, menggunakan property), nomor_antrian, total_reservasi (class), denda_pembatalan (class), status_valid (class), metode_pembayaran_valid (class), antrian_per_hari (class)

Method: hitung_biaya(), konfirmasi(), selesaikan(), kirim_notifikasi(), tampilkan_struk()

Class Method: buat_reservasi_baru(), ubah_denda_pembatalan()

Static Method: validasi_format_jam(), validasi_hari()

**5. AdminBarbershop**

Atribut: daftar_kapster, daftar_pelanggan, daftar_reservasi, admin_default (class), total_login (class)

Method: atur_jam_operasional(), tambah_hari_libur_kapster(), lihat_semua_pelanggan(), laporan_pendapatan()

Static Method: cek_username()

**hubungan Antar Class:**
Komposisi / Asosiasi (Reservasi sebagai penghubung): Class Reservasi berelasi langsung dengan objek Pelanggan, Kapster, dan Layanan guna menggabungkan entitas-entitas tersebut ke dalam satu transaksi pemesanan yang utuh.

Kontrol Terpusat (AdminBarbershop): Class AdminBarbershop berada di lapisan pengelola tertinggi, yang menerima kumpulan objek (daftar_kapster, daftar_pelanggan, daftar_reservasi) untuk memanipulasi jadwal, memantau riwayat kunjungan, serta mengalkulasi laporan keuangan secara global.