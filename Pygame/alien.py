
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('images/alien.bmp')
        self.image=pygame.transform.scale(self.image,(50,50))   #缩放图像
        self.rect=self.image.get_rect()

        #把飞船初始位置设为左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x,self.y=0.0,0.0


    def update(self):
        self.x+=self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        self.rect.x=int(self.x)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.right<=0:
            return True
        else:
            return False

    def blitme(self):
        self.screen.blit(self.image,self.rect)