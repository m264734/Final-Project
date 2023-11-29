import pygame
import random
from parameters import *
from math import cos, sin

class Hunter(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("../hunting_game/images/shotgun4.png").convert()
        self.image = pygame.transform.scale_by(self.image, .2)
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(HUNTER_SPEED_MIN, HUNTER_SPEED_MAX)
        self.rect.center = (x, y)

    def update(self):
        self.x += self.speed
        self.rect.center = (self.x, self.y)
