# Import the required libraries
import os

def create_initial_md_file(file_path = '''./Logs/md_logs.md''', overwrite = False):
    # Set the file path and name
    file_path = file_path

    # Define the markdown content
    markdown_content = """
    # ChatGPT log file
    """

    if os.path.exists(file_path) and overwrite == False:
        print(f"There already is a markdown file in {file_path}")
        return 1

    # Write the content to the file
    with open(file_path, "w") as file:
        file.write(markdown_content)

    # Confirm that the file has been created
    if os.path.exists(file_path):
        print(f"Markdown file created successfully at {file_path}")
        return 1
    else:
        print("Failed to create markdown file.")
        return 0
    
def write_to_md_file(content, file_path = '''./Logs/md_logs.md'''):

    new_markdown_content = str(content)

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write(new_markdown_content)

create_initial_md_file(overwrite = True)