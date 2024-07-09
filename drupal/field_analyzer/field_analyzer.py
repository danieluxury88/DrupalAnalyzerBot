from drupal.config_files_reader.config_files_reader import list_starting_with_module_name_config_files, list_and_count_module_files, print_grouped_files_hierarchically, sort_and_group_by_depth
from modules.utils.sorting_utils import filter_list_by_string


def analyze_fields_by_module(config_directory, module):
    field_files, count_1 = list_starting_with_module_name_config_files(
        config_directory, "field")
    module_fields = filter_list_by_string(field_files, module)
    grouped_files = sort_and_group_by_depth(module_fields, 4)

    group_details = []
    for group, files in grouped_files.items():
        # Store group and files in a dictionary for each group
        group_details.append({'group': group, 'files': files})

    return group_details


def filter_field_field_elements(groups):
    # Initialize a list to hold the filtered data
    filtered_data = []

    # Iterate over each group
    for group_info in groups:
        # Check if 'field.field' is in the group name
        if 'field.field' in group_info['group']:
            field_data = {
                'group': group_info['group'],
                'files': []
            }
            # Iterate over files and add those that are related to 'field.field'
            for file in group_info['files']:
                if 'field.field' in file:
                    field_data['files'].append(file)
            # Add the filtered group to the list if it has any relevant files
            if field_data['files']:
                filtered_data.append(field_data)

    return filtered_data



def extract_commerce_product_info(field_field_data):
    # Dictionary to hold the commerce products and their field details
    commerce_product_details = {}

    for item in field_field_data:
        # Extracting the product type from the group name
        product_type = item['group'].split('.')[2]

        # Initialize the product type dictionary if not already present
        if product_type not in commerce_product_details:
            commerce_product_details[product_type] = {}

        # Extract fields for the specific product type
        for filename in item['files']:
            # Properly split the filename to extract the subtype and the field name
            parts = filename.split('.')
            subtype = parts[3]  # Extracting the subtype

            # Extract the field name
            field_name = parts[4]

            # Initialize the subtype dictionary if not already present
            if subtype not in commerce_product_details[product_type]:
                commerce_product_details[product_type][subtype] = []

            # Add the field to the subtype list
            if field_name not in commerce_product_details[product_type][subtype]:
                commerce_product_details[product_type][subtype].append(field_name)

    return commerce_product_details


def display_commerce_product_info(commerce_product_details, specific_product_type=None, specific_subtype=None):
    for product_type, subtypes in commerce_product_details.items():
        if specific_product_type and specific_product_type != product_type:
            continue

        for subtype, fields in subtypes.items():
            # If a specific subtype is provided and does not match the current subtype, skip
            if specific_subtype and specific_subtype != subtype:
                continue

            print(f"Product Type: {product_type}")
            print(f"  Subtype: {subtype}")
            print("    Fields:")
            for field in fields:
                print(f"      - {field}")
            print("\n")


def fields_analysis_controller(config_directory):
    groups = analyze_fields_by_module(config_directory, "commerce")
    field_field_data = filter_field_field_elements(groups)

    print(field_field_data)

    commerce_product_info = extract_commerce_product_info(field_field_data)
    display_commerce_product_info(commerce_product_info, specific_subtype="drawer_slide_system")
    return
