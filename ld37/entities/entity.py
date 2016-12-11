import pygame
from ld37.common.constants import Colors
from ld37.entities.component import *
from ld37.entities.trigger import *

class Entity:
    def __init__(self, entity_id, components):
        self.entity_id = entity_id
        self.components = components
        self.setup()
        self.is_current_player_controllable = False
        self.is_displayable = False
        self.is_collidable = False
        self.speed = 0
        self.is_active = True

    def setup(self):
        return

    def update(self, game_time):
        for component in self.components:
            component.update(self, game_time)

def create_playable_character(entity_id, start_pos, size, starting_image_name):
    e = Entity(entity_id, [LinearMovementComponent((0.0, -1.0)), MovementComponent(), SpriteAnimationComponent()])
    e.done = False
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], size[0], size[1])
    e.speed = 50 #50 pixels/second
    e.x_direction = 0
    e.y_direction = 0
    e.is_displayable = True
    e.is_collidable = True
    e.current_delay_wait = 0
    e.delay = 500
    e.is_waiting = True

    sprite_name_components = starting_image_name.split("_")
    e.sprite_name = sprite_name_components[0]
    e.sprite_direction = sprite_name_components[1]
    e.sprite_step = sprite_name_components[2]
    e.time_since_last_step = 0
    return e

def create_static_object(entity_id, start_pos, size, img_name, is_displayable, is_collidable):
    e = Entity(entity_id, [StaticObjectAnimationComponent()] if img_name != "" else [])
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], size[0], size[1])
    e.image = pygame.Surface(size)
    e.img_name = img_name
    e.is_displayable = is_displayable
    e.is_collidable = is_collidable
    return e

def create_text_box(entity_id, start_pos, min_size, text, display_time):
    e = Entity(entity_id, [])
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], min_size[0], min_size[1])
    e.speed = 0
    e.is_displayable = True
    e.is_collidable = False
    e.text = text
    e.display_time = display_time
    return e

def create_trigger(entity_id, start_pos, size, trigger_str, trigger_props):
    e = Entity(entity_id, [TriggerComponent()])
    e.rect = pygame.rect.Rect(start_pos[0], start_pos[1], size[0], size[1])
    e.triggers = [lookup_trigger(trigger_str)]
    e.trigger_props = trigger_props
    return e
