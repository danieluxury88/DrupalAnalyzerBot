import os
from collections import defaultdict
from modules.utils.sorting_utils import sort_list_alphabetically


def parse_yaml_file(filepath):
    """ Parse a YAML file and return its content. """
    import yaml
    with open(filepath, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {filepath}: {exc}")
            return None


def is_commerce_installed(config_directory):
    """Check if there are configuration files indicating Drupal Commerce is installed."""
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if 'commerce' in file.lower():
                return True
    return False


def list_starting_with_commerce_config_files(config_directory):
    """List file names of Drupal Commerce-related configuration files in the specified directory."""
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if file.startswith('commerce'):
                commerce_files.append(file)  # Only add the file name
    return commerce_files


def group_files_by_prefix(file_list):
    """Group files by their prefixes, determined by the substring before the first period,
    ensuring that each group only contains unique file names.

    Args:
        file_list (list of str): List of filenames to group.

    Returns:
        dict: Dictionary of files grouped by their prefixes with unique entries.
    """
    file_groups = defaultdict(set)  # Use set instead of list to avoid duplicates
    for file_name in file_list:
        prefix = file_name.split('.')[0]  # Get the prefix before the first period
        file_groups[prefix].add(file_name)  # Add to set, automatically handling duplicates
    return {prefix: list(files) for prefix, files in file_groups.items()}  # Convert set to list for usability


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


def list_and_count_commerce_files(config_directory):
    """List all files containing 'commerce' in their names and count them.

    Args:
        config_directory (str): The directory to search for files.

    Returns:
        tuple: A list of filenames containing 'commerce', and the count of such files.
    """
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if 'commerce' in file:
                commerce_files.append(file)

    return commerce_files, len(commerce_files)


def generate_reports(commerce_files):
    """Generate reports from the analyzed Commerce data."""
    # Example stub, this needs more specific implementation details
    print("Generating reports...")
    # Implement report generation logic here

def categorize_and_sort_commerce_product_files(files):
    """
    Categorize and sort commerce_product files by the second segment of their filenames.

    Args:
        files (list of str): List of filenames starting with 'commerce_product'.

    Returns:
        dict: Dictionary where keys are categories derived from the second segment and values are sorted lists of filenames.
    """
    file_groups = defaultdict(list)
    for file_name in files:
        parts = file_name.split('.')
        if len(parts) > 1:
            category = parts[1]  # Extract the second segment
            file_groups[category].append(file_name)

    # Sort files in each category
    for category in file_groups:
        file_groups[category].sort()

    return dict(file_groups)

def commerce_analysis_controller(config_directory):

    is_commerce = is_commerce_installed(config_directory)
    print("Commerce Installed:", is_commerce)

    # All Commerce related config files
    commerce_files, file_count = list_and_count_commerce_files(
        config_directory)
    print("Commerce-related files found:", file_count)

    commerce_files = sort_list_alphabetically(commerce_files, descending=False)

    grouped_files = group_files_by_prefix(commerce_files)
    for prefix, files in grouped_files.items():
        print(f"\nFiles grouped under {prefix} ({len(files)} files):")
        for file in files:
            print(f"  - {file}")


    # Only config files starting with commerce
    starting_with_commerce_files = list_starting_with_commerce_config_files(
        config_directory)
    print("Commerce Configuration Files:", starting_with_commerce_files)

    starting_with_commerce_files = sort_list_alphabetically(starting_with_commerce_files, descending=False)

    grouped_files = group_files_by_prefix(starting_with_commerce_files)
    for prefix, files in grouped_files.items():
        print(f"\nFiles grouped under {prefix} ({len(files)} files):")
        for file in files:
            print(f"  - {file}")


    # Commerce Product categorize and sort
    commerce_product_files = list_starting_with_commerce_config_files(config_directory)  # Filter this list if needed
    commerce_product_files = [file for file in commerce_product_files if 'commerce_product' in file]

    commerce_product_files = sort_list_alphabetically(commerce_product_files, descending=False)

    categorized_sorted_files = categorize_and_sort_commerce_product_files(commerce_product_files)

    # Print the categorized and sorted files
    for category, files in categorized_sorted_files.items():
        print(f"\nCategory: {category} ({len(files)} files)")
        for file in files:
            print(f"  - {file}")


    commerce_fields = analyze_commerce_fields(commerce_files)
    print("Commerce Fields:", commerce_fields)

    dependencies = analyze_dependencies(commerce_files, config_directory)
    print("Dependencies:", dependencies)

# Example usage in another script or module
if __name__ == "__main__":
    config_directory = '/path/to/your/drupal/config/directory'
    commerce_analysis_controller(config_directory)
