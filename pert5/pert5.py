class UTY:
    def __init__(self,nama,alamat,id):
        self.nama = nama
        self.alamat = alamat
        self.id = id
        
    def perkenalan(self):
        print("perkenalkan nama saya",self.nama,"alamat saya di",self.alamat)
        
class Student(UTY):
    def __init__(self, nama, alamat,id,ip,angkatan,prodi):
        super().__init__(nama, alamat, id)
        self.__ip = ip
        self._angkatan = angkatan
        self.prodi = prodi
        
    @property
    def angkatan(self):
        return self._angkatan
    @angkatan.setter
    def angkatan(self,y):
        if(y<2017):
            y=2017
        elif (y>2023):
            y=2023
        else:
            y=y
            self._angkatan = y
            
#method student
    def perkenalan_student(self):
        self.perkenalan()
        print('saya berasal dari prodi',self.prodi,'angkatan',self._angkatan)
        
    def perkenalan_privat_student(self):
        self.perkenalan
        print('IP saya saat ini',self.__ip)
        
class Dosen (UTY):#bikin stter gether & method
    def __init__(self, nama, alamat, id,homebase,keahlian,gaji):
        super().__init__(nama, alamat, id)
        self._homebase = homebase
        self.keahlian = keahlian
        self.__gaji = gaji
    @property
    def gaji(self):
        return self.__gaji
    @gaji.setter
    def gaji(self,x):
        if(x<4000000):
            x=4000000
        elif(x<6000000):
            x=6000000
        else:
            x=x
            self.__gaji = x
    def perkenalan_dosen(self):
        self.perkenalan()
        print('keahlian saya',self.keahlian,'homebase besesar',self._homebase)
        
    def perkenalan_privat_dosen(self):
        self.perkenalan
        print('gaji saya sebesar',self.__gaji)
        
class Tendik(UTY):#bikin stter gether & method
    def __init__(self, nama, alamat, id,unitkerja,gaji):
        super().__init__(nama, alamat, id)
        self.unitkerja =unitkerja 
        self.__gaji=gaji
    @property
    def gaji(self):
        return self.__gaji
    @gaji.setter
    def gaji(self,x):
        if(z<5000000):
            z=5000000
        elif(z<10000000):
            z=10000000
        else:
            z=z

    def perkenalan_Tendik(self):
        self.perkenalan()
        print('unit kerja saya',self.unitkerja)
        
    def perkenalan_privat_dosen(self):
        self.perkenalan
        print('gaji saya sebesar',self.__gaji)
        