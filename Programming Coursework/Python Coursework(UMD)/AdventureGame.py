from pygame.locals import *
import pygame
import math
from time import sleep

display = pygame.display.set_mode((1300, 700), 0, 32)


class Player(object):
    x = 650
    y = 600

    def __init__(self):
        self.rect = pygame.rect.Rect((100, 100, 100, 100))
        self.velocity = 10
        self.is_jump = False
        self.jump_count = 10
        self.right = False
        self.left = False
        self.walk_count = 0
        self.running = True

    def controls(self):

        key = pygame.key.get_pressed()
        dist = 1
        if (key[K_RIGHT]):
            self.rect.move_ip(1, 0)

        if (key[K_LEFT]):
            self.player.moveLeft(1, 0)

    def draw(self, surface):
        pygame.draw.rect(display, (0, 0, 128), self.rect)

        #if (keys[K_UP]):
            #self.player.jump()

        #if (keys[K_ESCAPE]):
            #self._running = False
    def running(self, running):
        self.running = running
        self.running = True

    #def move_right(self):
        #self.x = self.x + self.velocity

    #def move_left(self):
        #self.x = self.x - self.velocity

    #def jump(self):
        #self.is_jump = 1

    #def update(self):
        #if self.is_jump:
            #if self.jump_count >= -10:
                #neg = 1
                #if self.jump_count < 0:
                    #neg = -1
                #self.y -= (self.jump_count ** 2) / 2 * neg
                #self.jump_count -= 1


pygame.init()
display.fill((255, 255, 255))

while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            pygame.display.update()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                square.player.moveRight()

            if (keys[K_LEFT]):
                square.player.moveLeft()

            if (keys[K_UP]):
                square.player.jump()

            if (keys[K_ESCAPE]):
                square._running = False


if __name__ == '__main__':
    main()


#square = Player(650, 600, 40, 60)

#screenwidth = 1300
#screenheight = 700


