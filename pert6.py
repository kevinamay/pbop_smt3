class pegawai :
    Jumlah=0
    def __init__(self,NIK,nama,gaji,jml_lembur) :
        self.NIK = NIK
        self.nama = nama
        self.gaji=gaji
        self.jml_lembur = jml_lembur
        
    def tampilkan_jumlah(self):
        print('total pegawai=',pegawai.Jumlah)
    def tampilkan_pegawai(self):
        print('NIK    :',self.NIK)
        
        print('Nama   :',self.nama)
        print('Gaji   :',self.gaji)
        print('Jumlah lembur :',self.jml_lembur,'hari')
    def hitung_lembur (self,hari):
        return 20000*hari
    def cetak_lembur(self):
        x=self.hitung_lembur(self.jml_lembur)
        print('pendapatan lembur anda = Rp',x)
        
#class anak anak
class pegawai_tetap(pegawai):
    Jumlah_tetap=0
    def __init__(self, NIK, nama, gaji, jml_lembur,masa_kerja):
        super().__init__(NIK, nama, gaji, jml_lembur)
        self.masa_kerja=masa_kerja
        pegawai_tetap.Jumlah_tetap+=1
        
    def tampilkan_pegawai_tetap(self):
        self.tampilkan_pegawai()
        print('masa kerja :',self.masa_kerja,'tahun')
        
    def tunjangan_pegawai(self,istri=None ,anak=None):
        if(anak!=None) and (istri!=None):
            total=anak+istri
            print("tunjangan anak dan istri Rp :",total)
        elif(istri!=None):
            total=istri
            print('tunjangan istri= Rp',total)
        else:
            total=0
            print('anda belum berkeluarga dan tidak mendapat tunjangan anak istri')
    
    def hitung_lembur(self, hari):
        if(hari>20):
            return 20*30000
        elif(hari>10):
            return hari*30000
        else:
            return hari*20000
    def tampilkan_jumlah(self):
        print('jumlah pegawai tetep =',pegawai_tetap.Jumlah_tetap)
        
#anak kedua
class pegawai_kontrak(pegawai):
    jumlah_kontrak=0
    def __init__(self, NIK, nama, gaji, jml_lembur,durasi_kontrak):
        super().__init__(NIK, nama, gaji, jml_lembur)
        self.durasi_kontrak=durasi_kontrak
        pegawai_kontrak.jumlah_kontrak+=1
    def tampilkan_pegawai_kontrak(self):
        self.tampilkan_pegawai()
        print('surasi kontrak :',self.durasi_kontrak,'tahun')
    def tunjangan_pegawai(self):
        total=0
        print('pegawai kontrak tidak mendapat tunjangan')
    def hitung_lembur(self, hari):
        if(hari>=10):
            return 10*20000
        elif(hari<=0):
            return 0
        else:
            return hari*15000
    def tampilkan_jumlah(self):
        print('jumlah pegawai kontrak =',pegawai_kontrak.jumlah_kontrak,'orang')
        