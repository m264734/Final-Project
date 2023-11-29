import pygame
import random
from parameters import *
from math import cos, sin

class Mallard(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("../hunting_game/images/mallard2.png").convert()
        self.image = pygame.transform.scale_by(self.image, .2)
        self.image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MALLARD_SPEED_MIN, MALLARD_SPEED_MAX)
        self.rect.center = (x, y)

    def update(self):
        self.x += self.speed
        self.rect.center = (self.x, self.y)

    #def update(self):
      #  self.x -= self.speed
       # self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

mallards = pygame.sprite.Group()