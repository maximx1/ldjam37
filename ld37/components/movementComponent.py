class MovementComponent:
    def update(self, entity, game_time):
        delta = game_time / 1000.0 * entity.speed
        entity.x_loc = entity.x_loc + entity.x_direction * delta
        entity.y_loc = entity.y_loc + entity.y_direction * delta
