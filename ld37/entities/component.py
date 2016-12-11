import pygame

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
        delta = game_time / 1000.0 * entity.speed
        entity.oldrect = pygame.rect.Rect(entity.rect.x, entity.rect.y, entity.rect.w, entity.rect.h)
        entity.rect.x = entity.rect.x + entity.x_direction * delta
        entity.rect.y = entity.rect.y + entity.y_direction * delta


class CollisionComponent:
    def update(self, entity, game_time):
        for collidable in [x for x in entity.master_entity_list if x.is_collidable and entity.entity_id != x.entity_id]:
            if entity.rect.colliderect(collidable.rect):
                self.collide_x(entity, collidable)
            if entity.rect.colliderect(collidable.rect):
                self.collide_y(entity, collidable)

    def collide_x(self, entity, collidable):
        if entity.x_direction > 0:
            entity.rect.right = entity.oldrect.right
        elif entity.x_direction < 0:
            entity.rect.left = entity.oldrect.left

    def collide_y(self, entity, collidable):
        if entity.y_direction > 0:
            entity.rect.bottom = entity.oldrect.bottom
        elif entity.y_direction < 0:
            entity.rect.top = entity.oldrect.top
