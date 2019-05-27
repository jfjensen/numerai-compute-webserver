import json

config_file = "config.json"

def load_config():

    config = None
    with open(config_file, "r") as read_file:
        config = json.load(read_file)

    return config

def save_config(config):

    with open(config_file, "w") as write_file:
        json.dump(config, write_file)