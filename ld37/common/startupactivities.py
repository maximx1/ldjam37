from ld37.entities.entity import *

def create_starting_entities():
    entities = []

    pc = create_playable_character(1, (0, 0))
    pc.is_current_player_controllable = True
    entities.append(pc)
    entities.append(create_static_collidable(2, (70, 70)))

    for entity in entities:
        entity.master_entity_list = entities

    return entities
