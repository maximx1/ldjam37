import json
from ld37.common.constants import Colors
from ld37.entities.entity import *

class WorldLoader:
    def __init__(self):
        self.data = self.get_world_data()

    def get_world_data(self):
        with open('assets/world_map.json') as f:
            return json.loads(f.read())

    def build_entities(self):
        return [self.build_entity(x) for x in self.data]

    def build_entity(self, entity):
        if "playable_character" == entity["type"]:
            return create_playable_character(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["starting_image"])
        if "obj_st_disp_coll" == entity["type"]:
            return create_static_object(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["starting_image"], True, True)
        if "obj_st_disp" == entity["type"]:
            return create_static_object(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["starting_image"], True, False)
        if "obj_st_coll" == entity["type"]:
            return create_static_object(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["starting_image"], False, True)
        if "obj_st" == entity["type"]:
            return create_static_object(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["starting_image"], False, False)
        if "obj_st_disp_coll" == entity["type"]:
            return create_static_object(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["starting_image"], True, True)
        if "trigger" == entity["type"]:
            return create_trigger(entity["entity_id"], (entity["start_pos"]["x"], entity["start_pos"]["y"]), (entity["dimension"]["w"], entity["dimension"]["h"]), entity["triggers"], entity["trigger_props"])
