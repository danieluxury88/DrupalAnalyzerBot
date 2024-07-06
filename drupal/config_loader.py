import yaml

def load_config(config_file, project_name=None):
    """ Load configuration from a YAML file for a specific project and return the detailed settings.

    Args:
        config_file (str): Path to the configuration YAML file.
        project_name (str): Optionally specify a project name to override the default in the config.

    Returns:
        dict: Complete project configuration with necessary settings if successful, otherwise None.
    """
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            if project_name is None:
                project_name = config['current_project']
            project_config = config['projects'].get(project_name)
            if not project_config:
                print("Project configuration not found.")
                return None

            # Add the project name to the configuration for reference
            project_config['project_name'] = project_name
            return project_config
    except yaml.YAMLError as exc:
        print(f"Error loading configuration file {config_file}: {exc}")
        return None
    except FileNotFoundError:
        print(f"Configuration file not found: {config_file}")
        return None

# Example usage within this script for testing or initialization (remove if not needed)
if __name__ == "__main__":
    config = load_config('drupal/config.yaml', project_name='vpack')
    if config:
        print("Configuration loaded successfully:", config)
    else:
        print("Failed to load configuration.")
