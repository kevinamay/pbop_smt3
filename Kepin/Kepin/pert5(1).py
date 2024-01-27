from pert5 import UTY
from pert5 import Student
from pert5 import Dosen
from pert5 import Tendik

import os 

while(True):
    os.system("cls")
    print('menu pilihan')
    print('1. input data mahasiswa')
    print('2. input data dosen')
    print('3. input data tendik')
    print('4. cetak data mahasiswa')
    print('5. cetak data dosen')
    print('6. cetak data tendik')
    print('0. selesai')
    pilih=int(input('pilih menu:'))
    if(pilih==1):
        print('isi data mahasiswa')
        a=str(input("masukan NPM :"))
        b=str(input('masukkan Nama :'))
        c=str(input('masukan alamat :'))
        d=str(input('Program studi :'))
        e=str(input('angkatan:'))
        f=float(input('masukkan IP :'))
        mhs1=Student(a,b,c,d,e,f)
        
        #panggil Getter
        mhs1.angkatan=e
    if(pilih==2):
        print('isi data Dosen')
        a1=str(input("masukan id :"))
        b1=str(input('masukkan Nama :'))
        c1=str(input('masukan alamat :'))
        d1=str(input('homebase :'))
        e1=str(input('keahlian:'))
        f1=float(input('gaji :'))
        dsn1=Dosen(a1,b1,c1,d1,e1,f1)
    if (pilih==3):
        print('isi data Tendik')
        a2=str(input("masukan id :"))
        b2=str(input('masukkan Nama :'))
        c2=str(input('masukan alamat :'))
        d2=str(input('unit kerja :'))
        f2=float(input('gaji :'))
        tnk1=Tendik(a2,b2,c2,d2,f2)
    elif (pilih==4):
        print('isi data mahasiswa')
        mhs1.perkenalan_student()
        mhs1.perkenalan_privat_student()
    elif(pilih==5):
        print('cetak data dosen')
    elif (pilih==6):
        print('cetak data Tendik')
    elif (pilih==0):
        print('terimakasih')
        break
    else:
        print('anda salah pilih menu')
        print('tekan enter untuk melanjutkan')
    os.system("pause")   