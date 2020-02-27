#飞船类：管理飞船的行为
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        #init初始化飞船并设置其初始位置
        self.screen=screen
        self.ai_seettings=ai_settings

        #self.rect取得飞船矩形     self.screen_rect取得屏幕矩形
        self.image=pygame.image.load("images/ship.bmp")
        self.image=pygame.transform.scale(self.image,(50,50))   #缩放图像
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        '''
        可设置相应 rect 对象的属性center,centerx,centery 
        要让游戏元素与屏幕边缘对齐,可使用属性 top,bottom,left,right ；
        要调整游戏元素的水平或垂直位置，可使用属性 x,y ，它们分别是相应矩形左上角的 x 和 y 坐标。
        '''
        #将飞船放在屏幕最下方中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #移动标记
        self.moving_right=False
        self.moving_left=False

        #移动速度
        self.center=float(self.rect.centerx)

    def update(self):
        #根据移动标记调整飞船位置
        if self.moving_right and self.center<self.ai_seettings.screen_width:
            self.center+=self.ai_seettings.ship_speed
        if self.moving_left and self.center>0:
            self.center-=self.ai_seettings.ship_speed
        self.rect.centerx=int(self.center)

    def blitme(self):
        #根据self.rect的指定位置将飞船绘制到屏幕上
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx