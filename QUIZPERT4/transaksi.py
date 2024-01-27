class transaksi :
    def __init__(self,pembeli , toko , daftar_barang ,total_pembayaran):
       self.pembeli = pembeli
       self.toko = toko 
       self.daftr_barang = daftar_barang
       self.total_pembayaran = total_pembayaran
      
    def perkenalan(self):
        print('nama pembeli:',self.pembeli)
        print('nama toko:',self.toko)
        print('daftar barang yang diambil:',self.daftr_barang)
        print('total pembayaran :',self.total_pembayaran)
        