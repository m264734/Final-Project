
import pygame
import math
from player import Player
from mallard import Mallard
import random

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font("../hunting_game/fonts/hunting.otf", 48)

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banner = []
guns = []
level = 1
# for i in range(1,4):
bgs = pygame.transform.scale(pygame.image.load(f"../hunting_game/assets/bgs/wetlands.jpg"), (WIDTH, HEIGHT))
banner = pygame.transform.scale(pygame.image.load(f"../hunting_game/assets/banner/banner2.png"), (WIDTH, 0.1*HEIGHT))
guns = pygame.transform.scale(pygame.image.load(f"../hunting_game/assets/guns/gun.png"), (100,100))

# def draw_gun():
#     mouse_pos = pygame.mouse.get_pos()
#     gun_point = (WIDTH/2, HEIGHT - 200)
#     lasers = ['red', 'purple', 'green']
#     clicks = pygame.mouse.get_pressed()
#     if mouse_pos[0] != gun_point[0]:
#         slope = (mouse_pos[1] - gun_point[1])/(mouse_pos[0] - gun_point[0])
#     else:
#         slope = -100000
#     angle = math.atan(slope)
#     rotation = math.degrees(angle)
#     if mouse_pos[0] < WIDTH/2:
#         gun = pygame.transform.flip(guns[level - 1], True, False)
#         if mouse_pos[1] < 600:
#             screen.blit(pygame.transform.rotate(gun, 90 - rotation), (WIDTH/2 - 90, HEIGHT - 250))
#             if clicks[0]:
#                 pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
#     else:
#         gun = guns[level - 1]
#         if mouse_pos[1] < 600:
#             screen.blit(pygame.transform.rotate(gun, 270 - rotation), (WIDTH/2 - 90, HEIGHT - 250))
#             if clicks[0]:
#                 pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
mallards= pygame.sprite.Group()
for i in range(10):
    x= random.uniform(0,1)
    y = int(random.uniform(0,400))
    # if x>.5:
    #     x= 600
    # else:
    #     x=0
    mallards.add(Mallard(x,y))
    i+=1

run = True
while run:
    timer.tick(fps)

    screen.fill('black')
    screen.blit(bgs, (0,0))
    screen.blit(banner, (0, 0.9*HEIGHT))
    mallards.update()
    mallards.draw(screen)

    # if level > 0:
    #     draw_gun()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player = Player(WIDTH / 2, HEIGHT / 2)

# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.quit:
#             running = False
#
#         player.stop()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 player.move_up()
#             if event.key == pygame.K_DOWN:
#                 player.move_down()
#             if event.key == pygame.K_LEFT:
#                 player.move_left()
#             if event.key == pygame.K_RIGHT:
#                 player.move_right()


    pygame.display.flip()
    pygame.quit