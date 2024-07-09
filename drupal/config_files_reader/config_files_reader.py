import os
from modules.utils.sorting_utils import sort_list_alphabetically, filter_list_by_string
from collections import defaultdict


def list_starting_with_module_name_config_files(config_directory, module):
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if file.startswith(module):
                commerce_files.append(file)

    commerce_files = sort_list_alphabetically(commerce_files, descending=False)
    return commerce_files, len(commerce_files)


def list_and_count_module_files(config_directory, module):
    commerce_files = []
    for root, dirs, files in os.walk(config_directory):
        for file in files:
            if module in file:
                commerce_files.append(file)
    commerce_files = sort_list_alphabetically(commerce_files, descending=False)
    return commerce_files, len(commerce_files)

def print_grouped_files_hierarchically(file_list):
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

def group_files_by_prefix(file_list):
    file_groups = defaultdict(set)
    for file_name in file_list:
        prefix = file_name.split('.')[0]
        file_groups[prefix].add(file_name)
    return {prefix: list(files) for prefix, files in file_groups.items()}


def sort_and_group_by_depth(file_list, group_depth):
    """
    Sorts the file names based on their depth, groups them by a specified depth level, and ensures no duplicates.
    Groups are sorted so that those with fewer segments appear first.

    Args:
        file_list (list of str): The list of filenames.
        group_depth (int): The depth level at which to group the filenames.

    Returns:
        dict: A dictionary where keys are the group names and values are lists of filenames, with no duplicates.
    """

    # Remove duplicates in the input list to ensure they don't affect grouping
    unique_files = list(set(file_list))

    # Parsing each filename and storing in a dictionary based on their depth
    depth_dict = defaultdict(list)
    for filename in unique_files:
        depth = filename.count('.')  # depth based on the number of dots
        depth_dict[depth].append(filename)

    # Sorting files within each depth
    for depth in depth_dict:
        depth_dict[depth].sort(key=lambda x: x.split('.'))

    # Grouping by specified depth level
    grouped_files = defaultdict(list)
    for files in depth_dict.values():
        for file in files:
            # Split the filename and create a group key based on the specified depth level
            parts = file.split('.')
            group_key = '.'.join(parts[:group_depth]) if len(parts) > group_depth else '.'.join(parts)
            if file not in grouped_files[group_key]:  # Check to avoid duplicates in the same group
                grouped_files[group_key].append(file)

    # Sorting groups by number of segments (fewer segments come first)
    sorted_grouped_files = {k: sorted(v) for k, v in sorted(grouped_files.items(), key=lambda x: (x[0].count('.'), x))}
    return sorted_grouped_files
