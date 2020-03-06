import pygame
from random import randint
from pygame.sprite import Sprite
class Ball(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ball,self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/ball.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = randint(1,ai_settings.screen_width-self.rect.width)
        self.rect.y = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.ai_settings.ball_drop_speed

    
    