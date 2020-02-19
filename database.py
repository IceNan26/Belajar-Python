import csv

print('\t\t Selamat Datang di halaman Pendaftaran\n')

def menulis_data():
    nama = input('Nama Lengkap\t: ')
    email = input('Alamat email\t: ')
    username = input('Create Your Username\t: ')
    Password = input('Password\t\t: ')
    with open('data.csv','a') as tulis:
        database_pengguna = ['Nama','email','Username','Password']

        menulis = csv.DictWriter(tulis,fieldnames=database_pengguna)

        menulis.writeheader()
        menulis.writerow({
            'Nama'     : nama,
            'email'    : email,
            'Username' : username,
            'Password' : Password,
            })

def membaca_data():
    with open("data.csv","r") as baca :
        data = []
        membaca = csv.reader(baca)
        for i in baca:
            data.append(i)
        Username = input("Masukkan Username anda: ")
        password = input("Masukkan Password anda: ")
        if Username in data:
            print("Selamat anda berhasil login")
        else:
            print("Username atau password yang anda masukkan salah ")


print("1. Login \n2.Daftar")
pilihan = input("pilih menu : ")
if int(pilihan) == 1 :
    membaca_data()
elif int(pilihan) == 2:
    menulis_data()
else:
    print("pilihan yang anda tidak valid silahkan cek kembali")
