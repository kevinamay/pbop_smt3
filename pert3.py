#mendeklarasikan class
class mobil:
    def __init__(self,merk,warna,tahun):
        self.warna=warna
        self.merk= merk
        self.tahun= tahun
    def ngebut(self):
        print('mobil merek',self.merk,'warna',self.warna,'tahun',self.tahun)
        print('mobil saya bisa ngebut')
        

