import turtle
import os

# layar

layar = turtle.Screen()
layar.title("Game Pong")
layar.bgcolor("green")
layar.setup(width=800,height=600)
layar.tracer(0)


#player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.penup()
player1.goto(-350,0)
player1.shapesize(stretch_wid=5,stretch_len=1)
#player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.penup()
player2.goto(350,0)
player2.shapesize(stretch_wid=5,stretch_len=1)
#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = 2
bola.dy = -2



#function
def player1_naik():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_turun():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_naik():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_turun():
    y = player2.ycor()
    y -= 20
    player2.sety(y)

#keyboard
layar.listen()
layar.onkeypress(player1_naik,"w")
layar.onkeypress(player1_turun,"s")
layar.onkeypress(player2_naik,"Up")
layar.onkeypress(player2_turun,"Down")

#Game loop
while True:
    layar.update()
    # pergerakan bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)


    #batas pergerakan bola
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1

    # bola menyentuh player
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < player2.ycor() + 40 and bola.ycor() > player2.ycor() -40):
        bola.setx(340)
        bola.dx *= -1


    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < player1.ycor() + 40 and bola.ycor() > player1.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
