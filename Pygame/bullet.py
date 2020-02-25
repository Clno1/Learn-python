
import pygame

from pygame.sprite import Sprite

#子弹类：对飞船子弹进行管理，继承自Sprite
class Bullet(Sprite):
    #__init__在飞船位置创建一颗子弹
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen

        #在 (0,0) 处创建一个表示子弹的矩形，再设置正确的位置
        self.rect=pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        #x轴设为飞船x轴
        self.rect.centerx = ship.rect.centerx   
        self.rect.top = ship.rect.top   #
  
        #记录self.y值用于以后改变，self.x不会变不用记录
        self.y=float(self.rect.y)

        #子弹颜色和速度
        self.color=ai_settings.bullet_color
        self.bullet_speed=ai_settings.bullet_speed

    #update将子弹向上移动
    def update(self):
        self.y-=self.bullet_speed
        self.rect.y=int(self.y)

    def draw_bullet(self):
        #用self.color的颜色填充self.screen的self.rect的矩形部分
        pygame.draw.rect(self.screen,self.color,self.rect)