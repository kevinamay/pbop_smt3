class Pasien:
    def _init_(self, nama, umur, alamat,metode_pembayaran,poli,faskes_asal):
        self.nama = nama
        self.umur = umur
        self.__alamat = alamat
        self.__metode_pembayaran = metode_pembayaran
        self._poli=poli
        self._faskes_asal=faskes_asal

    def public_pasien(self):
        print("nama pasien yang terdaftar",self.nama,"umur pasien yang terdaftar",self.umur)
    def _protected_poli_dan_faskesasal(self):
        print("dokumen untuk rumah sakit")
        print("nama pasien",self.nama)
        print("umur pasien",self.umur)
        print("pasien merujuk ke poli",self._poli)
        print("asal faskes pasien ",self._faskes_asal)
    def __privat_alamat_dan_metodepembayaran(self):
        print("hanya tenaga medis dan rumah sakita yang tau")
        print("alamat pasien yang terdaftar",self.__alamat,"Metode pembayaran pasien",self.__metode_pembayaran)
        
    def akses_method_protected(self):
        self._protected_poli_dan_faskesasal()
    def akses_method_privat(self):
        self.__privat_alamat_dan_metodepembayaran()
        


psn1= Pasien(a,b,c,d,e,f)
print('Akses Method Public :')
psn1.public_pasien
print('Akses method protected :')
psn1.public_pasien()
print('Akses method protected :')
psn1.akses_method_protected()
print('Akses method protected :')
psn1.akses_method_privat()