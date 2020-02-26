
import sys
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
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)

#功能：更新屏幕图像，绘制新的图像
def update_screen(ai_setting,screen,ship,aliens,bullets):
    #每次循环都重绘屏幕
    screen.fill(ai_setting.bg_color)
    #更新子弹group内子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #让最近绘制的屏幕可见
    pygame.display.flip()

#更新子弹
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    #print(len(bullets))

#创建外星人舰队：
def creat_fleet(ai_settings,screen,ship,aliens):
    #创建一个外星人，并计算每行可容纳多少个外星人
    alien=Alien(ai_settings,screen)
    number_aliens_x=calc_aliens_number(ai_settings,alien.rect.width)
    row_numbers=calc_row_number(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
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
def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

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
