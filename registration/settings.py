import yaml

config_path = '/var/config/registration.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
