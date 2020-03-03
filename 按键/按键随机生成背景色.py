"""
    
    这个程序显示一个空屏幕.
    
    在事件循环中,每当检测到
    
    pygame.KEYDOWN事件
    
    随机生成背景色.运行这个
    
    程序，并按各种按键，看看

    Pygame如何响应

"""

import pygame
import sys
import random

def run():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    
    #创建名为sceen的宽600，高300的显示窗口
    screen = pygame.display.set_mode((600,400))
    
    #设置窗口标题
    pygame.display.set_caption("随意按下按键吧!")
    
    while True:
        for event in pygame.event.get():
            r= random.randint(1,255)
            g= random.randint(1,255)
            b= random.randint(1,255)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                screen.fill((r,g,b))
                #print(event.key)
        
        pygame.display.flip()


run()
