from pert3 import mobil
from mahasiswa import Mahasiswa
from kucing import kucing
import os

while(True):
    os.system("cls")
    print('pilihan menu:')
    print('1. isi data mahasiswa :')
    print('2. isi data mobil :')
    print('3. isi data kucing :')
    print('4. cetak mahasiswa :')
    print('5. cetak mobil :')
    print('6. cetak kucing :')
    print('0. keluar menu :')
    pilih=int(input('pilih menu:'))
    
    if(pilih==1):
        a=str(input('NIM :'))
        b=str(input('NAMA:'))
        c=str(input('PRODI:'))
        d=str(input('ALAMAT:'))
        a1=str(input('MERK MOBIL:'))
        b1=str(input('WARNA MOBIL:'))
        c1=str(input('TAHUN MOBIL:'))
        a2=str(input('NAMA KUCING :'))

        mhs1=Mahasiswa(a,b,c,d,
                    mobil(a1,b1,c1),
                    kucing(a2,''))
        
    elif(pilih==2):
        a1=str(input('MERK MOBIL:'))
        b1=str(input('WARNA MOBIL:'))
        c1=str(input('TAHUN MOBIL:'))
        mycar=mobil(a1,b1,c1)
    elif(pilih==3):
        a2=str(input('NAMA KUCING :'))
        mycat=kucing(a2,'')
    elif(pilih==4):
        mhs1.perkenalan()
    elif(pilih==5):
        mycar.ngebut()
    elif(pilih==6):
        mycat.mengeong()
    else:
        print('terimakasih')
        break
    os.system("pause")
