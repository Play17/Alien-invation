import pygame  #导入pygame模块
import sys      #导入sys模块
from bullet import Bullet #导入bullet.py的Bullet类
from alien import Alien #导入alien.py的Alien类                        
from time import sleep

def check_events(ai_settings, screen, ship, bullets):
    #监视键盘和鼠标事件
    for event in pygame.event.get():       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:                                      #检测键盘按下事件 
            check_keydown_events(event, ai_settings, screen, ship, bullets)     #调用函数check_keydown_events
        elif event.type == pygame.KEYUP:                                        #检测键盘松开事件
            check_keyup_events(event, ship)                                     #调用函数check_keyup_events
               
                
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:         #如果按下方向键右键
        ship.moving_right = True            #飞船移动标志变位True，即说明飞船向右移动1
    elif event.key == pygame.K_LEFT:        #如果按下方向键左键
        ship.moving_left = True             #飞船移动标志变位True，即说明飞船向左移动1
    elif event.key == pygame.K_UP:          #如果按下方向键上键
        ship.moving_up = True               #飞船移动标志变True，即说明飞船向左移动1
    elif event.key == pygame.K_DOWN:        #如果按下方向键下键
        ship.moving_down = True             #飞船移动标志变位True，即说明飞船向左移动1
    elif event.key == pygame.K_SPACE:       #按下空格键
        fire_bullet(ai_settings, screen, ship, bullets) #发射子弹
    elif event.key == pygame.K_q:           #按下q 退出游戏  (退出快捷键,测试用)
        pygame.quit()
        sys.exit()
        
        
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
    #创建一颗子弹,并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:         #如果松开方向键右键
        ship.moving_right = False           #飞船移动标志变False，即说明飞船不发生变化
    elif event.key == pygame.K_LEFT:        #如果松开方向键左键
        ship.moving_left = False            #飞船移动标志变False，即说明飞船不发生变化
    elif event.key == pygame.K_UP:          #如果松开方向键上键
        ship.moving_up = False              #飞船移动标志变False，即说明飞船不发生变化
    elif event.key == pygame.K_DOWN:        #如果松开方向键下键
        ship.moving_down = False            #飞船移动标志变变False，即说明飞船不发生变化

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环前都重绘屏幕
    screen.fill(ai_settings.bg_color)       #screen.fill()用背景色填充屏幕
    
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    #在指定位置绘制飞船
    ship.blitme()

    #在指定位置绘制外星人
    aliens.draw(screen)
    
    #让绘制的屏幕可见
    pygame.display.flip()     

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:  #如果子弹的下方小于=0，代表超出屏幕
            bullets.remove(bullet)      #print(len(bullets)) 输出子弹数 测试用
            
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
    
    
    
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    """响应子弹和外星人的碰撞"""
    #删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        #删除现有的子弹并创建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人之间的间距为外星人宽度
    alien = Alien(ai_settings, screen)
      
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    #print(number_aliens_x)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    #创建外星人群
    for alien_number in range(number_aliens_x):
        #创建一个外星人并将其加入当前行
        for row_number in range(number_rows):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def get_number_aliens_x(ai_settings,alien_width):         
    """计算每行可容纳多少外星人"""
    #每一行可容纳外星人的水平空间 = 窗口宽度窗口宽度- (2 X 外星人的宽)
    availiable_space_x = ai_settings.screen_width - 2 * alien_width   
    #每一行可容纳外星人数 = 可容纳外星人的水平空间 /  (2 X 外星人的宽)      
    number_aliens_x = int(availiable_space_x / (2 * alien_width))        
    return number_aliens_x        
            
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = 30 + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y =  30 + alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (10 * alien_height) - ship_height)
    number_rows = int(available_space_y / alien_height)
    return number_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        #print("Ship hit!!!")
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    
def check_fleet_edges(ai_settings, aliens):
    #循环外星人群
    for alien in aliens.sprites():
        #检查外星人是否接触到屏幕边缘
        if alien.check_edges():
            #改变外星人的位置
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    #循环外星人群
    for alien in aliens.sprites():
        #让外星人下落
        alien.rect.y += ai_settings.fleet_drop_speed
    #把fleet_direction的值乘-1,从而改变外星人水平移动方向
    ai_settings.fleet_direction *= -1
   
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        #将ships_left减1
        stats.ships_left -= 1
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人,并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
        
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞到一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
































   









    
            
