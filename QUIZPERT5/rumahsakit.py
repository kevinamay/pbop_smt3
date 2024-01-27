from pasien import Pasien
import os

while (True):
    os.system("cls")
    print("1.input data")
    print("2.menampilkan method public")
    print("3.method untuk edit data protected")
    print("4.menampilkan atribut atribut yang bersifat protected")
    print("5.menampilkan atribut atribut yang bersifat privat")
    print("0.Keluar")
    pilih=int(input('pilih menu:'))
    
    if(pilih==1):
        a=str(input("NAMA PASIEN  ="))
        b=str(input("UMUR PASIEN  ="))
        c=str(input("ALAMAT PASIEN  ="))
        d=str(input("METODE PEMBAYARAN  ="))
        e=str(input("POLI YANG DITUJU ="))
        f=str(input("FASKES RUJUKAN ="))
        psn1=Pasien(a,b,c,d,e,f)
        
    elif(pilih==2):
        a=str(input("NAMA PASIEN  ="))
        b=str(input("UMUR PASIEN  ="))
        psn=Pasien(a,b)
    elif(pilih==3):
        print()
        e=str(input("POLI YANG DITUJU ="))
        f=str(input("FASKES RUJUKAN =")) 
       ppp=Pasien(e,f)
       print("edit berhasil")
    elif(pilih==4):
        pesanan.done()
    elif(pilih==5):
        
    elif(pilih==6):
        transaksi.berhasil()
    else:
        print('terimakasih')
        break
    os.system("pause")          
    