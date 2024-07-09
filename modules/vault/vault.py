def analyze_fields(config_directory):
    field_files, count_1 = list_starting_with_module_name_config_files(
        config_directory, "field")
    all_field_files, count_2 = list_and_count_module_files(
        config_directory, "field")

    grouped_files = sort_and_group_by_depth(field_files, 3)
    for group, files in grouped_files.items():
        print(f"Group: {group}")
        for file in files:
            print(f"  - {file}")

def extract_product_variations(file_list):
    variations = set()
    for filename in file_list:
        parts = filename.split('.')
        # Identify the product variation part of the filename based on the expected structure
        if len(parts) > 3 and parts[2] == "commerce_product_variation":
            # parts[3] is expected to be the variation type
            variations.add(parts[3])

    return variations


def analyze_commerce_fields(config_directory, module):
    """
    Analyzes and returns detailed information about commerce product and variation fields.

    Args:
        config_directory (str): Directory containing the configuration files.
        module (str): Specific module part to filter fields, e.g., 'commerce_product'.

    Returns:
        list of dicts: Each dictionary contains 'group' (name), 'number of files', and detailed 'fields'.
    """
    field_files, _ = list_starting_with_module_name_config_files(
        config_directory, "field")
    module_fields = filter_list_by_string(field_files, module)
    grouped_files = sort_and_group_by_depth(module_fields, 3)

    # Filter relevant groups
    relevant_groups = ['field.field.commerce_product', 'field.field.commerce_product_variation']
    group_details = []
    for group, files in grouped_files.items():
        if group in relevant_groups:
            # Extract individual fields from filenames
            # Assume field names are second last in filename
            fields = [file.split('.')[-2] for file in files]
            group_details.append({
                'group': group,
                'number_of_files': len(files),
                'fields': fields
            })

    return group_details
