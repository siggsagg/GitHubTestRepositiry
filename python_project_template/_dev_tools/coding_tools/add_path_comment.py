"""Path: _dev_tools/coding_tools/add_path_comment.py."""
import os
import sys

PROJECT_ROOT_NAME = "python_project_template"
# Correctly locate the project root based on this script's location
# Script is in _dev_tools/coding_tools, so project root is two levels up.
CURRENT_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_ABS_PATH = os.path.abspath(os.path.join(CURRENT_SCRIPT_DIR, "..", ".."))

# Ensure the determined root path actually ends with PROJECT_ROOT_NAME for safety
if not PROJECT_ROOT_ABS_PATH.endswith(PROJECT_ROOT_NAME):
    print(f"Error: Calculated project root '{PROJECT_ROOT_ABS_PATH}' does not match expected name '{PROJECT_ROOT_NAME}'. Exiting.")
    sys.exit(1)

# _dev_tools should NOT be ignored if we want to process scripts within it.
IGNORE_DIRS_BASENAMES = ['.git', '.vscode', '__pycache__', 'data'] 
IGNORE_FILES_BASENAMES = ['file_path_tree.txt'] # Files to ignore by their base name

def get_relative_path(file_abs_path, root_abs_path):
    """Computes the relative path of a file with respect to the root, using forward slashes."""
    rel_path = os.path.relpath(file_abs_path, root_abs_path)
    return rel_path.replace(os.sep, '/')

def process_python_file(file_abs_path):
    """
    Adds or updates a path comment at the beginning of a Python file.
    """
    try:
        relative_path = get_relative_path(file_abs_path, PROJECT_ROOT_ABS_PATH)
        # Ensure the relative path starts from within the project structure, not from the parent of PROJECT_ROOT_NAME
        # e.g. for /app/python_project_template/src/file.py, relative_path should be src/file.py
        # The PROJECT_ROOT_NAME itself should not be part of the path comment's displayed path.
        
        # If PROJECT_ROOT_ABS_PATH is /app/python_project_template
        # and file_abs_path is /app/python_project_template/src/module.py
        # os.relpath gives "src/module.py" which is correct.

        path_comment_str = f'"""Path: {relative_path}."""'

        with open(file_abs_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines:
            # File is empty, add the path comment
            lines.append(path_comment_str + '\n')
            action_taken = "Added path comment to empty file"
        else:
            first_line_stripped = lines[0].strip()
            
            # Normalize the comment string for comparison by stripping it too
            if first_line_stripped == path_comment_str: # Compare with stripped version
                print(f"Skipped: {relative_path} (already has correct path comment)")
                return

            # Check if the first line is an existing path comment (potentially outdated)
            # It must start with """Path: or '''Path: and end with .""" or .'''
            is_path_comment_line = False
            if first_line_stripped.startswith('"""Path: ') and first_line_stripped.endswith('."""'):
                is_path_comment_line = True
            elif first_line_stripped.startswith("'''Path: ") and first_line_stripped.endswith(".'''"):
                is_path_comment_line = True

            if is_path_comment_line:
                # It is a path comment, but not the correct one (checked above). Replace it.
                lines[0] = path_comment_str + '\n'
                action_taken = f"Updated outdated path comment in {relative_path}"
            # Check if the file starts with any other multiline docstring
            elif first_line_stripped.startswith('"""') or first_line_stripped.startswith("'''"):
                # It's some other docstring, insert path comment before it
                lines.insert(0, path_comment_str + '\n')
                action_taken = f"Added path comment before existing docstring in {relative_path}"
            else:
                # No docstring at all, insert path comment at the beginning
                lines.insert(0, path_comment_str + '\n')
                action_taken = f"Added path comment to {relative_path} (no initial docstring)"
        
        with open(file_abs_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Modified: {action_taken}")

    except Exception as e:
        print(f"Error processing file {file_abs_path}: {e}")


def add_path_comments_to_project():
    """
    Walks through the project directory and processes all .py files.
    """
    print(f"Starting to process Python files in: {PROJECT_ROOT_ABS_PATH}")
    processed_files_count = 0
    for root, dirs, files in os.walk(PROJECT_ROOT_ABS_PATH, topdown=True):
        # Modify dirs in-place to exclude IGNORE_DIRS_BASENAMES
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS_BASENAMES]
        
        for file_name in files:
            if file_name.endswith(".py") and file_name not in IGNORE_FILES_BASENAMES:
                file_abs_path = os.path.join(root, file_name)
                
                # Double check we are not processing files inside ignored parent directories
                # (though os.walk topdown=True with dirs[:] modification should handle it)
                in_ignored_dir = False
                for ignored_dir_basename in IGNORE_DIRS_BASENAMES:
                    if os.path.join(PROJECT_ROOT_ABS_PATH, ignored_dir_basename) in file_abs_path:
                        # Check if the ignored_dir_basename is part of the path.
                        # e.g. if PROJECT_ROOT_ABS_PATH/_dev_tools is an ignored path.
                        # This check ensures that if os.walk still somehow yields something from an ignored dir,
                        # we catch it.
                        # A more precise check would be:
                        # rel_to_root = os.path.relpath(file_abs_path, PROJECT_ROOT_ABS_PATH)
                        # if rel_to_root.startswith(ignored_dir_basename + os.sep):
                        #    in_ignored_dir = True
                        #    break
                        # For simplicity, current IGNORE_DIRS_BASENAMES logic in os.walk is primary.
                        pass # Relying on dirs[:] modification

                if not in_ignored_dir:
                    process_python_file(file_abs_path)
                    processed_files_count += 1
    
    if processed_files_count == 0:
        print("No Python files found to process (or all were ignored/skipped).")
    else:
        print(f"Finished processing. Checked/modified {processed_files_count} Python files.")


if __name__ == "__main__":
    # Make sure PROJECT_ROOT_ABS_PATH is what we expect
    print(f"Identified Project Root: {PROJECT_ROOT_ABS_PATH}")
    if not os.path.isdir(PROJECT_ROOT_ABS_PATH):
        print(f"Error: Project root directory '{PROJECT_ROOT_ABS_PATH}' does not exist. Exiting.")
        sys.exit(1)
    
    # Check if the script itself is inside the project root (it should be)
    if not CURRENT_SCRIPT_DIR.startswith(PROJECT_ROOT_ABS_PATH):
        print(f"Error: This script at '{CURRENT_SCRIPT_DIR}' seems to be outside the identified project root '{PROJECT_ROOT_ABS_PATH}'. Exiting for safety.")
        sys.exit(1)

    add_path_comments_to_project()
    # As a final step, this script should add a path comment to itself.
    print("\nProcessing the script itself to add/update its path comment:")
    process_python_file(os.path.abspath(__file__))
