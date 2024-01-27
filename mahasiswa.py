#membuat class mahasiswa
from pert3 import mobil
from kucing import kucing
class Mahasiswa :
    def __init__(self,nim , nama , prodi , alamat, mobil,kucing):
       self.nim = nim
       self.nama = nama 
       self.prodi = prodi
       self.alamat = alamat
       self.mobil = mobil
       self.kucing = kucing
       
    def perkenalan(self):
        print('perkenalkan nama saya:',self.nama)
        print('nomor pokok mahasiwa:',self.nim)
        print('prodi saya:',self.prodi)
        print('alamat saya :',self.alamat)
        print('merk mobil:',self.mobil.merk)
        print('warna mobil:',self.mobil.warna)
        print('tahun mobil:',self.mobil.tahun)
        print('saya mempunyai kucing bernama:',self.kucing.nama)
 
 #class mahasiswa menggunkan atribut dari class mobil       


 #panggil methodnya
