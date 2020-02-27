
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

#响应键盘按下事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

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
def check_events(ai_settings, screen, stats, play_button, ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_buttons(ai_settings,screen,stats,play_button,mouse_x,mouse_y,ship,aliens,bullets)
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

def check_play_buttons(ai_settings,screen,stats,play_button,mouse_x,mouse_y,ship,aliens,bullets):
    if not stats.game_active and play_button.rect.collidepoint(mouse_x, mouse_y):
        pygame.mouse.set_visible(False)

        stats.reset_stats
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        creat_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

#功能：更新屏幕图像，绘制新的图像
def update_screen(ai_settings, screen,stats,ship,aliens, bullets,play_button):
    #每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    #更新子弹group内子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 如果游戏处于非活动状态，就绘制 Play 按钮
    if not stats.game_active:
        play_button.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()

#更新子弹
def update_bullets(ai_settings,screen,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    #print(len(bullets))
    #内置函数：一行就双重遍历子弹和敌人，矩形重叠就消失
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    #检测现有敌人是否为0了
    if len(aliens)==0:
        bullets.empty()
        creat_fleet(ai_settings,screen,ship,aliens)

#创建外星人舰队：
def creat_fleet(ai_settings,screen,ship,aliens):
    #创建一个外星人，并计算每行可容纳多少个外星人
    alien=Alien(ai_settings,screen)
    number_aliens_x=calc_aliens_number(ai_settings,alien.rect.width)
    row_numbers=calc_row_number(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x-1):
            creat_an_alien(ai_settings,screen,aliens,alien_number,row_number)
        

def creat_an_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height + 2 * alien.rect.height * row_number
    alien.x=float(alien.rect.x)
    alien.y=float(alien.rect.y)
    aliens.add(alien)

def calc_aliens_number(ai_settings,alien_width):
    #公式计算
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def calc_row_number(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

#更新外星人
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        print("Xiba!!!")

def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_direction(ai_settings,aliens)
            break

def change_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.y+=ai_settings.fleet_drop_speed
        alien.rect.y=int(alien.y)
    ai_settings.fleet_direction*=-1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ship_lives>0:
        stats.ship_lives-=1

        aliens.empty()
        bullets.empty()

        creat_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        sleep(1)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

""" 更新屏幕上的图像，并切换到新屏幕 """
def update_screen(ai_settings, screen, stats, ship, aliens, bullets,play_button):
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    #更新子弹group内子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 如果游戏处于非活动状态，就绘制 Play 按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()