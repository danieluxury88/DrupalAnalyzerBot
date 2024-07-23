import os
import yaml
from collections import defaultdict
from modules.utils.sorting_utils import sort_list_alphabetically

def print_grouped_files(grouped_files):
    for depth, files in sorted(grouped_files.items()):
        print(f"Depth {depth}:")
        for file in files:
            print(f"  {file}")

# Using the original function without integrated printing
def group_files_by_depth(file_list):
    sorted_files = []
    sorted_files = sorted(file_list)
    file_groups = defaultdict(list)
    for file_name in sorted_files:
        depth = file_name.count('.') - 1
        file_groups[depth].append(file_name)
    return dict(file_groups)

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
    with open(filepath, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {filepath}: {exc}")
            return None


def group_files_by_prefix(file_list):
    file_groups = defaultdict(set)
    for file_name in file_list:
        prefix = file_name.split('.')[0]
        file_groups[prefix].add(file_name)
    return {prefix: list(files) for prefix, files in file_groups.items()}

def categorize_and_sort_commerce_product_files(files):
    file_groups = defaultdict(list)
    for file_name in files:
        parts = file_name.split('.')
        if len(parts) > 1:
            category = parts[1]
            file_groups[category].append(file_name)

    for category in file_groups:
        file_groups[category].sort()

    return dict(file_groups)


def is_commerce_installed(config_directory):
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if 'commerce' in file.lower():
                return True
    return False


def list_starting_with_commerce_config_files(config_directory):
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if file.startswith('commerce'):
                commerce_files.append(file)

    commerce_files = sort_list_alphabetically(commerce_files, descending=False)
    return commerce_files, len(commerce_files)


def list_and_count_commerce_files(config_directory):
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if 'commerce' in file:
                commerce_files.append(file)
    commerce_files = sort_list_alphabetically(commerce_files, descending=False)

    return commerce_files, len(commerce_files)

def print_grouped_files_hierarchically(file_list):
    """
    Print files grouped hierarchically by segments in filenames,
    treating the file extension as part of the last segment.

    Args:
        file_list (list of str): List of filenames to print in a hierarchical structure.
    """
    from collections import defaultdict
    import os

    def recursive_defaultdict():
        return defaultdict(recursive_defaultdict)

    # Create a nested dictionary from filenames
    file_tree = recursive_defaultdict()
    for file in sorted(file_list):
        # Handling the file extension as part of the last segment
        parts = file.rsplit('.', 1)  # Split only once from the right
        subparts = parts[0].split('.')  # Split the first part by dots
        if len(parts) > 1:
            subparts[-1] += '.' + parts[1]  # Append the extension to the last segment

        current_level = file_tree
        for part in subparts:
            current_level = current_level[part]

    # Function to print the nested dictionary with indentation
    def print_tree(tree, indent=""):
        for key, subtree in tree.items():
            print(indent + key)
            if isinstance(subtree, dict):
                print_tree(subtree, indent + "  ")

    # Start printing from the root
    print_tree(file_tree)


def commerce_analysis_controller(config_directory):

    is_commerce = is_commerce_installed(config_directory)
    print("Commerce Installed:", is_commerce)

    # All Commerce related config files
    commerce_files, file_count = list_and_count_commerce_files(
        config_directory)
    print("Commerce-related files found:", file_count)

    grouped_files = group_files_by_depth(commerce_files)
    print_grouped_files(grouped_files)

    print_grouped_files_hierarchically(commerce_files)

    # grouped_files = group_files_by_prefix(commerce_files)
    # for prefix, files in grouped_files.items():
    #     print(f"\nFiles grouped under {prefix} ({len(files)} files):")
    #     for file in files:
    #         print(f"  - {file}")

    # grouped_files = group_files_by_depth(commerce_files)
    # for depth, files in grouped_files.items():
    #   print(f"Depth {depth}: {files}")

    # Only config files starting with commerce
    starting_with_commerce_files, file_count = list_starting_with_commerce_config_files(
        config_directory)
    grouped_files = group_files_by_depth(starting_with_commerce_files)
    print_grouped_files(grouped_files)

    print_grouped_files_hierarchically(starting_with_commerce_files)


    # Commerce Product categorize and sort
    # commerce_product_files = list_starting_with_commerce_config_files(config_directory)  # Filter this list if needed
    # commerce_product_files = [file for file in commerce_product_files if 'commerce_product' in file]

    # commerce_product_files = sort_list_alphabetically(commerce_product_files, descending=False)

    # categorized_sorted_files = categorize_and_sort_commerce_product_files(commerce_product_files)



    # commerce_fields = analyze_commerce_fields(commerce_files)
    # print("Commerce Fields:", commerce_fields)

    # dependencies = analyze_dependencies(commerce_files, config_directory)
    # print("Dependencies:", dependencies)
