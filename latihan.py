import turtle

kuro = turtle.Turtle()
kuro.speed(0)
kuro.color('yellow')
def kotak(x,y):
     kuro.forward(x)
     kuro.right(y)
     kuro.forward(x)
     kuro.right(y)
     kuro.forward(x)
     kuro.right(y)
     kuro.forward(x)

for i in range(360):
    kotak(100,90)
    kuro.left(1)
    if(i>=200):
        kuro.color('green')
    elif(i>=100):
        kuro.color('blue')
    elif(i>=50):
        kuro.color('pink')

# http://www.codeskulptor.org/#user47_kEUDao2LZQ_9.py
