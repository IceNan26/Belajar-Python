import os
os.environ['KIVY_WINDOW'] = 'pygame'
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class login(GridLayout):
    def __init__(self,**kwargs):
        super(login,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = "Username"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password"))
        self.password = TextInput(multiline = False)
        self.add_widget(self.password)

class aplikasi(App):
    def build(self):
        return login()

if __name__ == "__main__":
    aplikasi().run()
