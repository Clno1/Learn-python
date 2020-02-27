import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_function as gf

def run_game():
    #初始化游戏+创建一个屏幕
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    #Play按钮
    play_button=Button(ai_settings,screen,"Play")
    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    #创建用于存储子弹的编组
    bullets=Group()
    #创建一个外星人编组
    aliens=Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)
  
    #游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens,bullets)    #监视键盘和鼠标事件
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,stats,sb,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,sb,stats,ship,aliens, bullets,play_button)  #更新屏幕


run_game()