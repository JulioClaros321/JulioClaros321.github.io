import math
import pygame
from time import sleep
from pygame.locals import *


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
floor = 450


class player(object):

    def __init__(self):
        self.x = 450
        self.y = 450
        self.velocity = 10
        self.mass = 2
        self.blocks = 10
        self.floor = 450
        self.jump = False
        self.running = True
        self.right = False
        self.left = False

    def game_update(self):
        display.fill(black)
        pygame.draw.rect(display, white, [first_player.x, first_player.y, 70, 70])
        pygame.display.update()

    def game_engine(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        pygame.time.delay(20)
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            first_player.x += first_player.velocity

        if keys[K_LEFT]:
            first_player.x -= first_player.velocity

        if not first_player.jump:
            if (keys[K_SPACE]):
                first_player.jump = True

        else:
            if first_player.blocks >= -10:
                neg = 1
                if first_player.blocks < 0:
                    neg = -1
                first_player.y -= neg * (
                            .5 * first_player.mass * (first_player.blocks ** 2))
                first_player.blocks -= 1
            else:
                first_player.jump = False
                first_player.blocks = 10

        first_player.game_update()


display = pygame.display.set_mode((1300, 700), 0, 32)
pygame.display.set_caption("Adventure Game")
running = True
first_player = player()

while first_player.running:
    first_player.game_engine()

