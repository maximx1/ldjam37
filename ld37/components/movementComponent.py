class MovementComponent:
    def update(self, entity, game_time):
        delta = game_time / 1000.0 * entity.speed
        entity.rect.x = entity.rect.x + entity.x_direction * delta
        entity.rect.y = entity.rect.y + entity.y_direction * delta
