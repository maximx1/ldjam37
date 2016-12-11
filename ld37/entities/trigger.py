from ld37.common.utils.libutils import *
from ld37.entities.component import *

def lookup_trigger(prop):
    if prop == "music":
        return MusicTrigger()
    if prop == "resumecontrol":
        return ResumePlayerControlTrigger()

class MusicTrigger:
    def check(self, entity, game_time):
        return entity.is_active and entity.rect.colliderect(get_playable_entity_by_id(1, entity.master_entity_list).rect)

    def activate(self, entity, game_time):
        entity.asset_manager.load_song(entity.trigger_props["song"])
        entity.is_active = False

class ResumePlayerControlTrigger:
    def check(self, entity, game_time):
        return entity.is_active and entity.rect.colliderect(get_playable_entity_by_id(1, entity.master_entity_list).rect)

    def activate(self, entity, game_time):
        pc = get_playable_entity_by_id(1, entity.master_entity_list)
        del pc.components[0]
        pc.components.insert(0, ManualCharacterInputComponent())
        entity.is_active = False
