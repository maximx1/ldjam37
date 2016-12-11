from ld37.entities.entity import *
from ld37.common.utils.worldManager import *
from ld37.common.utils.libutils import *

def create_starting_entities():
    entities = WorldLoader().build_entities()
    get_playable_entity_by_id(1, entities).is_current_player_controllable = True

    for entity in entities:
        entity.master_entity_list = entities

    return entities
