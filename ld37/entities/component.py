import pygame
from ld37.common.utils.libutils import detect_collision
from ld37.common.constants import Colors
class DrawComponent:
    def update(entity, game_time):
        pygame.draw.rect()

class ManualCharacterInputComponent:
    def update(self, entity, game_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                entity.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    entity.done = True

        keys_pressed = pygame.key.get_pressed()

        entity.x_direction = 0
        entity.y_direction = 0
        if keys_pressed[pygame.K_a]:
            entity.x_direction = -1
        if keys_pressed[pygame.K_d]:
            entity.x_direction = 1
        if keys_pressed[pygame.K_w]:
            entity.y_direction = -1
        if keys_pressed[pygame.K_s]:
            entity.y_direction = 1

class MovementComponent:
    def update(self, entity, game_time):
        if entity.x_direction != 0:
            delta = game_time / 1000.0 * entity.speed
            entity.rect.x = entity.rect.x + entity.x_direction * delta
            if entity.is_collidable:
                detect_collision(entity, entity.x_direction, 0)
        if entity.y_direction != 0:
            delta = game_time / 1000.0 * entity.speed
            entity.rect.y = entity.rect.y + entity.y_direction * delta
            if entity.is_collidable:
                detect_collision(entity, 0, entity.y_direction)

class StaticObjectAnimationComponent:
    def update(self, entity, game_time):
        entity.image = entity.asset_manager.request_texture(entity.img_name)

class TextBoxAnimationComponent:
    def update(self, entity, game_time):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 12)
        text_surface = font.render(entity.text, False, Colors.WHITE)
        text_dimension = font.size(entity.text)
        textbox = pygame.Surface(text_dimension).fill(Colors.BLACK)
        textbox.blit(text_surface, (entity.pos_x, entity.pos_y))
        entity.image = textbox

class SpriteAnimationComponent:
    def update(self, entity, game_time):
        if entity.x_direction > 0 and (entity.sprite_direction == "left" or entity.y_direction == 0)  :
            entity.sprite_direction = "right"
        elif entity.x_direction < 0 and (entity.sprite_direction == "right" or entity.y_direction == 0):
            entity.sprite_direction = "left"

        if entity.y_direction > 0 and (entity.sprite_direction == "up" or entity.x_direction == 0):
            entity.sprite_direction = "down"
        elif entity.y_direction < 0 and (entity.sprite_direction == "down" or entity.x_direction == 0):
            entity.sprite_direction = "up"

        entity.time_since_last_step += game_time
        if entity.x_direction != 0 or entity.y_direction != 0:
            entity.sprite_step = str(((entity.time_since_last_step % 1024) / 256) + 1)

        image_name = entity.sprite_name + "_" + entity.sprite_direction + "_" + entity.sprite_step

        entity.image = entity.asset_manager.request_texture(image_name)
