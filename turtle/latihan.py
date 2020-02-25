import turtle

objek = turtle.Turtle()

objek.color("red","yellow")
objek.begin_fill()
for gambar in range(20):
    objek.forward(50)
    objek.right(150)
objek.end_fill()
objek.penup()
objek.color("yellow","green")
objek.forward(80)
objek.begin_fill()
objek.pendown()
for gambar in range(20):
    objek.forward(50)
    objek.right(150)
objek.end_fill()


turtle.done()
