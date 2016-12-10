import pygame, sys
from pygame.locals import *
from ld37.common.constants import Colors
from ld37.components.entity import Entity
from ld37.components.manualCharacterInputComponent import ManualCharacterInputComponent
from ld37.components.movementComponent import MovementComponent

class Ldjam:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((800, 600))

    def setup(self):
        self.clock = pygame.time.Clock()
        self.pc = Entity(1, [ManualCharacterInputComponent(), MovementComponent()])
        self.pc.done = False
        self.pc.x_loc = 0
        self.pc.y_loc = 0
        self.pc.speed = 200 #200 pixels/second

    def play(self):
        while not self.pc.done:
            game_time = self.clock.tick(60)
            self.screen.fill(Colors.WHITE)
            self.pc.update(game_time)

            #Gotta move this
            pygame.draw.rect(self.screen, Colors.RED, [self.pc.x_loc, self.pc.y_loc, 30, 30], 0)

            pygame.display.flip()

        pygame.quit()
