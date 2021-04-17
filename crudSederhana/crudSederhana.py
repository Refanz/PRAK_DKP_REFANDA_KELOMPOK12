import fungsiMethod

#Membuat Objek

fi = fungsiMethod.prosesData()


#Pendeklarasian Fungsi

def namaKelompok():
    garis() 
    print("-         KELOMPOK 12           -")
    garis() 
    print("1. Anugrah")
    print("2. Fadel Rizky ")
    print("3. Refanda Surya")
    print("4. Ruben Rusel")
    garis()

def ulangi():

    pilihan = input("Apakah anda ingin melakukan proses kembali (Y/T) ? ")

    if(pilihan == 'Y' or pilihan =='y'):
        tampilMenu()

    else:
         print("\n")
         print("Terima Kasih")


def garis():
    print("---------------------------------")

def tampilMenu():
    print("\n")
    garis()
    print("-    PROGRAM CRUD SEDERHANA     -")
    garis()


    print("[1] TAMPIL DATA")
    print("[2] TAMBAH DATA")
    print("[3] UBAH DATA")
    print("[4] HAPUS DATA")
    garis()
    print("\n")

    menu = int(input("Pilih menu yang ingin anda lakukan (1 - 4) : "))
    print("\n")

    if(menu == 1):
        fi.tampilData()
        ulangi()
    elif menu == 2:
        fi.tambahData()
        ulangi()
    elif menu == 3:
        fi.ubahData()
        ulangi()
    elif menu == 4:
        fi.hapusData()
        ulangi()
    else:
        print("MENU YANG ANDA MASUKKAN SALAH !!!")
        print("\n")
        ulangi()


#Pemanggilan Fungsi Utama
namaKelompok()

tampilMenu()














