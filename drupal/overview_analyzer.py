import os

def list_installed_modules(config_directory):
    """List all unique modules based on the presence of configuration files."""
    modules = set()
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if file.endswith('.yml'):
                module_name = file.split('.')[0]
                modules.add(module_name)
    return modules
