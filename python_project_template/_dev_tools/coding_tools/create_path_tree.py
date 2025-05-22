"""Path: _dev_tools/coding_tools/create_path_tree.py."""
import os

# Define folders and files to ignore during tree generation
IGNORE_LIST = ['.git', '__pycache__', '.vscode', '.DS_Store', 'file_path_tree.txt']

def generate_tree(dir_path, prefix=""):
    """
    Recursively generates an ASCII tree structure for a given directory.

    Args:
        dir_path (str): The path to the directory to scan.
        prefix (str): The prefix string for the current level of the tree
                      (e.g., "│   ", "    ").

    Returns:
        list: A list of strings, where each string is a line in the tree.
    """
    tree_lines = []
    # Get all items in the directory, filter out ignored ones
    try:
        items = sorted([item for item in os.listdir(dir_path) if item not in IGNORE_LIST or item == 'file_path_tree.txt'])
    except FileNotFoundError:
        return [f"{prefix}└── [Error: Directory not found: {dir_path}]"]
    except PermissionError:
        return [f"{prefix}└── [Error: Permission denied: {dir_path}]"]


    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = i == (len(items) - 1)

        # Connector for the current item
        connector = "└── " if is_last else "├── "
        tree_lines.append(f"{prefix}{connector}{item}{'/' if os.path.isdir(path) else ''}")

        if os.path.isdir(path):
            # New prefix for items inside this directory
            new_prefix = prefix + ("    " if is_last else "│   ")
            tree_lines.extend(generate_tree(path, new_prefix))
    return tree_lines

def create_path_tree(project_root, output_file):
    """
    Generates and saves the directory tree visualization.

    Args:
        project_root (str): The root directory of the project.
        output_file (str): The file to save the tree to.
    """
    # Start the tree with the project root directory itself
    tree_content = [f"{os.path.basename(os.path.normpath(project_root))}/"] # Show root as dir
    
    # Generate the tree for the contents of the project root
    tree_content.extend(generate_tree(project_root))

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(tree_content))
        print(f"Successfully generated path tree to: {output_file}")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    # Define the project root relative to the script's location or an absolute path
    # For this script, we assume it's in _dev_tools/coding_tools,
    # so project_root is two levels up.
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    project_root_dir = os.path.abspath(os.path.join(current_script_path, "..", "..")) 
    
    # Output file will be in the project root
    output_file_path = os.path.join(project_root_dir, "file_path_tree.txt")

    # Update IGNORE_LIST to exclude the output file itself from the scan initially
    # to prevent it from appearing if it exists from a previous run,
    # but we want it to be listed if it's created by this script.
    # The logic in generate_tree already handles including 'file_path_tree.txt' if present.
    
    create_path_tree(project_root_dir, output_file_path)
