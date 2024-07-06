import os

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


def generate_modules_report(project_name, modules_list):
    # Create the "out" folder if it doesn't exist
    os.makedirs("out", exist_ok=True)  # Using os.makedirs with exist_ok=True

    html_content = create_basic_html("Installed Modules Report")
    html_content += add_table_to_html(modules_list, ["Module Name"])
    html_content = finalize_html(html_content)
    with open(f"out/{project_name}.html", "w") as file:
        file.write(html_content)
