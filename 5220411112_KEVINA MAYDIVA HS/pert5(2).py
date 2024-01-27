from pert5 import UTY
from pert5 import Student
from pert5 import Dosen
from pert5 import Tendik

import os

while (True):
    os.system("cls")
    print('menu pilihan')
    print('1. input data mahasiswa')
    print('2. input data dosen')
    print('3. input data tendik')
    print('4. cetak data mahasiswa')
    print('5. cetak data dosen')
    print('6. cetak data tendik')
    print('7. edit gaji dosen')
    print('8. edit gaji tendik')
    print('0. selesai')
    pilih = int(input('pilih menu:'))
    if (pilih == 1):
        print('isi data mahasiswa')
        a = str(input("masukan NPM :"))
        b = str(input('masukkan Nama :'))
        c = str(input('masukan alamat :'))
        d = str(input('Program studi :'))
        e = int(input('angkatan:'))
        f = float(input('masukkan IP :'))
        mhs1 = Student(id=a, nama=b, alamat=c, prodi=d, angkatan=e, ip=f)
        # panggil Getter
        mhs1.angkatan = e
    elif (pilih == 2):
        print('isi data Dosen')
        c = input("Masukan nik :")
        a = input("Masukan nama :")
        b = input("Masukan alamat :")
        d = input("Masukan homebase :")
        e = input("Masukan keahlian :")
        f = int(input("Masukan gaji :"))
        dsn1 = Dosen(nama=a, alamat=b, id=c, homebase=d, keahlian=e, gaji=f)
    elif (pilih == 3):
        print('isi data Tendik')
        c = input("Masukan nik :")
        a = input("Masukan nama :")
        b = input("Masukan alamat :")
        d = input("Masukan Unit Kerja :")
        f = int(input("Masukan gaji :"))
        tnd1 = Tendik(nama=a, alamat=b, id=c, unitkerja=d, gaji=f)
    elif (pilih == 4):
        print('isi data mahasiswa')
        mhs1.perkenalan_student()
        mhs1.perkenalan_privat_student()
    elif (pilih == 5):
        print('cetak data dosen')
        dsn1.perkenalan_dosen()
        dsn1.perkenalan_privat_dosen()
    elif (pilih == 6):
        print('cetak data Tendik')
        tnd1.perkenalan_Tendik()
        tnd1.perkenalan_privat_tendik()
    elif (pilih == 7):
        print('ubah gaji Dosen')
        a = int(input("Masukan gaji :"))
        dsn1.gaji = a
    elif (pilih == 8):
        print('ubah gaji Tendik')
        a = int(input("Masukan gaji :"))
        tnd1.gaji = a

    elif (pilih == 0):
        print('terimakasih')
        break
    else:
        print('anda salah pilih menu')
        print('tekan enter untuk melanjutkan')
    os.system("pause")
