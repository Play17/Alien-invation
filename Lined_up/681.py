import pygame
import sys
import random

"""

            整齐排列681的图像

"""

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption('681')
    
    for lby in range(15):                                   #循环十个lby存储图片
            lby = pygame.image.load('681.jpg')              #加载图片
            rect =lby.get_rect()                            #获取图片的rect对象获取其位置
            for lby_number in range(5):                     #循环5个lby_number,代表每行5个
                for row_number in range(3):                 #循环3个row_number,代表有3行
                    rect.x = 150 + 2 * 100 * lby_number     #rect.x设置为150+ 2 * 100 * lby_number
                    rect.y = 100 + 2 * 70 * row_number      #rect.y设置为100 + 2 * 70 * row_number
                    #rect.x = 100
                    #rect.y = 100
                    screen.blit(lby, rect)                  #绘制图像
                    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

run()
