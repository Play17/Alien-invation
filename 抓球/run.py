import pygame
from settings import Settings
import game_functions as gf
from receiver import Receiver
from ball import Ball


def run():
    pygame.init
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    receiver = Receiver(ai_settings, screen)
    ball = Ball(ai_settings,screen)
    
    
    while True:
        gf.check_events(receiver)
        gf.update_balls(ai_settings,screen,ball,receiver)
        receiver.update()
        gf.update_screen(ai_settings,screen,receiver,ball)

run()
