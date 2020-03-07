import pygame  #导入pygame模块
from settings import Settings #导入settings.py的Settings类
from ship import Ship       #导入ship.py的Ship类
import game_functions as gf  #导入game_functions.py并设标签gf
from pygame.sprite import Group     
from game_stats import GameStats
"""
    
   按 F5 运行这个程序 ，你会启动Alicen Invasion游戏  按左右控制飞船移动

"""
     

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()       #ai_settings变量接收Settings对象

    #创建名为sceen的显示窗口
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #设置窗口名为Alien Invasion
    pygame.display.set_caption("Alien Invasion")  
    stats = GameStats(ai_settings)

    #创建一艘飞船,一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            #更新飞船位置
            ship.update()
            #删除已消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            #print(len(bullets))
            #更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        #更新屏幕上的图像，并切换到新屏幕
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
