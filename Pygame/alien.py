
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

        #
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)