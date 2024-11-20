import pygame
import random

class Apple(): 

    def __init__(self, color = "red", position = [300, 50], size = 5):
        self._position = position
        self._size = size
        self._color = color

    def displayApple(self, surface):
        pygame.draw.rect(surface , self._color, 
                         pygame.Rect(self._position[0], self._position[1], 15, 15))

    def getApplePos(self):
        return self._position
    
    def setApplePos(self, snake):
        run = True
        while run:
            x = 7
            y = 7
            while x % 10 != 0:
                x = random.randint(1, 640)
            while y % 10 !=0:
                y = random.randint(1,360)
            self._position = [x, y]
            if self._position in snake._body:
                run = True
            else:
                run = False
    
    # def getAppleColor(self):
    #     color = self._color
    #     return color
    
    # def getAppleSize(self):
    #     size = self._size
    #     return size