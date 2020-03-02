import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

"""
    
   按 F5 运行这个程序 ，你会启动Alicen Invasion游戏

"""
     

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    #创建名为sceen的显示窗口
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #设置窗口名为Alien Invasion
    pygame.display.set_caption("Alien Invasion")  
    
    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    
    #创建一个用于存储子弹的编组
    bullets = Group()
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        #更新飞船位置
        ship.update()
        #删除已消失的子弹
        gf.update_bullets(bullets)
        #print(len(bullets))
        #更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
