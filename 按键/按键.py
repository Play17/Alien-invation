"""
    
    这个程序显示一个空屏幕.
    
    在事件循环中,每当检测到
    
    pygame.KEYDOWN事件时都打
    
    印属性event.key.运行这个
    
    程序，并按各种按键，看看
    Pygame如何响应

"""

import pygame
import sys

def run():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    
    #创建名为sceen的宽600，高300的显示窗口
    screen = pygame.display.set_mode((600,400))
    
    #设置窗口标题
    pygame.display.set_caption("随意按下按键吧!")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
    
    #让画面可见
    pygame.display.flip()


run()
