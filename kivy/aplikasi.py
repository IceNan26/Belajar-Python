import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class layout(GridLayout):
    def __init__(self,**kwargs):
        super(layout,self).__init__(**kwargs)
        self.cols = 1


        self.tampilan_Dalam = layout()
        self.tampilan_Dalam.cols = 2
        self.tampilan_Dalam.add_widget(Label(text="Nama: "))
        self.nama = TextInput(multiline = False)
        self.tampilan_Dalam.add_widget(self.nama)

        self.tampilan_Dalam.add_widget(Label(text="Alamat: "))
        self.alamat = TextInput(multiline = False)
        self.tampilan_Dalam.add_widget(self.alamat)

        self.tampilan_Dalam.add_widget(Label(text = "email: "))
        self.email = TextInput(multiline = False)
        self.tampilan_Dalam.add_widget(self.email)

        self.tampilan_Dalam.add_widget(Label(text = "Alasan mengikuti kegiatan: "))
        self.alasan = TextInput(multiline = True)
        self.tampilan_Dalam.add_widget(self.alasan)

        self.add_widget(self.tampilan_Dalam)

        self.tombol = Button(text = "Submit")
        self.add_widget(self.tombol)


class aplikasi(App):
    def build(self):
        return layout()

if __name__ == "__main__":
    aplikasi().run()
