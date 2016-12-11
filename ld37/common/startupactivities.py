from ld37.entities.entity import *
from ld37.common.utils.worldManager import *
from ld37.common.utils.libutils import *
from ld37.common.utils.assetManager import AssetManager

def create_starting_entities():
    asset_manager = AssetManager()
    # asset_manager.load_song("BGM_2") # Moving this into a trigger.

    entities = WorldLoader().build_entities()
    get_playable_entity_by_id(1, entities).is_current_player_controllable = True

    for entity in entities:
        entity.master_entity_list = entities
        entity.asset_manager = asset_manager

    return entities
