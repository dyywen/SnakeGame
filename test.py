from collections import deque 
from queue import Queue
import pygame
from snake import Snake
from apple import Apple
from engine import Engine
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
game_state = 'start_menu'
font = pygame.font.SysFont("Segoe UI", 35)


snake= Snake(15, 15)
apple= Apple()
engine = Engine()


# setting default snake direction 
# towards right
direction = 'RIGHT'
move_to = direction

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == 'start_menu':
        engine.start_menu(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_state = 'game'

    elif game_state == 'game_over':
        engine.game_over_screen(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            game_state = 'start_menu'
            engine.restart(snake)
            direction = 'RIGHT'
            move_to = direction
            running = True
        if keys[pygame.K_q]:
            running = False

    elif game_state == 'game':
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_to ="UP"           
                
            if event.key == pygame.K_DOWN:
                move_to ="DOWN"
                
            if event.key == pygame.K_LEFT:
                move_to = "LEFT"
                
            if event.key == pygame.K_RIGHT:
                move_to = "RIGHT"

        if engine.borderCollision(snake, screen.get_width(), screen.get_height()):
            game_state = 'game_over'
        if snake.self_collision() == True :
            print("test")
            game_state = 'game_over'
               
    # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        score_text = font.render(f'Score: {engine.getScore()}', True, (255, 255, 255))
        screen.blit(score_text, (5, 5))


        if move_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if move_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if move_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if move_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        if direction == 'UP':
            snake._position[1] -= 10
        if direction == 'DOWN':
            snake._position[1] += 10
        if direction == 'LEFT':
            snake._position[0] -= 10
        if direction == 'RIGHT':
            snake._position[0] += 10
        
        snake.displaySnake(screen)
        snake.growthAndMouvement(engine, apple, snake)
        apple.displayApple(screen)
        engine.resetApple(apple, snake)
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        
        

    clock.tick(snake._speed)   

pygame.quit()
