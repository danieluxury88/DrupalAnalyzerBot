from modules.html_generator import generate_modules_report
from drupal.config_loader import load_config
from drupal.language_analyzer import list_language_files
from drupal.commerce_analyzer import is_commerce_installed
from drupal.overview_analyzer import list_installed_modules
from modules.sorting_utils import sort_data




def main():
    config = load_config('drupal/config.yaml')
    if not config:
        return

    # Use the loaded configuration
    print("Project Name:", config['project_name'])
    print("Configuration Directory:", config['config_directory'])
    print("Languages Directory:", config['languages_directory'])

    project_name = config['project_name']
    config_directory = config['config_directory']
    languages_directory = config['languages_directory']


    # Language Analysis
    languages_files = list_language_files(languages_directory)
    print("Language files:", languages_files)

    # Commerce Installation Check
    commerce_installed = is_commerce_installed(config_directory)
    print("Commerce Installed:", commerce_installed)

    # Overview of Installed Modules
    installed_modules = list_installed_modules(config_directory)
    print("Installed Modules:", installed_modules)

    # Prepare data for HTML table
    installed_modules_data = [(module,) for module in installed_modules]

    # Sort modules data alphabetically, and you can toggle ascending/descending by changing the 'descending' flag
    sorted_modules_data = sort_data(installed_modules_data, column_index=0, descending=False)

    # Generate HTML report
    generate_modules_report(project_name, sorted_modules_data)


if __name__ == "__main__":
    main()
