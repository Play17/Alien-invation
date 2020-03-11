import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图像,并设置其rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()   #获取外星人图像rect对象获取位置信息
        
        #每个外星人最初都在屏幕    左上角附近
        self.rect.x = self.rect.width       #将外星人的左边距设置为外星人图像的宽度        
        self.rect.y = self.rect.height      #将外星人的上边距设置为外星人图像的高度
        
        #存储外星人的准确位置
        self.x = float(self.rect.x)
    
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
   
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right - 30:
            return True
        elif self.rect.left <= 0:
            return True
            
            
                
            
            
