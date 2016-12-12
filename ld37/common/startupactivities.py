from ld37.entities.entity import *
from ld37.common.utils.worldManager import *
from ld37.common.utils.libutils import *
from ld37.common.utils.assetManager import AssetManager
from ld37.common.constants import PLAYER_ID

def create_starting_entities():
    asset_manager = AssetManager()
    world_loader = WorldLoader()
    entities = world_loader.build_entities()
    entities.extend(world_loader.build_world_from_seed())
    get_playable_entity_by_id(PLAYER_ID, entities).is_current_player_controllable = True

    for entity in entities:
        entity.master_entity_list = entities
        entity.asset_manager = asset_manager

    return entities
