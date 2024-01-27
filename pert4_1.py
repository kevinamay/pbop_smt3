class mahasiswa:
    def __init__(self):
        self.nama=None
        self.alamat=None
        self._umur=0
        
@property
def umur(self):
    print("method getter dipanggil untuk atribut umur")
    return self._umur

@umur.setter
def umur(self,a):
    if(a<18):
        print('maaf anda belum boleh menonton')
    else:
        print('monggo')
    print("method setter untuk atribut umur dipanggil ")
    self._umur=a
    
bejo=mahasiswa()
bejo.umur=20
bejo.nama="andi"
bejo.alamat="sleman"
print(bejo.nama)
print(bejo.alamat)
print(bejo.umur)
    