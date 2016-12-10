import pygame, sys
from pygame.locals import *
from ld37.common.constants import Colors
from ld37.components.entity import Entity
from ld37.components.manualCharacterInputComponent import ManualCharacterInputComponent
from ld37.components.movementComponent import MovementComponent
from ld37.display.camera import Camera
from ld37.common.utils.libutils import update_image_rect

class Ldjam:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((800, 600))

    def setup(self):
        self.clock = pygame.time.Clock()
        self.pc = Entity(1, [ManualCharacterInputComponent(), MovementComponent()])
        self.pc.done = False
        self.pc.rect = pygame.rect.Rect(0, 0, 30, 30)
        self.pc.image = pygame.Surface((30,30))
        self.pc.speed = 200 #200 pixels/second
        self.camera = Camera(800, 600, 1600, 1200)

    def play(self):
        while not self.pc.done:
            game_time = self.clock.tick(60)
            self.screen.fill(Colors.WHITE)
            self.pc.update(game_time)
            self.camera.update(self.pc)

            update_image_rect(self.pc.image, self.pc.rect)

            self.screen.blit(self.pc.image, self.camera.apply(self.pc))

            #Gotta move this
            #pygame.draw.rect(self.screen, Colors.RED, self.pc.rect, 0)

            pygame.display.flip()
        pygame.quit()
