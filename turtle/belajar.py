import turtle
import random
import math

objek = turtle.Turtle()

def kotak(panjang):
    for i in range(4):
        objek.forward(panjang)
        objek.right(90)

def lingkaran():
    for i in range(36):
        kotak(30)
        objek.left(11)

def lingkaranKecil():
    for i in range(36):
        kotak(20)
        objek.left(11)


objek.color("#4271ff")
objek.begin_fill()
lingkaran()
objek.right(45)
objek.end_fill()
objek.penup()
objek.color("#499bff")
objek.begin_fill()
objek.forward(100)
objek.pendown()
lingkaran()
objek.left(90)
objek.end_fill()
objek.penup()
objek.color("#59e1ff")
objek.begin_fill()
objek.forward(100)
objek.pendown()
lingkaran()
objek.left(80)
objek.end_fill()
objek.penup()
objek.begin_fill()
objek.forward(100)
objek.left(90)
objek.forward(200)
objek.pendown()
objek.forward(100)
for i in range(100):
    objek.left(155)
    objek.forward(100)
objek.penup()
objek.right(180)
objek.forward(500)
objek.pendown()
for i in range(100):
    objek.left(155)
    objek.forward(100)
objek.penup()
objek.right(90)
objek.forward(300)
objek.pendown()
for i in range(100):
    objek.left(155)
    objek.forward(100)
objek.penup()
objek.right(180)
objek.forward(300)
for i in range(20):
    objek.forward(100)
    objek.right(145)
turtle.done()
