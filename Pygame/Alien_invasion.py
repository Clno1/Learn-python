import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
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
    #创建一个外星人编组
    aliens=Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    #游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)    #监视键盘和鼠标事件
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship,aliens, bullets)  #更新屏幕
       

run_game()