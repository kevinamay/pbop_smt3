#akses publik protected and privat
class mahasiswa:
    def __init__(self,nim,nama,prodi,ipk,uang_saku):
        self._nim=nim
        self.nama=nama
        self.prodi=prodi
        self.__ipk=ipk
        self._uang_saku=uang_saku
    def public_pekenalan(self):
        print("perkenalkan nama saya",self.nama,"saya kuliah di prodi",self.prodi)
        
    def _protected_nim_dan_uangsaku(self):
        print("ini ranah khusus keluarga saya dan teman dekat")
        print("nama saya",self.nama)
        print("nim saaya di prodi ",self.prodi,"adalah",self._nim)
        print("uang saku saya perbulan adalah Rp",self._uang_saku)
    
    def __privat_IPK(self):
        print("ini ranah privat saya")
        print("nama saya",self.nama,"IPK saya",self.__ipk)
        
    #mengakses method protected    
    def akses_method_protected(self):
        self._protected_nim_dan_uangsaku()
    #mengakses method privat
    def akses_method_privat(self):
        self.__privat_IPK()
        
#bikin object     
a=str(input("NIM  ="))
b=str(input("NAMA  ="))
c=str(input("PRODI  ="))
d=str(input("IPK  ="))
e=str(input("UANG SAKU PERBULAN = RP"))

#akses public
mhs1= mahasiswa(a,b,c,d,e)
print('Akses method public :')
mhs1.public_pekenalan()
print('Akses method protected :')
mhs1.akses_method_protected()
print('Akses method privat :')
mhs1.akses_method_privat()