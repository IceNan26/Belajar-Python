import pygame

pygame.init()

layar = pygame.display.set_mode((1000,600))
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders by maliefrr")
pesawat = pygame.image.load("space-invaders.png")
running = True
posisix = 480
posisiy = 480
perubahan = 0
def player(x,y):
    layar.blit(pesawat,(posisix,posisiy))
while running:
    layar.fill((25,100,180))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                perubahan = -0.5
            if event.key == pygame.K_RIGHT:
                perubahan =  0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                perubahan = 0

    posisix += perubahan
    player(posisix,posisiy)
    pygame.display.update()
