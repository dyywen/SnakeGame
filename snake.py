from collections import deque 
import pygame

class Snake:
    def __init__(self,  taille, speed: int, position = [100,50] ):
        self._body = deque([[100,50], [90,50], [80,50]])   
        self._position = position
        self._taille = taille 
        self._speed = speed

    def getTaille(self):
        return self._taille
    
    def setSnakeTaille(self, taille: int):
        self._taille= taille

    def getPosition(self):
        return self._position
    
    def setPosition(self, position):
        self._position = position
    
    def getSnakeBody(self):
        return self._body
    
    def resetSnakeBody(self):
        self._body = deque([[100,50], [90,50], [80,50]])
        self._position = [100,50]
        self._speed = 15
        
    
    def displaySnake(self, screen):
        for pos in self._body:
            pygame.draw.rect(screen, (0,128,0),
                         pygame.Rect(pos[0], pos[1], 15, 15))
    
    def growthAndMouvement(self, engine, apple, snake):
        self._body.appendleft(self._position.copy())
        if engine.collision(apple, snake) != True :
            self._body.pop()
    
    def setSpeed(self, speed):
        self._speed = speed

    def getSpeed(self):
        return self._speed
    
    def self_collision(self):
        for pos in range(1, len(self._body)):
            if self._body[0] == self._body[pos]:
                return True
    
    def input(self, events): #Méthode qui va gérer les mouvements du snake
        direction = 'RIGHT'
        move_to = direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_to ="UP"           
                
                if event.key == pygame.K_DOWN:
                    move_to ="DOWN"
                   
                if event.key == pygame.K_LEFT:
                    move_to = "LEFT"
                    
                if event.key == pygame.K_RIGHT:
                    move_to = "RIGHT"
        
        if move_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if move_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if move_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if move_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            self._position[1] -= 10 
        if direction == 'DOWN':
            self._position[1] += 10 
        if direction == 'LEFT':
            self._position[0] -= 10 
        if direction == 'RIGHT':
            self._position[0] += 10 
        
        self._body.appendleft(self._position.copy())
        self._body.pop()


    