#Pendeklarasian Array

buah = []

#Pendeklarasian Class

class prosesData():


    #Pendeklarasian Method

    def tampilData(self):
        if len(buah) <=0:
                print("DATA KOSONG !!!")
                print("\n")


        else:
           for i in range(len(buah)):
                print("[%d] %s" % (i, buah[i]))
                print("\n")



    def tambahData(self):
        buahBaru = input("Nama Buah : ")
        buah.append(buahBaru)
        print("\n")


    def ubahData(self):

        prosesData.tampilData(self)
       

        i = int(input("Masukkan ID buah : "))
        if(i > len(buah)):
            print("ID tidak ada !!!")
            print("\n")
        else:
            buahBaru = input("Buah Baru : ")
            buah[i] = buahBaru
            print("\n")

    def hapusData(self):

        prosesData.tampilData(self)

        i = int(input("Masukkan ID Buah : "))
        if(i > len(buah)):
            print("ID tidak ada !!!")
            print("\n")
        else:
            buah.remove(buah[i])
            print("\n")
