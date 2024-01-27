class Pasien:
    def _init_(self, nama, umur, alamat, metode_pembayaran, poli, faskes_asal):
        self.nama = nama
        self.umur = umur
        self.__alamat = alamat
        self.__metode_pembayaran = metode_pembayaran
        self._poli = poli
        self._faskes_asal = faskes_asal

    def public_pasien(self):
        print("Nama pasien yang terdaftar:", self.nama)
        print("Umur pasien yang terdaftar:", self.umur)

    def _protected_poli_dan_faskesasal(self):
        print("Dokumen untuk rumah sakit:")
        print("Nama pasien:", self.nama)
        print("Umur pasien:", self.umur)
        print("Pasien merujuk ke poli:", self._poli)
        print("Asal faskes pasien:", self._faskes_asal)

    def __privat_alamat_dan_metodepembayaran(self):
        print("Hanya tenaga medis dan rumah sakit yang tahu:")
        print("Alamat pasien yang terdaftar:", self.__alamat)
        print("Metode pembayaran pasien:", self.__metode_pembayaran)

    def akses_method_protected(self):
        self._protected_poli_dan_faskesasal()

    def akses_method_privat(self):
        self.__privat_alamat_dan_metodepembayaran()


a = "Nama Pasien"
b = 25
c = "Alamat Pasien"
d = "Metode Pembayaran"
e = "Poli Tujuan"
f = "Faskes Rujukan"

psn1 = Pasien(a, b, c, d, e, f)

print('Akses Method Public:')
psn1.public_pasien()
print('\nAkses Method Protected:')
psn1.akses_method_protected()
print('\nAkses Method Private:')
psn1.akses_method_privat()