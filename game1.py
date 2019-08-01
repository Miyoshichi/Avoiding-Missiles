import pygame
from pygame.locals import *
from sys import exit

# Color defination
white = (255, 255, 255)
black = (0, 0, 0)
skyblue = (135, 206, 250)


# Class defination
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill(white)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        self.d = 10
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.d)
            print('up pressed')
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.d)
            print('down pressed')
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.d, 0)
            print('left pressed')
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.d, 0)
            print('right pressed')

# Objects initialization
pygame.init()
screen = pygame.display.set_mode((1080, 720))
screen.fill(black)
bg = pygame.Surface(screen.get_size())
bg.fill(skyblue)
player = Player()
clock = pygame.time.Clock()

# Main Window
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

# Move
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

# Visualization
    screen.blit(bg, (0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

# FPS controlling
    print(clock.tick())
    clock.tick(60)
