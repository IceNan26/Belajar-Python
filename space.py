import pygame as game
import random


game.init()

#layar
screen = game.display.set_mode((800,600))

# judul dan icon
game.display.set_caption("Spaceship war by @maliefrr ")
icon = game.image.load('spaceship.png')
game.display.set_icon(icon)

#player
pesawat = game.image.load('spaceship.png')
playerx = 390
playery = 470
perubahan = 0
def player():
    screen.blit(pesawat,(playerx,playery))

# peluru
peluru = game.image.load('bullet.png')
pelurux = 0
peluruy = 470
gerak_pelurux = 0
gerak_peluruy = 5
peluru_state = "ready"
def tembak(x,y):
    global peluru_state
    peluru_state = "fire"
    screen.blit(peluru,(x + 13 , y + 9))

#enemy
ufo = game.image.load("ufo.png")
ufox = random.randint(4,735)
ufoy = random.randint(40,165)
gerakx = 3
geraky = 20
def musuh():
    screen.blit(ufo,(ufox,ufoy))

# background game
background = game.image.load("bg.jpg")

# game loop
running = True
while running:
    screen.fill((25,100,255))
    screen.blit(background,(0,0))
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        if event.type == game.KEYDOWN:
            if event.key == game.K_LEFT:
                perubahan = -6
            if event.key == game.K_RIGHT:
                perubahan = 6
            if event.key == game.K_SPACE:
                tembak(playerx,peluruy)
        if event.type == game.KEYUP:
            if event.key == game.K_LEFT or event.key == game.K_RIGHT:
                perubahan = 0

    playerx += perubahan
    if playerx <= 4 :
        playerx = 4
    elif playerx >= 735:
        playerx = 735
    # gerak musuh
    ufox += gerakx
    if ufox <= 4:
        gerakx *= -1
        ufoy += geraky
    if ufox >= 735:
        gerakx *= -1
        ufoy += geraky
    # gerak peluru
    if peluru_state is "fire":
        tembak(playerx,peluruy)
        peluruy -= gerak_peluruy
    player()
    musuh()
    game.display.update()
