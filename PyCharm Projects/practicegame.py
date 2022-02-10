from pygame.locals import *
import pygame
import math
from time import sleep


class player(object):
    def __init__(self, x, y, width, height):
    self.x = 10
    y = 500
    speed = 10

    # Stores if player is jumping or not.
    isjump = 0

    # Force (v) up and mass m.
    v = 8
    m = 2

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def jump(self):
        self.isjump = 1

    def update(self):
        self.isjump = 1


class App:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = player()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.draw.rect(self._display_surf, (250, 0, 0), (0, 0, 30, 30), 0)

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.update()
        pygame.display.flip()
        sleep(0.03)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.jump()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()