class GameStats():
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏刚启动时处于活动状态
        self.game_active = False

        #在任何时候都不应重置最高得分
        f = open("high_score.txt","r")
        self.high_score = int(f.read())
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
