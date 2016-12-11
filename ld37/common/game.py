import pygame, sys
from ld37.common.constants import Colors
from ld37.common.startupactivities import create_starting_entities
from ld37.display.camera import Camera
from ld37.common.utils.libutils import update_image_rect
from ld37.common.utils.libutils import get_playable_entity

class Ldjam:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.window_d = (800, 600)
        self.screen = pygame.display.set_mode(self.window_d)
        self.clock = pygame.time.Clock()
        self.master_entity_list = create_starting_entities()
        self.camera = Camera(self.window_d[0], self.window_d[1], 1800, 1400)

    def play(self):
        pc = get_playable_entity(self.master_entity_list)
        while not pc.done:
            # Set up tick
            pc = get_playable_entity(self.master_entity_list)
            game_time = self.clock.tick(45)
            self.screen.fill(Colors.WHITE)

            # update
            for entity in self.master_entity_list:
                entity.update(game_time)
            self.camera.update(pc)

            # clean up entities
            self.master_entity_list[:] = [x for x in self.master_entity_list if x.is_active]

            # display
            for entity in sorted([x for x in self.master_entity_list if x.is_displayable], key=lambda x: x.entity_id, reverse=True):
                update_image_rect(entity.image, entity.rect)
                self.screen.blit(entity.image, self.camera.apply(entity))

            pygame.display.flip()
        pygame.quit()
