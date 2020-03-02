import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship0.jpg')

        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性centerx中存储小数值
        self.center = float(self.rect.centerx)
        self.bottomm = float(self.screen_rect.bottom)
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        #if self.moving_right and self.rect.right < self.screen_rect.right  (调用rect对象获取屏幕右边缘的值)
        if self.moving_right and self.rect.right < self.ai_settings.screen_width:  #如果移动标志时True并且飞船的x坐标小于窗口的宽(从设置里获取窗口宽)
            self.center += self.ai_settings.ship_speed_factor
        #if self.moving_left and self.rect.left > self.screen_rect.left     
        if self.moving_left and self.rect.left > 0:     #如果移动标志时True并且飞船的x坐标大于0
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottomm -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < 400:
            self.bottomm += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottomm 
            
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
