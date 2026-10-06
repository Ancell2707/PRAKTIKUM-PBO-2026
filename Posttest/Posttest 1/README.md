Laporan Posttest 2 PBO

Nama: Muhammad Ancel Prinata
NIM: 2509106099
Judul: Sistem Reservasi Jadwal Potong Rambut Barbershop (RapiJaya Barbershop)

Penjelasan Program

Program ini lanjutan dari Posttest 1. Sistem reservasi RapiJaya Barbershop tetap jalan otomatis lewat blok simulasi di __main__, jadi gak perlu input manual di terminal. Bedanya, di Posttest 2 ini ditambah konsep pewarisan (inheritance), overriding method, komposisi, dan agregasi supaya struktur kodenya lebih rapi dan gak ada kode yang diulang-ulang.

Yang Baru di Posttest 2
Class induk Pengguna. Kapster, Pelanggan, dan AdminBarbershop sekarang turunan dari Pengguna, jadi data dasar (nama, no HP, ID otomatis seperti USR001) cukup ditulis sekali di induknya.
Overriding method. Method peran() dan tampilkan_info() ditulis ulang di tiap class turunan. Hasilnya beda-beda: Kapster tampil sebagai "Kapster", Pelanggan sebagai "Pelanggan", Admin sebagai "Admin". tampilkan_info() juga memanggil super() dulu baru nambah info khusus.
Class Pembayaran. Urusan pembayaran dipisah dari Reservasi. Kalau bayar di tempat statusnya "Belum Bayar", metode lain langsung "Lunas".
Class Barbershop. Ini nyimpan daftar kapster yang kerja di barbershop. Kapster bisa ditambah dan dikeluarkan, dan kalau objek barbershop dihapus, kapsternya tetap ada.
Method interaksi baru. Pelanggan.pesan_layanan() buat pesan langsung ke kapster, dan Kapster.layani_pelanggan() buat melayani sekaligus kasih poin ke pelanggan.
Pengecekan pewarisan. Di akhir program ada isinstance() dan issubclass() buat buktiin kalau tiga class tadi memang turunan Pengguna.
Fitur
Kelola Layanan & Promo: tambah layanan, ubah harga (ada validasi), hapus layanan, dan set diskon promo untuk semua layanan.
Manajemen Kapster: simpan data kapster (nama, spesialisasi, rating), jadwal yang terisi, dan hari libur.
Simulasi Reservasi: booking dicek dulu (hari valid, format jam HH:MM, metode bayar, kapster kosong atau tidak), lalu struk keluar otomatis.
Poin & Membership: pelanggan dapat poin dari kunjungan, dan kalau poinnya cukup otomatis naik jadi VIP (dapat diskon 10%).
Dashboard Admin: ubah jam operasional, atur libur kapster, lihat data dan riwayat pelanggan, serta laporan pendapatan dari transaksi yang lunas.
Daftar Kapster Barbershop (baru): tambah dan keluarkan kapster lewat class Barbershop.
Cara Menjalankan
Pastikan Python sudah terinstal di komputer.
Buka terminal, masuk ke folder tempat file berada.
Jalankan perintah python 2509106099-M-Ancel-Prinata-PT-2.py.

Programnya langsung jalan sendiri dan nampilin semua simulasi di layar, jadi gak perlu pilih menu.
Struktur Class
1. Pengguna (class induk) (baru)
Atribut: nama (protected, pakai property), no_hp (protected, pakai property), id_pengguna (private, pakai property), total_pengguna (class)
Method: peran(), tampilkan_info()
Static Method: validasi_no_hp()

2. Layanan

Atribut: nama, kategori, harga (private, pakai property), kategori_valid (class), registry (class), diskon_promo_persen (class)

Method: harga_setelah_promo(), tampilkan()

Class Method: tambah_layanan(), ubah_harga(), hapus_layanan(), set_promo(), daftar_semua()

Static Method: validasi_harga()

3. Kapster (turunan Pengguna)

Atribut: spesialisasi, jadwal_terisi, hari_libur, rating (private, pakai property), nama_barbershop (class), jam_operasional (class), total_kapster (class)

Method: tambah_jadwal(), tambah_hari_libur(), cek_ketersediaan(), slot_kosong(), peran() dan tampilkan_info() (override), layani_pelanggan() (baru)

Class Method: dari_dict(), ubah_jam_operasional()

Static Method: generate_slot_jam()

4. Pelanggan (turunan Pengguna)

Atribut: status_member, preferensi_gaya, riwayat_kunjungan, saldo_poin (private, pakai property), total_pelanggan (class), syarat_poin_redeem (class), member_default (class)

Method: tambah_poin(), catat_kunjungan(), tampilkan_riwayat(), peran() dan tampilkan_info() (override), pesan_layanan() (baru)

Class Method: dari_dict(), ubah_syarat_poin_redeem()

5. Pembayaran (baru)

Atribut: metode, status, metode_valid (class)

Method: lunasi(), ringkasan()

6. Reservasi

Atribut: pelanggan, kapster, layanan, hari, jam, pembayaran (objek Pembayaran), status (private, pakai property), nomor_antrian, total_reservasi (class), denda_pembatalan (class), status_valid (class), antrian_per_hari (class)

Method: hitung_biaya(), konfirmasi(), selesaikan(), kirim_notifikasi(), tampilkan_struk()

Class Method: buat_reservasi_baru(), ubah_denda_pembatalan()

Static Method: validasi_format_jam(), validasi_hari()

Catatan: metode_pembayaran dan status_pembayaran sekarang diambil dari objek Pembayaran lewat property.

7. Barbershop (baru)

Atribut: nama, alamat, _kapster (list)

Method: tambah_kapster(), keluarkan_kapster(), tampilkan_daftar_kapster(), total_kapster (property)

8. AdminBarbershop (turunan Pengguna)

Atribut: level_akses, daftar_kapster, daftar_pelanggan, daftar_reservasi, admin_default (class), total_login (class)

Method: atur_jam_operasional(), tambah_hari_libur_kapster(), lihat_semua_pelanggan(), laporan_pendapatan(), peran() dan tampilkan_info() (override)

Static Method: cek_username()

Hubungan Antar Class
Pewarisan (baru): Kapster, Pelanggan, dan AdminBarbershop adalah turunan dari Pengguna.
Komposisi (baru): Reservasi bikin objek Pembayaran sendiri di dalamnya. Kalau reservasinya hilang, pembayarannya ikut hilang.
Agregasi (baru): Barbershop punya banyak Kapster, tapi kapster bisa tetap ada walau barbershop-nya dihapus.
Asosiasi: Reservasi menghubungkan Pelanggan, Kapster, dan Layanan jadi satu transaksi.
Kontrol terpusat: AdminBarbershop pegang daftar kapster, pelanggan, dan reservasi buat atur jadwal, lihat riwayat, dan hitung laporan pendapatan.