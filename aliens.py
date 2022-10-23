import pygame
from rocket import Rocket 

class Aliens:
    def __init__(self, positionX, positionY):
        self.vitesse = 5
        self.color = (255, 0, 230)
        self.width = 30
        self.height = 30
        self.spacing = 45
        self.positionX = positionX
        self.positionY = positionY
        self.direction = "right"
        self.invaders = [[1 for x in range(10)] for x in range(4)]
        self.blocHeight = 180
        self.blocWidth = 450
        self.bottomBloc = self.positionY + self.blocHeight 
                     

    def Draw(self, screen):
        for y in range(len(self.invaders)):
            for x in range(len(self.invaders[y])):
                if (self.invaders[y][x] == 1):
                    pygame.draw.rect(screen, self.color, ((x * self.spacing) + self.positionX, (y * self.spacing) + self.positionY,self.width,self.height))
    def Shoot(self):
        return Rocket(self.positionX, 0)

    def checkCollision(self, allRockets):
        toDestroy = []
        for indexRocket in range(len(allRockets)):
            rocket = allRockets[indexRocket]
            if rocket.side == 1:
                if rocket.y <= self.positionY + self.blocHeight:
                    if rocket.x >= self.positionX and rocket.x<= self.positionX+self.blocWidth:
                        distanceBlocRocket = rocket.x - self.positionX
                        foundTarget = False
                        for rowIndex in reversed(range(len(self.invaders))):
                            if foundTarget == False:
                                if rocket.y <= (self.blocHeight + self.positionY) - ((3 - rowIndex) * (self.height + 15)):
                                    row  = self.invaders[rowIndex]
                                    for indexAlien in range(len(row)):
                                        if self.invaders[rowIndex][indexAlien] == 1:
                                            distanceBlocAlien =  (((indexAlien)*self.width) + ((indexAlien) * 15))
                                            if distanceBlocRocket >= distanceBlocAlien - 7.5 and distanceBlocRocket<= distanceBlocAlien+self.width + 7.5:
                                                self.invaders[rowIndex][indexAlien] = 0
                                                toDestroy.append(indexRocket)
                                                foundTarget = True
                                    
        return toDestroy


    def MoveSide(self):
        match self.direction :
            case "right" :
                if self.positionX + 1 >= 350:
                    self.MoveDown()
                    return
                self.positionX += 1
            case "left":
                if self.positionX - 1 <= 0:
                    self.MoveDown()
                    return
                self.positionX -= 1


    def MoveDown(self):
        match self.direction:
            case 'left':
                self.direction = "right"
            case 'right':
                self.direction = "left"
        self.positionY += self.height
        if self.positionY > 340:
            pygame.quit()

