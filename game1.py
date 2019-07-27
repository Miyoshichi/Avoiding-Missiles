import pygame
from pygame.locals import *
import sys

# Color defination
white = (255, 255, 255)
black = (0, 0, 0)


# Function defination
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.surf.fill(white)
        self.rect = self.surf.get_rect()
player = Player()


# Initialization
pygame.init()
screen = pygame.display.set_mode((1600, 900))

# Main Window
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

# Blit
    screen.fill(black)
    screen.blit(player.surf, (775, 425))
    pygame.display.flip()
