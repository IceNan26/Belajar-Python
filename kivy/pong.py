from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class pemain(Widget):
    score = NumericProperty(0)

    def mantul(self,bola):
        if self.collide_widget(bola):
            vx,vy = bola.kecepatan
            keluar =(bola.center_y - self.center_y) / (self.height / 2)
            memantul = Vector(-1*vx,vy)
            cepat = memantul * 1.1
            bola.kecepatan = cepat.x,cepat.y + keluar
class bola(Widget):
        kecepatan_x = NumericProperty(0)
        kecepatan_y = NumericProperty(0)

        kecepatan = ReferenceListProperty(kecepatan_x,kecepatan_y)

        def gerak(self):
            self.pos = Vector(*self.kecepatan) + self.pos

class game(Widget):
    bola = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def mulai(self):
        self.bola.center = self.center
        self.bola.kecepatan = Vector(4,0).rotate(randint(0,360))

    def update(self,dt):
        self.bola.gerak()
        self.player1.mantul(self.bola)
        self.player2.mantul(self.bola)

        if (self.bola.y < 0) or (self.bola.top > self.height):
            self.bola.kecepatan_y *= -1
        if self.bola.x < self.x :
            self.player2.score += 1
            self.mulai(cepat=(4,0))
        if self.bola.x > self.width :
            self.player1.score += 1

    def gerak_pemain(self,touch):
        if touch.x < self.width / 3:
            self.player1.center_y =  touch.y
        if touch.x > self.width / 3:
            self.player2.center_y = touch.y

class pong(App):
    def build(self):
        pong = game()
        pong.mulai()
        Clock.schedule_interval(pong.update,1.0/60.0)
        return pong

if __name__ == '__main__':
    pong().run()
