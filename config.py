import json


def get_config_value(setting):
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config[setting]
    
    
def get_config_json():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config


def update_config(conf):
    with open('config.json', 'w') as config_file:
        json.dump(conf, config_file)