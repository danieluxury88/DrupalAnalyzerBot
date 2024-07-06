import yaml

def load_config(config_file):
    """ Load configuration from a YAML file. """
    with open(config_file, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error loading configuration file {config_file}: {exc}")
            return None
