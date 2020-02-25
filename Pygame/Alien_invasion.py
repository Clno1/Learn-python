import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    #初始化游戏+创建一个屏幕
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建用于存储子弹的编组
    bullets=Group()

    #游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)    #监视键盘和鼠标事件
        ship.update()
        update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)  #更新屏幕
       

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    #print(len(bullets))


run_game()