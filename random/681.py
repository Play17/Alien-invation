import pygame
import sys
import random

"""

                    生成10个随机位置的681的图像

"""

def run():
    pygame.init()

    screen = pygame.display.set_mode((1200,600))

    pygame.display.set_caption('681')

    for lby in range(10):                                 #循环十个lby存储图片         
            lby = pygame.image.load('681.jpg')            #加载图片
            rect =lby.get_rect()                          #获取图片的rect对象来获取其位置
            rect.x = random.randint(1,1200)               #随机生成1~1200的数为rect.x
            rect.y = random.randint(1,600)                #随机生成1~600的数为rect.y
            screen.blit(lby, rect)                        #绘制图像
    
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
