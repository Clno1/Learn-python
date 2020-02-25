import sys
import pygame

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    #初始化游戏+创建一个屏幕
    pygame.init()
    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(screen)

    #游戏主循环
    while True:
        gf.check_events()    #监视键盘和鼠标事件
        gf.update_screen(ai_setting,screen,ship)  #更新屏幕
        
run_game()