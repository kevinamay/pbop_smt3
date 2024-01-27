from coba import Pasien
import os

psn1 = None  # Inisialisasi objek Pasien di luar loop

while True:
    os.system("cls")
    print("1. Input data")
    print("2. Menampilkan method public")
    print("3. Method untuk edit data protected")
    print("4. Menampilkan atribut atribut yang bersifat protected")
    print("5. Menampilkan atribut atribut yang bersifat privat")
    print("0. Keluar")
    
    pilih = int(input('Pilih menu: '))

    if pilih == 1:
        a = str(input("NAMA PASIEN  = "))
        b = str(input("UMUR PASIEN  = "))
        c = str(input("ALAMAT PASIEN  = "))
        d = str(input("METODE PEMBAYARAN  = "))
        e = str(input("POLI YANG DITUJU = "))
        f = str(input("FASKES RUJUKAN = "))
        psn1 = Pasien(a, b, c, d, e, f)

    elif pilih == 2:
        if psn1 is not None:
            psn1.tampilkan_data_public()
        else:
            print("Data Pasien belum diinput.")
    
    elif pilih == 3:
        if psn1 is not None:
            e = str(input("POLI YANG DITUJU = "))
            f = str(input("FASKES RUJUKAN = "))
            psn1.edit_data_protected(e, f)
            print("Edit berhasil.")
        else:
            print("Data Pasien belum diinput.")
    
    elif pilih == 4:
        if psn1 is not None:
            psn1.tampilkan_atribut_protected()
        else:
            print("Data Pasien belum diinput.")
    
    elif pilih == 5:
        if psn1 is not None:
            psn1.tampilkan_atribut_private()
        else:
            print("Data Pasien belum diinput.")
    
    elif pilih == 0:
        print('Terimakasih')
        break
    
    os.system("pause")