from modules.html_generator import generate_modules_report
from drupal.config_loader import load_config
from drupal.language_analyzer import list_language_files
from drupal.commerce_analyzer import is_commerce_installed
from drupal.overview_analyzer import list_installed_modules
from modules.sorting_utils import sort_data




def main():
    config = load_config('config.yaml')
    if not config:
        print("Failed to load configuration.")
        return

    config_directory = config['config_directory']
    languages_folder = config['languages_folder']
    project_name = config['project_name']

    # Language Analysis
    # languages_files = list_language_files(config_directory, languages_folder)
    # print("Language files:", languages_files)

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
