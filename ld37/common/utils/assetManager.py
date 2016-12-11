import json
import pygame

class AssetManager:
    'Use this to get all of the resources'
    asset_dictionary = {}
    json_dict = {}

    #def __init__(self):

    def request_asset(self, name):
        'Get a texture surface with specified name'
        if AssetManager.asset_dictionary.get(name) is None:
            if len(AssetManager.json_dict) == 0:
                asset_file = open("assets/asset_map.json")
                file_text = asset_file.read()
                AssetManager.json_dict = json.loads(file_text)
            textures_array = AssetManager.json_dict['textures']
            for texture in textures_array:
                if texture['name'] == name:
                    main_surface = pygame.image.load(texture['filename'])
                    origin_json = texture['origin']
                    dimension_json = texture['dimensions']
                    origin = (origin_json['x'], origin_json['y'])
                    dimensions = (dimension_json['w'], dimension_json['h'])
                    AssetManager.asset_dictionary[texture['name']] = main_surface.subsurface(pygame.Rect(origin, dimensions))
                    return AssetManager.asset_dictionary[name]
        else:
            return AssetManager.asset_dictionary.get(name)
        print "No such texture with name: " + name
