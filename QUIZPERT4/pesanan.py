class pesanan :
    def __init__(self,pembeli,daftar_barang,tanggal_pesanan,status):
        self.pembeli = pembeli
        self.daftar_barang = daftar_barang
        self.tanggal_pesanan = tanggal_pesanan
        self.status = status
        
    def ubah_status(self):
        print('nama pembeli :',self.pembeli)
        print('daftar barang :',self.daftar_barang)
        print('tangggal_pesanan :',self.tanggal_pesanan)
        print('status pesanan:', self.status)