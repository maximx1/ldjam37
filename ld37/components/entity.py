class Entity:
    def __init__(self, id, components):
        self.id = id
        self.components = components
        self.setup()

    def setup(self):
        return

    def update(self, game_time):
        for component in self.components:
            component.update(self, game_time)
