import pygame, sys
from pygame.locals import *
from ld37.common.constants import Colors

class Ldjam:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((800, 600))

    def setup(self):
        self.done = False
        return 0

    def play(self):
        while not self.done:
            self.screen.fill(Colors.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
        pygame.quit()
