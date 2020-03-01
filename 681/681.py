"""

    运行这个程序，
    显示一个窗口，
    控制其中的681
    不让她移动出屏幕
    
"""

import sys
import pygame

def run_681():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    
    #创建width_height放置窗口的宽高
    width_height = (1200,600)
    #创建bg_color放置窗口的背景色
    bg_color = (255,255,255)
    
    screen = pygame.display.set_mode(width_height)
    
    pygame.display.set_caption("681")
    
    lby = Lby(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lby.moving_right = True
                elif event.key == pygame.K_LEFT:
                    lby.moving_left = True
                elif event.key == pygame.K_UP:
                    lby.moving_up = True
                elif event.key == pygame.K_DOWN:
                    lby.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    lby.moving_right = False
                elif event.key == pygame.K_LEFT:
                    lby.moving_left = False
                elif event.key == pygame.K_UP:
                    lby.moving_up = False
                elif event.key == pygame.K_DOWN:
                    lby.moving_down = False
        
        #更新681的位置
        lby.update() 
        #在每次循环前重绘屏幕  更新背景色
        screen.fill(bg_color)
        
        
        #在每次循环前绘制681
        lby.blitme() 
        #让绘制的屏幕可见
        pygame.display.flip()
        
        

        
        

class Lby():
    def __init__(self, screen):
        self.screen = screen
        #加载681并获取其外接矩形
        self.image = pygame.image.load('ship1.jpg')

        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        #将681放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right:
            self.rect.centerx+=10
        elif self.moving_left:
            self.rect.centerx-=10
        elif self.moving_up:
            self.rect.bottom-=10
        elif self.moving_down:
            self.rect.bottom+=10
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)




run_681()
