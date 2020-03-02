import pygame
import sys
from bullet import Bullet
                        
                        
def check_events(ai_settings, screen, ship, bullets):
        #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: #检测键盘按下事件 
            check_keydown_events(event, ai_settings, screen, ship, bullets)     #调用函数check_keydown_events
        elif event.type == pygame.KEYUP:    #检测键盘松开事件
            check_keyup_events(event, ship)         #调用函数check_keyup_events
               
                
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:     #如果按下方向键右键
        ship.moving_right = True          #飞船移动标志变位Tue，即说明飞船向右移动1
    elif event.key == pygame.K_LEFT:     #如果按下方向键左键
        ship.moving_left = True          #飞船移动标志变位Tue，即说明飞船向左移动1
    elif event.key == pygame.K_UP:     #如果按下方向键左键
        ship.moving_up = True          #飞船移动标志变位Tue，即说明飞船向左移动1
    elif event.key == pygame.K_DOWN:     #如果按下方向键左键
        ship.moving_down = True          #飞船移动标志变位Tue，即说明飞船向左移动1
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
        
        
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
    #创建一颗子弹,并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:     #如果松开方向键右键
        ship.moving_right = False        #飞船移动标志变False，即说明飞船不发生变化
    elif event.key == pygame.K_LEFT:     #如果松开方向键左键
        ship.moving_left = False        #飞船移动标志变False，即说明飞船不发生变化
    elif event.key == pygame.K_UP:     #如果松开方向键上键
        ship.moving_up = False          #飞船移动标志变False，即说明飞船不发生变化
    elif event.key == pygame.K_DOWN:     #如果松开方向键下键
        ship.moving_down = False          #飞船移动标志变变False，即说明飞船不发生变化

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环前都重绘屏幕
    screen.fill(ai_settings.bg_color)       #screen.fill()用背景色填充屏幕
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    #在指定位置绘制飞船
    ship.blitme()       
    
    #让绘制的屏幕可见
    pygame.display.flip()     

def update_bullets(bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
