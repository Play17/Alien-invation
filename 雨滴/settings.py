import pygame
"""
        设置类
"""
class Settings():
    def __init__(self):
        self.screen_width = 1200        #设置窗口宽度
        self.screen_height = 600         #设置窗口高度
        self.bg_color = 255,255,255    #设置窗口背景色
        
        self.yudi_speed_factor = 0.3    #设置雨滴下落速度
