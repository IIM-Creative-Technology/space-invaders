import pygame, sys, random
from pygame.locals import *
from player import Player
from aliens import Aliens

pygame.init()

playerCoordX = 0 
windowWidth = 800
windowHeight = 600
allRockets = []

shipX = windowWidth / 2
shipY = windowHeight - 50
clock = pygame.time.Clock()
GREEN = (0, 255, 8)
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Space Invaders')

background = pygame.Surface(screen.get_size())
background = background.convert()
screen.blit(background, (0, 0))

player = Player(shipX)
aliens = Aliens(100,100)
loop = True
status = True
s = -30

while loop:
    screen.fill((0, 0, 0)) 
    player.Draw(screen)
    toDestroy = aliens.checkCollision(allRockets)
    for rocket in reversed(toDestroy):
        allRockets.pop(rocket)
    for rocket in allRockets:
        if rocket.side == 1:
            rocket.MoveUp()
        else:
            rocket.MoveDown()  
        rocket.Draw(screen)
    aliens.Draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rocket =  player.Shoot()
                allRockets.append(rocket)
        if event.type == QUIT:
            loop = False
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        player.Move("right") 
    if keys_pressed[pygame.K_LEFT]:
        player.Move("left") 
    aliens.MoveSide()
    n = random.randint(1,200)
    if n == 4:
        print("hello")          
    pygame.display.flip()  
    
    clock.tick(120)

    if player.positionY ==  aliens.bottomBloc:
        pygame.quit()       
    pygame.display.flip()  

