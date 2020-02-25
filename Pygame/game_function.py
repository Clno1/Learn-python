
import sys
import pygame
from bullet import Bullet

#响应键盘按下事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    #监测到按下空格键：创建一颗子弹
    if len(bullets)<ai_settings.bullets_total:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

#响应键盘回弹事件
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

#监测并响应键盘鼠标事件
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

#功能：更新屏幕图像，绘制新的图像
def update_screen(ai_setting,screen,ship,bullets):
    #每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    #更新子弹group内子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()