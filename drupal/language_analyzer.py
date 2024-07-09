import os

def list_language_directories(languages_dir):
    """List all language directories in the specified directory."""
    return [d for d in os.listdir(languages_dir) if os.path.isdir(os.path.join(languages_dir, d))]


def list_language_files(languages_dir):
    """List all files in the languages directory."""
    return [f for f in os.listdir(languages_dir) if os.path.isfile(os.path.join(languages_dir, f))]
