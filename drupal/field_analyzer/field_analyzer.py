import os
import yaml
from drupal.config_files_reader.config_files_reader import list_starting_with_module_name_config_files, list_and_count_module_files, print_grouped_files_hierarchically, sort_and_group_by_depth
from modules.utils.sorting_utils import filter_list_by_string
from drupal.config_loader import load_config_keys


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
                commerce_product_details[product_type][subtype].append(
                    field_name)

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


def get_field_type(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data.get('field_type', 'unknown')


def generate_cli_report(product_data):
    print("Generate REPORT 1- CLI")
    report = ""
    for product_type, fields in product_data.items():
        report += f"Product Type: {product_type}\n"
        for field_name, field_type in fields:
            report += f"  - {field_name} : {field_type}\n"
        report += "\n"
    return report


def generate_uml_report(product_data):
    report = ""
    for product_type, fields in product_data.items():
        report += f"class {product_type} {{\n"
        for field_name, field_type in fields:
            report += f"  - {field_name} : {field_type}\n"
        report += "}\n"
    return report


def extract_data(groups, config_directory):
    product_data = {}
    for group in groups:
        product_subtype = group['group'].split('.')[-2]
        product_type = group['group'].split('.')[-1]
        fields = []
        for file_name in group['files']:
            file_path = os.path.join(config_directory, file_name)
            field_type = get_field_type(file_path)
            field_name = file_name.split('.')[-2]
            fields.append((field_name, field_type))
        product_data[f"{product_subtype}_{product_type}"] = fields
    return product_data


def sort_by_field_name(product_data):
    sorted_data = {}
    for product_type, fields in product_data.items():
        # Sorting the tuple list by the first element (field_name) in each tuple
        sorted_fields = sorted(fields, key=lambda x: x[0])
        sorted_data[product_type] = sorted_fields
    return sorted_data


def sort_by_field_type(product_data):
    sorted_data = {}
    for product_type, fields in product_data.items():
        # Sorting the tuple list by the second element (field_type) in each tuple
        sorted_fields = sorted(fields, key=lambda x: x[1])
        sorted_data[product_type] = sorted_fields
    return sorted_data


def obtain_product_differences(product_data, product_name1, product_name2):
    # Extract the field lists for both specified products
    fields_product1 = set(product_data[product_name1])
    fields_product2 = set(product_data[product_name2])

    # Find common fields (intersection of sets)
    common_fields = fields_product1 & fields_product2
    # Find fields unique to the first product (difference of sets)
    product1_unique = fields_product1 - fields_product2
    # Find fields unique to the second product
    product2_unique = fields_product2 - fields_product1

    return common_fields, product1_unique, product2_unique


def format_as_uml_class(name, fields):
    report = f"class {name} {{\n"

    # Iterate over the set of fields, each a tuple of (field_name, field_type)
    for field_name, field_type in fields:
        # Append each field as a class attribute in UML format
        report += f"  - {field_name} : {field_type}\n"

    # Close the class definition
    report += "}\n"
    return report


def print_product_differences(product_data, product_name1, product_name2):
    # Use the function to analyze the fields
    common, product1_unique, product2_unique = obtain_product_differences(
        product_data, product_name1, product_name2)

    report1 = format_as_uml_class(
        f"common_between_{product_name1}_and_{product_name2}", common)
    report2 = format_as_uml_class(
        f"unique_on_{product_name1}", product1_unique)
    report3 = format_as_uml_class(
        f"unique_on_{product_name2}", product2_unique)

    # print(f"----Common between {product_name1} and {product_name2}----")
    # print(report1)

    # print(f"Unique on  {product_name1}")
    # print(report2)

    # print(f"Unique on  {product_name2}")
    # print(report3)

    report_diff = f"{report1}\n{report2}\n{report3}"
    return report_diff

    # print(f"Product Data: {product_data} / {type(product_data)}")
    # print(f"Common: {common} / {type(common)}")
    # print(f"Product 1 Unique: {product1_unique} / {type(product1_unique)}")
    # print(f"Product 2 Unique: {product2_unique} / {type(product2_unique)}")

    # print("Common fields:")
    # for field in common:
    #     print(field)

    # print("\nUnique to " + product_name1 + ":")
    # for field in product1_unique:
    #     print(field)

    # print("\nUnique to " + product_name2 + ":")
    # for field in product2_unique:
    #     print(field)


def save_uml_report(report, filename):
    config = load_config_keys()
    uml_report_output = config.get('uml_report_output') if config else None
    print(uml_report_output)  # Debug print to verify the path
    if uml_report_output is None:
        raise ValueError("UML report output path is not configured")

    # Construct the full path to where the report will be saved
    output_file_path = os.path.join(uml_report_output, filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    # Open the file at the full path to write the UML report content
    with open(output_file_path, 'w') as file:
        file.write(report)


def create_configuration_comparisson_report(product_data):
    # Names of the products to compare
    product_name1 = 'commerce_product_accessory'
    product_name2 = 'commerce_product_drawer_slide_system'
    report_diff = print_product_differences(
        product_data, product_name1, product_name2)
    save_uml_report(report_diff, 'out/report_products_diff.puml')
    # print("Product configuration insights")
    # print(report_diff)

    product_name1 = 'commerce_product_variation_accessory'
    product_name2 = 'commerce_product_variation_drawer_slide_system'
    report_diff = print_product_differences(
        product_data, product_name1, product_name2)
    save_uml_report(report_diff, 'out/report_variations_diff.puml')
    # print("Product variation configuration insights")
    # print(report_diff)


def create_current_configuration_report(product_data):
    product_data_by_name = sort_by_field_name(product_data)
    report = generate_uml_report(product_data_by_name)
    save_uml_report(report, 'out/report_by_name.puml')

    # print(f"Sorted by name : \n{product_data_by_name} {type(product_data_by_name)}")
    product_data_by_type = sort_by_field_type(product_data)
    report = generate_uml_report(product_data_by_type)
    save_uml_report(report, 'out/report_by_type.puml')
    # print(f"Sorted by type : \n{product_data_by_type} {type(product_data_by_type)}")


def fields_analysis_controller(config_directory):
    groups = analyze_fields_by_module(config_directory, "commerce")
    field_field_data = filter_field_field_elements(groups)
    # print(field_field_data)

    # commerce_product_info = extract_commerce_product_info(field_field_data)
    # display_commerce_product_info(
    #     commerce_product_info, specific_subtype="drawer_slide_system")

    product_data = extract_data(field_field_data, config_directory)
    # print("CLI REPORT - BASIC")
    # report = generate_cli_report(product_data)
    # print(report)

    print("Generate REPORT - CONFIGURATION")
    create_current_configuration_report(product_data)

    print("Generate REPORT - DIFFERENCES")
    create_configuration_comparisson_report(product_data)

    return
