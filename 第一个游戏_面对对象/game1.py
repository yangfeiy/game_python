import sys
import cfg
import math
import random
import pygame
from moudule import *

def initgame():
    pygame.init()
    pygame.mixer.init()

    screen=pygame.display.set_mode((cfg.SCREENSIZE),0,32)
    pygame.display.set_caption("杨飞宇第一个python程序——面对对象进行编写")
    game_image={}
    for key,value in cfg.IMAGE_PATHS.items():
        game_image[key]=pygame.image.load(value)
        print(value)
    game_sound={}
    for key,value in cfg.SOUNDS_PATHS.items():
        game_sound[key]=pygame.mixer.Sound(value)
    return screen,game_sound,game_image

def main():
    screen, game_sound , game_image = initgame()
    font = pygame.font.Font(None, 50)
    #加载音乐
    pygame.mixer.music.load(cfg.SOUNDS_PATHS['moonlight'])
    pygame.mixer.music.play(-1, 0.0)
    #加载兔子
    bunny=BunnySprite(image=game_image.get('rabbit'),position=(100, 100))
    #用组管理所有的箭头
    arrow_sprites_group = pygame.sprite.Group()
    #用组的方式管理獾
    badguy_sprites_group = pygame.sprite.Group()
    badguy = BadguySprite(game_image.get('badguy'), position=(640, 100))
    badguy_sprites_group.add(badguy)
    #定义定时器
    badtimer =100
    badtimer1=0
    #血量值
    healthvalue = 194
    #用来追踪射出箭头的数量和獾的数量
    acc_record = [0., 0.]
    # 游戏主循环 running =1 程序开始运行
    running, exitcode = True, False
    clock = pygame.time.Clock()
    while running:
        screen.fill(0)
        for x in range(cfg.SCREENSIZE[0] // game_image['grass'].get_width() + 1):
            for y in range(cfg.SCREENSIZE[1] // game_image['grass'].get_height() + 1):
                screen.blit(game_image['grass'], (x * 100, y * 100))
        for t in range(20,cfg.SCREENSIZE[1],cfg.SCREENSIZE[1]//4):
            screen.blit(game_image['castle'], (0,t))
        #计时
        countdown_text = font.render(str((90000-pygame.time.get_ticks())//60000)+":"+str((90000-pygame.time.get_ticks())//1000%60).zfill(2), True, (0, 0, 0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topright = [600, 10]
        screen.blit(countdown_text, countdown_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
               # game_sounds['shoot'].play()
                acc_record[1] += 1
                mouse_pos = pygame.mouse.get_pos()
                angle = math.atan2(mouse_pos[1] - (bunny.rotated_position[1] + 32),
                                   mouse_pos[0] - (bunny.rotated_position[0] + 26))
                arrow = ArrowSprite(game_image.get('arrow'),
                                    (angle, bunny.rotated_position[0] + 32, bunny.rotated_position[1] + 26))
                arrow_sprites_group.add(arrow)
        #移动兔子
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            bunny.move(cfg.SCREENSIZE, 'up')
        elif key_pressed[pygame.K_s]:
            bunny.move(cfg.SCREENSIZE, 'down')
        elif key_pressed[pygame.K_a]:
            bunny.move(cfg.SCREENSIZE, 'left')
        elif key_pressed[pygame.K_d]:
            bunny.move(cfg.SCREENSIZE, 'right')
        #更新箭头
        for arrow in arrow_sprites_group:
            if arrow.update(cfg.SCREENSIZE):
                arrow_sprites_group.remove(arrow)
        #加入新的獾
        if badtimer ==0:
            badguy=BadguySprite(image=game_image.get('badguy'),position=(cfg.SCREENSIZE[0]-64,random.randint(20, cfg.SCREENSIZE[1]-32)))
            badguy_sprites_group.add(badguy)
            #通过这个时间来设置难度
            badtimer = 100 - (badtimer1 * 2)
            badtimer1 = 20 if badtimer1 >= 20 else badtimer1 + 2
        badtimer -= 1
        #更新獾的数量
        for badguy in badguy_sprites_group:
            if badguy.update():
                healthvalue -=random.randint(4,8)
                badguy_sprites_group.remove(badguy)
        #碰撞检测
        for arrow in arrow_sprites_group:
            for badguy in badguy_sprites_group:
                if pygame.sprite.collide_mask(arrow, badguy):
                  #  game_sounds['enemy'].play()
                    arrow_sprites_group.remove(arrow)
                    badguy_sprites_group.remove(badguy)
                    acc_record[0] += 1
        #画出箭头
        arrow_sprites_group.draw(screen)
        #画出兔子
        bunny.draw(screen, pygame.mouse.get_pos())
        #画出獾
        badguy_sprites_group.draw(screen)
        #画出血条值
        screen.blit(game_image.get('healthbar'), (5, 5))
        for i in range(healthvalue):
             screen.blit(game_image.get('health'), (i + 8, 8))
        #判断游戏是不是结束
        if pygame.time.get_ticks() >= 90000:
            running, exitcode = False, True
        #血条进行判断
        if healthvalue <= 0:
            running, exitcode = False, False
        pygame.display.flip()
    accuracy = acc_record[0] / acc_record[1] * 100 if acc_record[1] > 0 else 0
    accuracy = '%.2f' % accuracy
    showEndGameInterface(screen, exitcode,game_image,accuracy)

if __name__ =='__main__':
    main()


