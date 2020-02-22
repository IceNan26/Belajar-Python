import turtle

garis = turtle.Turtle()


for i in range(10):
    garis.forward(100)
    garis.left(135)
garis.forward(100)
for i in range(4):
    garis.left(90)
    garis.forward(100)


garis.penup()
garis.forward(200)
garis.pendown()
garis.color("blue")


for i in range(36):
    for j in range(4):
            garis.forward(50)
            garis.left(90)
    garis.left(11)
turtle.done()
