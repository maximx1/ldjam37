from ld37.common.utils.libutils import *

def lookup_trigger_props(trigger_str):
    toks = trigger_str.split("_")
    return [y for y in [look_up_trigger(x) for x in toks] if y]

def look_up_trigger(prop, ):
    if prop == "music":
        return MusicTrigger()

class MusicTrigger:
    def check(self, entity, game_time):
        return entity.is_active and entity.rect.colliderect(get_playable_entity_by_id(1, entity.master_entity_list))

    def activate(self, entity, game_time):
        entity.asset_manager.load_song(entity.trigger_props["song"])
        entity.is_active = False
