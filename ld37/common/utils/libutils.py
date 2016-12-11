import math
import pygame

def update_image_rect(image, rect):
    image_rect = image.get_rect()
    image_rect.x = rect.x
    image_rect.y = rect.y

def distance_between_rects(rect1, rect2):
    (r1_center_x, r1_center_y) = rect1.center
    (r2_center_x, r2_center_y) = rect2.center
    x_squared = (r2_center_x - r1_center_x)**2
    y_squared = (r2_center_y - r1_center_y)**2
    return math.sqrt(x_squared + y_squared)

def detect_collision(entity, x_direction, y_direction):
    for collidable in [x for x in entity.master_entity_list if x.is_collidable and entity.entity_id != x.entity_id]:
        if entity.rect.colliderect(collidable.rect):
            if x_direction > 0:
                entity.rect.right = collidable.rect.left
            if x_direction < 0:
                entity.rect.left = collidable.rect.right
            if y_direction > 0:
                entity.rect.bottom = collidable.rect.top
            if y_direction < 0:
                entity.rect.top = collidable.rect.bottom

def get_playable_entity(entities):
    return next(iter([x for x in entities if x.is_current_player_controllable]), None)

def get_playable_entity_by_id(entity_id, entities):
    return next(iter([x for x in entities if x.entity_id == entity_id]), None)

class ImageUtils:
    def __init__(self, image):
        self.image = image

    def scale(self, newWidth, newHeight) :
        self.image = pygame.transform.scale(self.image, (newWidth, newHeight))
        return self

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        return self

    def flip_vertical(self):
        self.image = pygame.transform.flip(self.image, False, True)
        return self

    def flip_horizontal(self):
        self.image = pygame.transform.flip(self.image, True, False)
        return self

    def get_image(self):
        return self.image
