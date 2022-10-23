import pygame

class Rocket:
    def __init__(self, x, side):
        self.x = x
        self.y = 550
        self.side = side
    def Draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),(self.x, (self.y), 20, 20))
    def MoveUp(self):
        self.y -= 5

# class Rocket:
#     def __init__(self, x, side):
#         self.x = x
#         self.y = 550
#         self.side = side
#     def Draw(self, screen):
#         pygame.draw.rect(screen, (255, 255, 255),(self.x, (self.y), 20, 20))
#     def MoveUp(self):
#         self.y -= 5