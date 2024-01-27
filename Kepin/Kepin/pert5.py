class UTY:
    def __init__(self,nama,alamat,id):
        self.nama = nama
        self.alamat = alamat
        self.id = id
        
    def perkenalan(self):
        print(f'perkenalkan nama saya {self.nama} alamat saya di {self.alamat}')
        
class Student(UTY):
    def __init__(self, nama, alamat,id,ip,angkatan,prodi):
        super().__init__(nama, alamat, id)
        self.__ip = ip
        self._angkatan = angkatan
        self.prodi = prodi
        
    @property
    def angkatan(self):
        pass
    @angkatan.getter
    def angkatan(self):
        return self._angkatan
    @angkatan.setter
    def angkatan(self,y):
        self._angkatan = y
            
#method student
    def perkenalan_student(self):
        self.perkenalan()
        print(f'saya berasal dari prodi {self.prodi} angkatan {self._angkatan}')
        
    def perkenalan_privat_student(self):
        self.perkenalan
        print(f'IP saya saat ini {self.__ip}')
        
class Dosen (UTY):#bikin stter gether & method
    def __init__(self, nama, alamat, id,homebase,keahlian,gaji):
        super().__init__(nama, alamat, id)
        self.homebase = homebase
        self.keahlian = keahlian
        self.gaji = gaji

    @property
    def detail():
        pass
    @detail.setter
    def detail(self,nama,alamat):
        self.nama = nama
        self.alamat = alamat
    @detail.getter
    def detail(self):
        return [self.nama,self.alamat]

        
class Tendik(UTY):#bikin stter gether & method
    def __init__(self, nama, alamat, id,unitkerja,gaji):
        super().__init__(nama, alamat, id)
        self.unitkerja =unitkerja 
        self.gaji=gaji

    @property
    def detail():
        pass
    @detail.setter
    def detail(self,nama,alamat):
        self.nama = nama
        self.alamat = alamat
    @detail.getter
    def detail(self):
        return [self.nama,self.alamat]
        