import pygame

class Alien :
    def __init__(self, positionX, positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.color = (255, 0, 230)
    def Draw(self, screen, distX, distY):
        pygame.draw.rect(screen, self.color, (50 + distX, 50 + distY, 20, 20))
        self.positionX += 0.5