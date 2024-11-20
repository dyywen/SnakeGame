from apple import Apple
from snake import Snake
import pygame

class Engine:

    def __init__(self, score = 0):
        self._score = score

    def resetApple(self, apple, snake):
        if self.collision(apple, snake) == True:
            apple.setApplePos(snake)
            self._score += 1
            if self._score % 2 == 0:
                snake.setSpeed(snake.getSpeed() + 2)
                print(snake.getSpeed())

    
    def collision(self, apple, snake):
        if pygame.Rect.colliderect(pygame.Rect(apple._position[0], apple._position[1], 15, 15), pygame.Rect(snake._position[0], snake._position[1], 15, 15)) == True:
            return True
    
    def getScore(self):
        return self._score
    
    def setScore(self, score):
        self._score = score + 1
        return score
            
    def borderCollision(self, snake, screen_width, screen_height):
        if snake.getSnakeBody()[0][0] > 1280 or snake.getSnakeBody()[0][1] > 720 or snake.getSnakeBody()[0][0] < 0 or snake.getSnakeBody()[0][1] < 0 :
            return True
        
    def start_menu(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Segoe UI', 40)
        title = font.render('Snake Game', True, (255, 255, 255))
        play_button = font.render('Play: SPACE', True, (255, 255, 255))
        screen.blit(title, (500, 340))
        screen.blit(play_button, (510, 400))
        pygame.display.update()

    def game_over_screen(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Segoe UI', 40)
        title = font.render('GAME OVER', True, ((255, 0, 0)))
        restart_button = font.render('Restart: S', True, ((255, 255, 255)))
        quit_button = font.render('Quit: Q', True, ((255, 255, 255)))
        score_text = font.render(f'Score: {self._score}', True, ((255, 255, 255)))
        screen.blit(title, (500, 240))
        screen.blit(score_text, (530, 310))
        screen.blit(restart_button, (370, 400))
        screen.blit(quit_button, (680, 400))
        pygame.display.update()
    def restart(self, snake):
        snake.resetSnakeBody()
        self._score = 0
   
            
