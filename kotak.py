import turtle
garis = turtle.Turtle()

def kotak(sudut,maju):
    for i in range(4):
        garis.forward(maju)
        garis.right(90)

def lingkaran():
    for i in range(360):
        kotak(11,100)


lingkaran()
