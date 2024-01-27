class barang :
    def __init__(self, nama , harga , stok, deskripsi):
       self.nama = nama 
       self.harga = harga
       self.stok = stok
       self.deskripsi = deskripsi
    
    def tambah_stok(self, jumlah):
        self.stok += jumlah

    def kurangi_stok(self, jumlah):
        self.stok -= jumlah
        
    def arsip(self):
        print('nama barang:',self.nama)
        print('harga barang:',self.harga)
        print('stok barang :',self.stok)
        print('deskripsi barang :',self.deskripsi)
        
      