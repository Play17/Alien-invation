import pygame
from settings import Settings
import functions as f
from pygame.sprite import Group

"""
  主函数
"""

def run():
    #初始化窗口
    pygame.init                        

    #创建ai_settings存放Settings对象
    ai_settings = Settings()

    #设置窗口宽高
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    #设置窗口标题
    pygame.display.set_caption('yudi')

    #创建雨滴编组
    yudis = Group()
    
    #创建雨滴群
    f.create_yudis(ai_settings, screen, yudis)
    while True:
        #监听键盘事件
        f.check_events()
        #更新雨滴位置
        f.update_yudis(ai_settings,screen,yudis)
        #更新窗口
        f.update_screen(ai_settings, screen, yudis)
    
run()
