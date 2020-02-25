
import sys

import pygame

def check_events():
    #监测并响应键盘鼠标事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()


#功能：更新屏幕图像，绘制新的图像
def update_screen(ai_setting,screen,ship):
    #每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()