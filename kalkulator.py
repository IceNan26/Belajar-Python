from os import system
def menu():
    print("1.Jumlah\n2.Kurang\n3.Kali\n4.Bagi\n")
    pilihan = int(input("Masukkan Pilihan anda (1-4)\t: "))
    if(pilihan == 1):
        tambah()
    elif(pilihan == 2):
        kurang()
    elif(pilihan == 3):
        kali()
    elif(pilihan == 4):
        bagi()
    else:
        print("Menu yang anda pilih tidak tersedia silahkan input ulang")
        system('cls')

def tambah():
    angka1 = int(input("Masukkan Angka 1\t: "))
    angka2 = int(input("Masukkan Angka 2\t: "))
    hasil = angka1 + angka2
    print("Hasilnya = " + str(hasil))



menu()
