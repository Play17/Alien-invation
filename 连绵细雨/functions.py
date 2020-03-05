import pygame
import sys
from yudi import Yudi

"""
        存放程序的相关事件函数
"""


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()


def update_screen(ai_settings, screen, yudis):
    #重绘窗口
    screen.fill(ai_settings.bg_color)
    #绘制雨滴
    yudis.draw(screen)
    #yudi.blitme()
    #让窗口可见
    pygame.display.flip()
    
def create_yudis(ai_settings, screen, yudis):
    yudi = Yudi(ai_settings, screen)
    yudi_width = yudi.rect.width
    for yudi_number in range(12):
        #for rows_number in range(4):
            yudi = Yudi(ai_settings, screen)
            yudi.x = 30+2 * yudi_number * yudi_width
            yudi.rect.x = yudi.x
            #yudi.rect.y = 10 + 2 * rows_number * yudi_width
            yudis.add(yudi)
            
def update_yudis(ai_settings,screen,yudis):
    yudis.update()

    #循环雨滴群
    for yudi in yudis.copy():
        #当雨滴超出屏幕(雨滴的底大于等于窗口的高)
        if yudi.rect.bottom >= ai_settings.screen_height:
            #移除超出窗口的雨滴
            yudis.remove(yudi)
       
    #print(len(yudis))    
    #if yudi.rect.bottom >= ai_settings.screen_height:  当雨滴超出屏幕(雨滴的底大于等于窗口的高)
        #create_yudis(ai_settings,screen, yudis)                创建雨滴群
    
    
    
    
    
    
    
    
    
    
    
    
    
