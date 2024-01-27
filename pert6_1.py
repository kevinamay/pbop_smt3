#menu untuk mengelola overloding dan overriding
from pert6 import pegawai,pegawai_tetap,pegawai_kontrak
import os

list_pegawai_tetap=[]
list_pegawai_kontrak=[]
print('input data pegawai berhenti isi XX')
n=0
while(True):
    os.system("cls")
    print('menu pilihan')
    print('1. input pegawai teteap')
    print('2. input pegawai kontrak')
    print('3. cetak pegawai tetap ' )
    print('4. cetak pegawai kontrak')
    print('0. selesai')
    pilih=int(input('pilih menu :'))
    if(pilih==1):
        print('input data pegawai berhenti isi XX')
        a=str(input('masukkan NIK pegawai :'))
        if(a!='XX'):
            b=str(input('masukkan nama pegawai :'))
            c=str(input('masukkan gaji Rp  :'))
            d=int(input('masukkan lama kerja(thn)  :'))
            e=int(input('maukkan jumlah lembur(hari)  :'))
            #onjek di buat
            peg=pegawai_tetap(a,b,c,d,e)
            list_pegawai_tetap.insert(n,peg)
            ya1=str(input('apakah anda sudah berkeluarga <y/t>?'))
            if(ya1=='y'):
                ya2=str(input('apakah anda punya anak <y/t>?'))
                if(ya2=='y'):
                    tunj_istri=250000
                    tunj_anak=200000
                else:
                    tunj_istri=250000
                    tunj_anak=None
            else:
                tunj_istri=None
                tunj_anak=None
            n+=1
        else:
            print('input data pegawai tetap selesai')
    elif(pilih==2):
        print('input data pegawai berhenti isi XX')
        a=str(input('masukkan NIK pegawai:'))
        if(a!='XX'):
            b=str(input('masukkan nama pegawai  :'))
            c=int(input('masukkan gaji Rp '))
            d=int(input('masukkan durasi kontrak(thn) :'))
            e=int(input('masukkan jumlah lembur(hari) :'))
            #objek dibuat
            peg=pegawai_kontrak(a,b,c,d,e)
            list_pegawai_kontrak.insert(n,peg)
            n+=1
        else:
            print('input pegawai kontrak selesai')
    elif(pilih==3):
        print('cetak pegawai tetap')
        y=len(list_pegawai_tetap)
        i=1
        for y in list_pegawai_tetap:
            print('pegawai ke',i)
            y.tampilkan_pegawai()
            y.tunjangan_pegawai(tunj_istri,tunj_anak)
            y.cetak_lembur()
            i+=1
            print('tekan enter --->')
            os.system("pause")
            print('jumlah pegawai tetap ',pegawai_tetap.Jumlah_tetap)
    elif(pilih==4):
        print('cetak pegawai kontrak')
        y=len(list_pegawai_kontrak)
        i=1
        for y in list_pegawai_kontrak:
            print('pegawai ke',i)
            y.tampilkan_pegawai_kontrak()
            y.tunjangan_pegawai()
            y.cetak_lembur()
            i+=1
            print('tekan enter --->')
            os.system("pause")
            print('jumlah pegawai kontrak ',pegawai_kontrak.jumlah_kontrak)
    elif(pilih==0):
        print('terimakasih')
        break
    else:
        print('salah pilih menu')
    print('tekan enter')
    os.system("pause")
                                  