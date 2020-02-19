file = open('belajar.txt','a+')


def nulis(Tulis):
    file.write(Tulis + " ")
    ulang()

def ulang():
    pilihan = input('Apakah kamu ingin nulis lagi ? (y/n): ')
    if(pilihan == "y"):
        nulis(input("Mau Nulis Apa ? "))
    elif(pilihan == "n"):
        print("Terimakasih telah menggunakan layanan kami")
    else:
        print("Pilihan Yang anda Masukkan salah silahkan input ulang")
        ulang()

nulis(input("Mau Nulis Apa ? "))
