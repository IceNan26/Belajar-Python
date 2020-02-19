from tkinter import *

root = Tk()
root.title("Kalkulator")
input1 = Entry(root,fg="white",width=30,bg="green",borderwidth=10)
def click():
    berubah = Label(root,text= "Hasilnya adalah  " + hasil)
    berubah.pack()



tombol = Button(root,text="Ini tombol Bos Pencet Dong kalau sudah input :p",padx=50,pady=15,command=click,bg="magenta")
tombol.pack()
root.mainloop()
