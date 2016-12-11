from ld37.entities.entity import *

def create_starting_entities():
    entities = []

    pc = create_playable_character(1, (0, 0), "left", "dennis")
    pc.is_current_player_controllable = True
    entities.append(pc)
    entities.append(create_static_object(2, (70, 70), True, True))
    entities.append(create_static_object(2, (105, 70), True, False))
    entities.append(create_static_object(2, (140, 70), False, True))
    entities.append(create_static_object(2, (175, 70), False, False))
    entities.append(create_static_object(2, (210, 70), True, True))

    for entity in entities:
        entity.master_entity_list = entities

    return entities
