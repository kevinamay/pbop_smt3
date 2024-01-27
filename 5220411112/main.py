from pasien import Pasien


while True:
    print("1. Input pasien ")
    print("2. Tampilkan pasien ")
    print("0. exit")
    pilih = int(input("Pilih menu : "))
    if pilih == 1:
        while True:
            nama = input("Masukan Nama Pasien : ")
            umur = int(input("Masukan umur pasien : "))
            alamat = input("Masukan alamat Pasien : ")
            metode = input("Masukan metode pembayaran Pasien : ")
            poli = input("Masukan poli Pasien : ")
            faskes = input("Masukan faskes Pasien : ")
            # pasien = Pasien(nama,umur,alamat,metode,poli,faskes)
            pasien = Pasien("Veranda",30,"Jombor","Tunai","Bidan","Bekasi")
            print("1. Cetak detail pasien")
            pilih = int(input("Pilih menu : "))
            if pilih == 1:
                pasien.detail_pasien()
            else:
                break
    else:
        break
