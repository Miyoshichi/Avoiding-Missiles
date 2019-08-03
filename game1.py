# -*- coding:utf-8 -*-

'''
pygame Project: Avoiding Missiles
A personal project for learning python by coding a game using "pygame".

Coder: Ruri
2019-07-25 ~
'''

import pygame
from pygame.locals import *
from sys import exit
import random

# Color defination
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (192, 192, 192)
skyblue = (135, 206, 250)
orange = (255, 183, 76)


# Class defination
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((80, 20))
        self.surf.fill(grey)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        self.speed = 10
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            # print('up pressed')
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            # print('down pressed')
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            # print('left pressed')
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            # print('right pressed')
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1080:
            self.rect.right = 1080
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 720:
            self.rect.bottom = 720


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((40, 10))
        self.surf.fill(orange)
        self.rect = self.surf.get_rect(center=(1120, random.randint(21, 700)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Objects initialization
pygame.init()
pygame.display.set_caption('Avoiding Missiles')
screen = pygame.display.set_mode((1080, 720))
screen.fill(black)
bg = pygame.Surface(screen.get_size())
bg.fill(skyblue)
title_font = pygame.font.SysFont('arial', 60)
game_over = title_font.render("Game Over!", True, red)
player = Player()
clock = pygame.time.Clock()
life = 3

# Groups
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Event
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)

# Main Window
while 1:
    # FPS controlling
    # print(clock.tick())
    # print(life)
    clock.tick(60)

    # Living
    if life > 0:
        print(life)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == ADD_ENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        # Moving
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()

        # Visualization
        screen.blit(bg, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        pygame.display.flip()

        # Detecting life
        if pygame.sprite.spritecollideany(player, enemies):
            print('Defeted')
            player.kill()
            life -= 1
            player = Player()
            all_sprites.add(player)

    # Dead
    elif life == 0:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            else:
                screen.blit(game_over, (420, 330))
            pygame.display.flip()
