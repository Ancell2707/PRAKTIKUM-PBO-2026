import re

HARI_VALID = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]


class Layanan:
    kategori_valid = ["Potong Rambut", "Cukur", "Cuci Rambut", "Paket Perawatan"]
    registry = {}
    diskon_promo_persen = 0

    def __init__(self, nama, harga, kategori):
        self.nama = nama
        self.kategori = kategori
        self.__harga = 0
        self.harga = harga
        Layanan.registry[nama.lower()] = self

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("harga harus lebih dari 0")
        self.__harga = harga_baru

    def harga_setelah_promo(self):
        return int(self.__harga * (1 - Layanan.diskon_promo_persen / 100))

    def tampilkan(self):
        harga_final = self.harga_setelah_promo()
        promo_info = f" (promo {Layanan.diskon_promo_persen}%)" if Layanan.diskon_promo_persen else ""
        print(f"{self.nama} ({self.kategori}) - Rp{harga_final:,}{promo_info}")

    @classmethod
    def tambah_layanan(cls, nama, harga, kategori):
        if kategori not in cls.kategori_valid:
            print(f"kategori '{kategori}' gak dikenal")
            return None
        return cls(nama, harga, kategori)

    @classmethod
    def ubah_harga(cls, nama, harga_baru):
        layanan = cls.registry.get(nama.lower())
        if not layanan:
            print("layanan gak ketemu")
            return
        try:
            layanan.harga = harga_baru
        except ValueError as e:
            print("gagal ubah harga:", e)

    @classmethod
    def hapus_layanan(cls, nama):
        key = nama.lower()
        if key in cls.registry:
            del cls.registry[key]
        else:
            print("layanan gak ketemu")

    @classmethod
    def set_promo(cls, persen):
        cls.diskon_promo_persen = persen

    @classmethod
    def daftar_semua(cls):
        return list(cls.registry.values())

    @staticmethod
    def validasi_harga(harga):
        return isinstance(harga, (int, float)) and harga > 0


class Kapster:
    nama_barbershop = "RapiJaya Barbershop"
    jam_operasional = "09:00 - 21:00"
    total_kapster = 0

    def __init__(self, nama, spesialisasi, rating_awal=5.0):
        self.nama = nama
        self.spesialisasi = spesialisasi
        self.jadwal_terisi = []  
        self.hari_libur = []
        self.__rating = rating_awal
        Kapster.total_kapster += 1

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating_baru):
        if not (0 <= rating_baru <= 5):
            print(f"rating {rating_baru} gak valid, harus 0-5")
            return
        self.__rating = rating_baru

    def tambah_jadwal(self, hari, jam):
        self.jadwal_terisi.append((hari, jam))

    def tambah_hari_libur(self, hari):
        if hari not in self.hari_libur:
            self.hari_libur.append(hari)

    def cek_ketersediaan(self, hari, jam):
        if hari in self.hari_libur:
            return False
        return (hari, jam) not in self.jadwal_terisi

    def slot_kosong(self, hari):
        if hari in self.hari_libur:
            return []
        semua_slot = Kapster.generate_slot_jam()
        return [j for j in semua_slot if (hari, j) not in self.jadwal_terisi]

    def tampilkan_profil(self):
        print(f"Kapster: {self.nama} | Spesialisasi: {self.spesialisasi} "
              f"| Rating: {self.rating}/5 | Hari libur: {self.hari_libur or '-'}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["spesialisasi"], data.get("rating", 5.0))

    @classmethod
    def ubah_jam_operasional(cls, jam_baru):
        cls.jam_operasional = jam_baru

    @staticmethod
    def generate_slot_jam(jam_operasional_str=None):
        if jam_operasional_str is None:
            jam_operasional_str = Kapster.jam_operasional
        buka, tutup = jam_operasional_str.split(" - ")
        jam_buka = int(buka.split(":")[0])
        jam_tutup = int(tutup.split(":")[0])
        return [f"{j:02d}:00" for j in range(jam_buka, jam_tutup)]


class Pelanggan:
    total_pelanggan = 0
    syarat_poin_redeem = 100
    member_default = "Reguler"

    def __init__(self, nama, no_hp, saldo_poin_awal=0):
        self.nama = nama
        self.no_hp = no_hp
        self.status_member = Pelanggan.member_default
        self.preferensi_gaya = None
        self.riwayat_kunjungan = []
        self.__saldo_poin = 0
        self.saldo_poin = saldo_poin_awal
        Pelanggan.total_pelanggan += 1

    @property
    def saldo_poin(self):
        return self.__saldo_poin

    @saldo_poin.setter
    def saldo_poin(self, poin_baru):
        if poin_baru < 0:
            raise ValueError("saldo poin tidak boleh negatif")
        self.__saldo_poin = poin_baru

    def tambah_poin(self, jumlah):
        if jumlah <= 0:
            print("jumlah poin harus lebih dari 0")
            return
        self.saldo_poin = self.saldo_poin + jumlah
        if self.saldo_poin >= Pelanggan.syarat_poin_redeem:
            self.status_member = "VIP"

    def catat_kunjungan(self, reservasi):
        self.riwayat_kunjungan.append(reservasi)

    def tampilkan_info(self):
        print(f"Pelanggan: {self.nama} | No HP: {self.no_hp} | Poin: {self.saldo_poin} "
              f"| Status: {self.status_member} | Gaya favorit: {self.preferensi_gaya or '-'}")

    def tampilkan_riwayat(self):
        if not self.riwayat_kunjungan:
            print("  belum ada riwayat kunjungan")
            return
        for r in self.riwayat_kunjungan:
            print(f"  - {r.hari} {r.jam} | {r.layanan.nama} | kapster {r.kapster.nama} | {r.status}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["nama"], data["no_hp"], data.get("saldo_poin", 0))

    @classmethod
    def ubah_syarat_poin_redeem(cls, syarat_baru):
        cls.syarat_poin_redeem = syarat_baru

    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.isdigit() and len(no_hp) >= 10


class Reservasi:
    total_reservasi = 0
    denda_pembatalan = 10000
    status_valid = ["menunggu", "dikonfirmasi", "selesai", "dibatalkan"]
    metode_pembayaran_valid = ["Transfer Bank", "E-Wallet", "QRIS", "Bayar di Tempat"]
    antrian_per_hari = {}

    def __init__(self, pelanggan, kapster, layanan, hari, jam, metode_pembayaran):
        self.pelanggan = pelanggan
        self.kapster = kapster
        self.layanan = layanan
        self.hari = hari
        self.jam = jam
        self.metode_pembayaran = metode_pembayaran
        self.status_pembayaran = "Belum Bayar" if metode_pembayaran == "Bayar di Tempat" else "Lunas"
        self.__status = "menunggu"

        self.kapster.tambah_jadwal(hari, jam)
        Reservasi.total_reservasi += 1
        Reservasi.antrian_per_hari[hari] = Reservasi.antrian_per_hari.get(hari, 0) + 1
        self.nomor_antrian = Reservasi.antrian_per_hari[hari]
        pelanggan.catat_kunjungan(self)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru not in Reservasi.status_valid:
            print(f"status '{status_baru}' gak dikenal")
            return
        self.__status = status_baru

    def hitung_biaya(self):
        harga = self.layanan.harga_setelah_promo()
        if self.pelanggan.status_member == "VIP":
            harga = int(harga * 0.9)
        return harga

    def konfirmasi(self):
        self.status = "dikonfirmasi"

    def selesaikan(self):
        self.status = "selesai"
        self.pelanggan.tambah_poin(20)

    def kirim_notifikasi(self):
        print(f"[Notifikasi WhatsApp ke {self.pelanggan.no_hp}] Halo {self.pelanggan.nama}, "
              f"reminder jadwal kamu hari {self.hari} jam {self.jam} bersama {self.kapster.nama}.")

    def tampilkan_struk(self):
        print("=" * 45)
        print(f"{Kapster.nama_barbershop} - Jam Operasional: {Kapster.jam_operasional}")
        print("-" * 45)
        print(f"No. Antrian   : {self.nomor_antrian} ({self.hari})")
        print(f"Pelanggan     : {self.pelanggan.nama}")
        print(f"Kapster       : {self.kapster.nama}")
        print(f"Layanan       : {self.layanan.nama}")
        print(f"Hari, Jam     : {self.hari}, {self.jam}")
        print(f"Status        : {self.status}")
        print(f"Pembayaran    : {self.metode_pembayaran} ({self.status_pembayaran})")
        print(f"Total         : Rp{self.hitung_biaya():,}")
        print("=" * 45)

    @classmethod
    def buat_reservasi_baru(cls, pelanggan, kapster, layanan, hari, jam, metode_pembayaran):
        if not Reservasi.validasi_hari(hari):
            print(f"hari '{hari}' gak valid")
            return None
        if not Reservasi.validasi_format_jam(jam):
            print(f"format jam '{jam}' salah, harus HH:MM")
            return None
        if metode_pembayaran not in cls.metode_pembayaran_valid:
            print(f"metode pembayaran '{metode_pembayaran}' gak dikenal")
            return None
        if not kapster.cek_ketersediaan(hari, jam):
            print(f"kapster {kapster.nama} udah ada jadwal di {hari} jam {jam}")
            return None
        return cls(pelanggan, kapster, layanan, hari, jam, metode_pembayaran)

    @classmethod
    def ubah_denda_pembatalan(cls, denda_baru):
        cls.denda_pembatalan = denda_baru

    @staticmethod
    def validasi_format_jam(jam_str):
        return bool(re.match(r'^([01]\d|2[0-3]):[0-5]\d$', jam_str))

    @staticmethod
    def validasi_hari(hari):
        return hari.capitalize() in HARI_VALID


class AdminBarbershop:
    admin_default = "admin"
    total_login = 0

    def __init__(self, daftar_kapster, daftar_pelanggan, daftar_reservasi):
        self.daftar_kapster = daftar_kapster
        self.daftar_pelanggan = daftar_pelanggan
        self.daftar_reservasi = daftar_reservasi
        AdminBarbershop.total_login += 1

    def atur_jam_operasional(self, jam_baru):
        Kapster.ubah_jam_operasional(jam_baru)
        print(f"jam operasional diubah jadi {jam_baru}")

    def tambah_hari_libur_kapster(self, kapster, hari):
        if not Reservasi.validasi_hari(hari):
            print("hari gak valid")
            return
        kapster.tambah_hari_libur(hari)
        print(f"{kapster.nama} sekarang libur di hari {hari}")

    def lihat_semua_pelanggan(self):
        if not self.daftar_pelanggan:
            print("belum ada pelanggan")
            return
        for p in self.daftar_pelanggan:
            p.tampilkan_info()
            p.tampilkan_riwayat()

    def laporan_pendapatan(self):
        lunas = [r for r in self.daftar_reservasi if r.status_pembayaran == "Lunas"]
        belum = [r for r in self.daftar_reservasi if r.status_pembayaran != "Lunas"]
        total = sum(r.hitung_biaya() for r in lunas)
        print(f"Transaksi lunas   : {len(lunas)}")
        print(f"Belum bayar       : {len(belum)}")
        print(f"Total pendapatan  : Rp{total:,}")
        return total

    @staticmethod
    def cek_username(username):
        return username.strip().lower() == AdminBarbershop.admin_default


if __name__ == "__main__":
    print(f"=== {Kapster.nama_barbershop} ===")

    kapster1 = Kapster("Andi", "Fade & Undercut", 4.9)
    kapster2 = Kapster.dari_dict({"nama": "Rian", "spesialisasi": "Classic Cut", "rating": 4.8})
    kapster3 = Kapster.dari_dict({"nama": "Doni", "spesialisasi": "Kids Cut", "rating": 4.7})
    daftar_kapster = [kapster1, kapster2, kapster3]

    layanan1 = Layanan.tambah_layanan("Potong Rambut", 25000, "Potong Rambut")
    layanan2 = Layanan.tambah_layanan("Cukur Jenggot", 15000, "Cukur")
    layanan3 = Layanan.tambah_layanan("Cuci Rambut", 20000, "Cuci Rambut")
    layanan4 = Layanan.tambah_layanan("Hair Spa", 50000, "Paket Perawatan")

    daftar_pelanggan = []
    daftar_reservasi = []

    print("\n--- DAFTAR KAPSTER ---")
    for k in daftar_kapster:
        k.tampilkan_profil()

    print("\n--- DAFTAR LAYANAN ---")
    for l in Layanan.daftar_semua():
        l.tampilkan()

    print("\n--- SIMULASI RESERVASI 1 ---")
    p1 = Pelanggan("Budi Santoso", "081234567890")
    p1.preferensi_gaya = "Two Block"
    daftar_pelanggan.append(p1)

    r1 = Reservasi.buat_reservasi_baru(p1, kapster1, layanan1, "Senin", "10:00", "QRIS")
    if r1:
        daftar_reservasi.append(r1)
        r1.konfirmasi()
        r1.selesaikan()
        r1.tampilkan_struk()
        r1.kirim_notifikasi()

    print("\n--- SIMULASI RESERVASI 2 ---")
    p2 = Pelanggan.dari_dict({"nama": "Siti Aminah", "no_hp": "089876543210", "saldo_poin": 90})
    daftar_pelanggan.append(p2)

    r2 = Reservasi.buat_reservasi_baru(p2, kapster2, layanan4, "Senin", "11:00", "Bayar di Tempat")
    if r2:
        daftar_reservasi.append(r2)
        r2.konfirmasi()
        r2.tampilkan_struk()

    print("\n--- DASHBOARD ADMIN ---")
    admin = AdminBarbershop(daftar_kapster, daftar_pelanggan, daftar_reservasi)

    print("\n[Admin] Mengatur Jam Operasional Baru & Libur Kapster:")
    admin.atur_jam_operasional("08:00 - 22:00")
    admin.tambah_hari_libur_kapster(kapster3, "Minggu")

    print("\n[Admin] Menambahkan Promo Diskon Layanan (10%):")
    Layanan.set_promo(10)
    for l in Layanan.daftar_semua():
        l.tampilkan()

    print("\n[Admin] Data Seluruh Pelanggan & Riwayat:")
    admin.lihat_semua_pelanggan()

    print("\n[Admin] Laporan Pendapatan:")
    admin.laporan_pendapatan()

    print(f"\nTotal reservasi tercatat: {Reservasi.total_reservasi}")