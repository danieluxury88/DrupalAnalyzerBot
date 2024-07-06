import os

def is_commerce_installed(config_directory):
    """Check if there are configuration files indicating Drupal Commerce is installed."""
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if 'commerce' in file.lower():
                return True
    return False
