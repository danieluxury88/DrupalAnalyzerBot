import os

def list_language_files(config_directory, languages_folder):
    """List all files in the languages directory."""
    language_dir = os.path.join(config_directory, languages_folder)
    return [f for f in os.listdir(language_dir) if os.path.isfile(os.path.join(language_dir, f))]
