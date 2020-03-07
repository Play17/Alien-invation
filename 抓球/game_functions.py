import pygame
import sys
from ball import Ball
from random import randint
from time import sleep

def check_events(receiver):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                receiver.moving_right = True
            elif event.key == pygame.K_LEFT:
                receiver.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                receiver.moving_right = False
            elif event.key == pygame.K_LEFT:
                receiver.moving_left = False
        


def update_screen(ai_settings, screen, receiver,ball):
    screen.fill((ai_settings.bg_color))
    receiver.blitme()
    ball.blitme()
    #collisions = pygame.sprite.groupcollide(receiver, balls, False, True)
    
    pygame.display.flip()

def update_balls(ai_settings,screen,ball,receiver):
        ball.update()
        
        #如果球与接球者发生碰撞，改变球的位置，输出改变了几次，也就代表你接住几次球.
        if pygame.sprite.collide_rect(ball, receiver):
            change_ball_rect(ball,ai_settings,screen)
            print(ai_settings.count)
        
        #如果没有接到球,球的个数减1，并暂停0.5秒，再改变球的位置
        if ball.rect.bottom >= ai_settings.screen_height:
            if ai_settings.balls > 1:
                ai_settings.balls -= 1 
                sleep(0.5)
                change_ball_rect(ball,ai_settings,screen)
            #如果没有球了，就不再改变球的位置，并打印game over
            else:
                ball.game_active == False
                print('game over')
                
                #pygame.quit()
                #sys.exit()
            #ball.rect.x = randint(1,ai_settings.screen_width)
            #ball.rect.y = 0
            
def change_ball_rect(ball,ai_settings,screen):
    ball.rect.x = randint(1,ai_settings.screen_width)
    ball.rect.y = 0  
    ai_settings.count+=1
        
        

