from pesanan import pesanan
from barang import barang
from transaksi import transaksi
import os

while(True):
    os.system("cls")
    print('pilihan menu:')
    print('1. isi data pelanggan :')
    print('2. isi data pembelian :')
    print('3. isi data barang :')
    print('4. cetak data pelanggan :')
    print('5. cetak pembelian/barang :')
    print('6. cetak transaksi :')
    print('0. keluar menu :')
    pilih=int(input('pilih menu:'))
    
    if(pilih==1):
        a=str(input('NAMA PEMBELI :'))
        b=str(input('DAFTAR BARANG:'))
        c=str(input('TANGGAL PESANAN:'))
        d=str(input('STATUS:'))
        a1=str(input('NAMA BARANG'))
        b1=str(input('STOK BARANG:'))
        c1=str(input('DESKRIPSI BARANG:'))
        a2=str(input('NAMA TOKO :'))
        b2=str(input('TOTAL PEMBAYARAN:'))
        pmb1=pesanan(a,b,c,d,barang(a1,b1,c1,transaksi(a2,b2)))
        
    elif(pilih==2):
        a1=str(input('NAMA BARANG'))
        b1=str(input('STOK BARANG:'))
        c1=str(input('DESKRIPSI BARANG:'))
        psn=pesanan(a1,b1,c1)
    elif(pilih==3):
       a2=str(input('NAMA TOKO :'))
       b2=str(input('TOTAL PEMBAYARAN:')) 
       trs=transaksi(a2,b2)      
    elif(pilih==4):
        pesanan.done()
    elif(pilih==5):
        barang.ready()
    elif(pilih==6):
        transaksi.berhasil()
    else:
        print('terimakasih')
        break
    os.system("pause")
    