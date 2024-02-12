import json

def read_config(config_path):
    """Read configuration from a JSON file."""
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config