import json
import pygame

class AssetManager:
    'Use this to get all of the resources'
    asset_dictionary = {}
    json_dict = {}

    def __init__(self):
        if len(AssetManager.json_dict) == 0:
            asset_file = open("assets/asset_map.json")
            file_text = asset_file.read()
            AssetManager.json_dict = json.loads(file_text)

    def request_texture(self, name):
        'Get a texture surface with specified name'
        texture_key = "Texture_" + name
        if AssetManager.asset_dictionary.get(texture_key) is None:
            textures_array = AssetManager.json_dict['textures']
            for texture in textures_array:
                if texture['name'] == name:
                    main_surface = pygame.image.load(texture['filename'])
                    origin_json = texture['origin']
                    dimension_json = texture['dimensions']
                    origin = (origin_json['x'], origin_json['y'])
                    dimensions = (dimension_json['w'], dimension_json['h'])
                    AssetManager.asset_dictionary[texture_key] = main_surface.subsurface(pygame.Rect(origin, dimensions))
                    return AssetManager.asset_dictionary[texture_key]
        else:
            return AssetManager.asset_dictionary.get(texture_key)
        print "No such texture with name: " + name

    def request_sound(self, name):
        'Get a mixer sound with specified name'
        sound_key = "Sound_" + name
        if AssetManager.asset_dictionary.get(sound_key) is None:
            sound_array = AssetManager.json_dict['sound']
            for sound in sound_array:
                if sound['name'] == name:
                    AssetManager.asset_dictionary[sound_key] = pygame.mixer.Sound(sound['filename'])
                    return AssetManager.asset_dictionary[sound_key]
        else:
            return AssetManager.asset_dictionary.get(sound_key)
        print "No such sound with name: " + name

    def load_song(self, name):
        'Loads song with specified name into pygame.mixer.music, does not start playback'
        song_key = "Song_" + name
        if AssetManager.asset_dictionary.get(song_key) is None:
            song_array = AssetManager.json_dict['song']
            for song in song_array:
                if song['name'] == name:
                    AssetManager.asset_dictionary[song_key] = song['filename']
                    pygame.mixer.music.load(AssetManager.asset_dictionary[song_key])
                    return
        else:
            return
        print "No such song with name: " + name
