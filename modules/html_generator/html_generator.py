import os
import webbrowser
from jinja2 import Environment, FileSystemLoader

def generate_modules_report(project_name, tables_data):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('report_template.html')

    output_dir = os.path.join(base_dir, 'out')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{project_name}.html")

    with open(file_path, "w") as file:
        html_content = template.render(
            title="Installed Modules Report",
            project_name=project_name,
            tables=tables_data
        )
        file.write(html_content)

    print(f"Report generated: {file_path}")
    webbrowser.open_new_tab(f'file://{os.path.realpath(file_path)}')

