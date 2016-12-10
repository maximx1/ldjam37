import pygame
from ld37.entities.component import *

class Entity:
    def __init__(self, entity_id, is_displayable, components):
        self.entity_id = entity_id
        self.components = components
        self.setup()
        self.is_current_player_controllable = False
        self.is_displayable = is_displayable

    def setup(self):
        return

    def update(self, game_time):
        for component in self.components:
            component.update(self, game_time)

def create_playable_character(entity_id):
    pc = Entity(entity_id, True, [ManualCharacterInputComponent(), MovementComponent()])
    pc.done = False
    pc.rect = pygame.rect.Rect(0, 0, 30, 30)
    pc.image = pygame.Surface((30,30))
    pc.speed = 200 #200 pixels/second
    return pc
