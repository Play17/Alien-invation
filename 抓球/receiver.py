import pygame
from pygame.sprite import Sprite
class Receiver():
    def __init__(self,ai_settings,screen):
        
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/receiver.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        
        if self.moving_right and self.rect.right < self.ai_settings.screen_width:
            self.center += self.ai_settings.receiver_speed_factor
        
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.receiver_speed_factor

        self.rect.centerx = self.center
