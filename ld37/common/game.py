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
        self.clock = pygame.time.Clock()
        return 0

    def play(self):
        while not self.done:
            self.screen.fill(Colors.WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
