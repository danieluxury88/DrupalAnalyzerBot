import datetime
from drupal.overview_analyzer import list_installed_modules, is_directory_valid
from modules.html_generator.html_generator import generate_modules_report
from modules.utils.sorting_utils import sort_data
from drupal.config_loader import load_config
from drupal.language_analyzer import list_language_directories
from drupal.commerce_analyzer import commerce_analysis_controller
from drupal.field_analyzer.field_analyzer import fields_analysis_controller


def main():
    config = load_config('drupal/config.yaml')
    if not config:
        return

    # Use the loaded configuration
    print("Current Time", datetime.datetime.now())
    print("Project Name:", config['project_name'])
    print("Configuration Directory:", config['config_directory'])
    print("Languages Directory:", config['languages_directory'])

    project_name = config['project_name']
    config_directory = config['config_directory']
    languages_directory = config['languages_directory']

    if not is_directory_valid(config_directory):
        print("Project not found")
        return

    # Overview of Installed Modules
    installed_modules = list_installed_modules(config_directory)
    installed_modules_data = [module for module in installed_modules]
    sorted_modules = sort_data(installed_modules_data, column_index=0, descending=False)
    # print("Sorted installed Modules:", sorted_modules)

    # # Language Analysis
    languages_files = list_language_directories(languages_directory)
    # print("Language files:", languages_files)

    # Generate HTML report
    generate_modules_report(project_name, [languages_files, sorted_modules, installed_modules])



    # # Commerce Installation Check
    # commerce_analysis_controller(config_directory)
    fields_analysis_controller(config_directory)


if __name__ == "__main__":
    main()
