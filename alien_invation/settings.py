class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200         #窗口宽
        self.screen_height = 600        #窗口高
        self.bg_color = (255,255,255)   #窗口背景色，白色
        
        #飞船移动速度
        self.ship_speed_factor = 1
        self.ship_limit = 3             #初始飞船数    
        
        #子弹设置
        self.bullet_speed_factor = 1    #子弹速度
        self.bullet_width = 3           #子弹宽
        self.bullet_height = 15         #子弹高
        self.bullet_color = 60,60,60    #子弹颜色，黑色
        self.bullets_allowed = 5        #子弹数量
        
        #外星人设置 
        self.alien_speed_factor = 0.5   #外星人移动速度
        self.fleet_drop_speed = 10      #外星人下落速度
        self.fleet_direction = 1        #1代表往右移动，-1代表往左移动
