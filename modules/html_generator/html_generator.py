
import os
import webbrowser
from jinja2 import Environment, FileSystemLoader

def create_basic_html(title):
    """Create a basic HTML5 document."""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        table, th, td {{
            border: 1px solid black;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 8px;
            text-align: left;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
"""
    return html_content

def add_table_to_html(data, column_headers):
    """Add a table to an existing HTML document based on provided data."""
    table_html = "<table>\n<tr>"
    for header in column_headers:
        table_html += f"<th>{header}</th>"
    table_html += "</tr>\n"

    for row in data:
        table_html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>\n"
    table_html += "</table>\n"
    return table_html

def finalize_html(html_content):
    """Finalize the HTML document."""
    return html_content + "</body>\n</html>"


# def generate_modules_report(project_name, modules_list):
#     import os
#     import webbrowser  # Ensure this import is at the top of your script if not already

#     # Create the "out" folder if it doesn't exist
#     os.makedirs("out", exist_ok=True)

#     html_content = create_basic_html("Installed Modules Report")
#     html_content += add_table_to_html(modules_list, ["Module Name"])
#     html_content = finalize_html(html_content)
#     file_path = f"out/{project_name}.html"
#     with open(file_path, "w") as file:
#         file.write(html_content)


def generate_modules_report(project_name, modules_list):
    # Base directory for the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'templates')

    # Configure Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_dir))

    template = env.get_template('report_template.html')

    # Create the "out" folder if it doesn't exist within the html_generator directory
    output_dir = os.path.join(base_dir, 'out')
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, f"{project_name}.html")
    with open(file_path, "w") as file:
        html_content = template.render(
            title="Installed Modules Report",
            modules=modules_list,
            project_name=project_name  # Pass the project name here
        )
        file.write(html_content)

    print(f"Report generated: {file_path}")

    # Open the HTML file in a web browser
    webbrowser.open_new_tab(f'file://{os.path.realpath(file_path)}')

