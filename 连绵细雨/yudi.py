import pygame
from pygame.sprite import Sprite

"""
        雨滴类
"""

class Yudi(Sprite):
    def __init__(self,ai_settings,screen):
        super(Yudi,self).__init__()
        self.ai_settings = ai_settings 
        self.screen = screen
        
        self.image = pygame.image.load('yu.jpg')    #加载雨滴的图片
        self.rect = self.image.get_rect()                     #获取图片的rect对象
        
        self.rect.x = self.rect.width                             #设置图片的x初始值为图片的宽度
        self.rect.y = 10                                                #设置图片的y初始值为10
        
        self.x = float(self.rect.x)                                 
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)               #绘制图片
        
    def update(self):
        self.rect.y += 1                                                #设置图片的y+=1,达成雨滴往下落的效果
        
