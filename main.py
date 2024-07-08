import datetime
from drupal.overview_analyzer import list_installed_modules, is_directory_valid
from modules.html_generator.html_generator import generate_modules_report
from drupal.config_loader import load_config
from drupal.language_analyzer import list_language_files
from drupal.commerce_analyzer import commerce_analysis_controller
from modules.utils.sorting_utils import sort_data


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
    print("Installed Modules:", installed_modules)

    # Prepare data for HTML table
    installed_modules_data = [(module,) for module in installed_modules]

    # Sort modules data alphabetically, and you can toggle ascending/descending by changing the 'descending' flag
    sorted_modules_data = sort_data(installed_modules_data, column_index=0, descending=False)

    # Generate HTML report
    generate_modules_report(project_name, sorted_modules_data)


    # Language Analysis
    languages_files = list_language_files(languages_directory)
    print("Language files:", languages_files)

    # Commerce Installation Check
    commerce_analysis_controller(config_directory)


if __name__ == "__main__":
    main()
