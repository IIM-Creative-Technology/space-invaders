from turtle import position
import pygame

from rocket import Rocket 

class Player:
    def __init__(self, positionX):
       self.positionX = positionX
       self.positionY = 550
       self.vitesse = 5
       self.color = (0, 255, 8)
       self.colorShot = (255, 255, 255)
    def Move(self, direction):
        match direction :
            case "left" :
                if  self.positionX <= 5:
                    self.positionX = 0
                else:  
                    self.positionX -= self.vitesse 
            case "right" :
                if self.positionX >= 775:
                    self.positionX = 780
                else:  
                    self.positionX += self.vitesse  
    def Shoot(self):
        return Rocket(self.positionX, 1)
        
    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.positionX, self.positionY, 20, 20)) 
    
