import os
from collections import defaultdict


def is_commerce_installed(config_directory):
    """Check if there are configuration files indicating Drupal Commerce is installed."""
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if 'commerce' in file.lower():
                return True
    return False


def list_commerce_config_files(config_directory):
    """List file names of Drupal Commerce-related configuration files in the specified directory."""
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if file.startswith('commerce'):
                commerce_files.append(file)  # Only add the file name
    return commerce_files


def group_files_by_prefix(file_list):
    """Group files by their prefixes, determined by the substring before the first period."""
    file_groups = defaultdict(list)
    for file_name in file_list:
        # Get the prefix before the first period
        prefix = file_name.split('.')[0]
        file_groups[prefix].append(file_name)
    return dict(file_groups)  # Convert defaultdict to dict for general use


def list_commerce_related_files(config_directory):
    """List all files related to Drupal Commerce in the specified directory."""
    commerce_files = []
    keywords = ["commerce", "core.base_field_override.commerce", "core.entity_form_display.commerce",
                "core.entity_view_display.commerce", "field.field.commerce", "field.storage.commerce",
                "system.action.commerce", "views.view.commerce"]
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if any(keyword in file for keyword in keywords):
                commerce_files.append(file)
    return commerce_files


def analyze_dependencies(commerce_files, config_directory):
    """Analyze dependencies based on configuration file content."""
    dependencies = {}
    for file_name in commerce_files:
        file_path = os.path.join(config_directory, file_name)
        content = parse_yaml_file(file_path)
        # Extract relevant dependency information from content
        # This will depend on the actual content structure of the files
    return dependencies


def analyze_commerce_fields(commerce_files):
    """Analyze and categorize fields defined in Commerce configuration files."""
    fields = {}
    for file_name in commerce_files:
        if "field.field.commerce" in file_name:
            # Assumes file naming convention is consistent
            entity = file_name.split('.')[2]
            if entity not in fields:
                fields[entity] = []
            fields[entity].append(file_name)
    return fields


def parse_yaml_file(filepath):
    """ Parse a YAML file and return its content. """
    import yaml
    with open(filepath, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {filepath}: {exc}")
            return None


def list_commerce_related_files(config_directory):
    """List all files related to Drupal Commerce in the specified directory."""
    commerce_files = []
    keywords = ["commerce", "core.base_field_override.commerce", "core.entity_form_display.commerce",
                "core.entity_view_display.commerce", "field.field.commerce", "field.storage.commerce",
                "system.action.commerce", "views.view.commerce"]
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if any(keyword in file for keyword in keywords):
                commerce_files.append(file)
    return commerce_files


def analyze_dependencies(commerce_files, config_directory):
    """Analyze dependencies based on configuration file content."""
    dependencies = {}
    for file_name in commerce_files:
        file_path = os.path.join(config_directory, file_name)
        content = parse_yaml_file(file_path)
        # Extract relevant dependency information from content
        # This will depend on the actual content structure of the files
    return dependencies


def analyze_commerce_fields(commerce_files):
    """Analyze and categorize fields defined in Commerce configuration files."""
    fields = {}
    for file_name in commerce_files:
        if "field.field.commerce" in file_name:
            # Assumes file naming convention is consistent
            entity = file_name.split('.')[2]
            if entity not in fields:
                fields[entity] = []
            fields[entity].append(file_name)
    return fields


def generate_reports(commerce_files):
    """Generate reports from the analyzed Commerce data."""
    # Example stub, this needs more specific implementation details
    print("Generating reports...")
    # Implement report generation logic here


def commerce_analysis_controller(config_directory):
    """Controller function that orchestrates the analysis of Drupal Commerce configurations."""
    commerce_files = list_commerce_related_files(config_directory)
    commerce_fields = analyze_commerce_fields(commerce_files)
    dependencies = analyze_dependencies(commerce_files, config_directory)

    print("Commerce Files:", commerce_files)
    print("Commerce Fields:", commerce_fields)
    print("Dependencies:", dependencies)

    generate_reports(commerce_files)


# Example usage in another script or module
if __name__ == "__main__":
    config_directory = '/path/to/your/drupal/config/directory'
    commerce_analysis_controller(config_directory)
