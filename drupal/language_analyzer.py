import os

def list_language_files(languages_dir):
    """List all files in the languages directory."""
    return [f for f in os.listdir(languages_dir) if os.path.isfile(os.path.join(languages_dir, f))]
