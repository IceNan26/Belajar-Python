uang = input("Masukkan JUmlah uang\t: ")
pengeluaran = input("Masukkan Pengeluaran perhari\t: ")
minggu = int(pengeluaran) * 6
tabungan = input("Masukkan Jumlah uang yang mau di kumpulkan\t:")
hari = int(tabungan) / ((int(uang) - int(minggu)))
print("Jadi Kurang lebih anda bisa mengumpulkan uang sebesar "  + str(tabungan) + " dalam " + str(hari) + " minggu")
pilihan = input("Apakah anda mau dalam hitungan bulan ? (y/n)")
