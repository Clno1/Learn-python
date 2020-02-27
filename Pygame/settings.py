
class Settings():
    #存储《外星人入侵》游戏的设置

    def __init__(self):
        #屏幕及飞船
        self.screen_width=1200
        self.screen_height=700
        self.bg_color=(230,230,230)
        self.ship_speed=3
        self.ship_lives=2
        #子弹
        self.bullet_width=5
        self.bullet_height=10
        self.bullet_speed=3
        self.bullet_color=60,60,60
        self.bullets_total=5
        #敌人
        self.alien_speed=0.5
        self.fleet_drop_speed=50    #敌人撞壁之后向下移动速度
        self.fleet_direction=1      #取1/-1为向右/向左
        self.alien_points=10
