# Python Project Template

A flexible and comprehensive template for starting new Python projects. It provides a well-defined directory structure, essential development tools, and configurations to ensure consistency and efficiency.

## Features

*   Standardized project structure.
*   Integrated development tools for code management and documentation.
*   Example configurations for environment variables and Git ignore.
*   Setup for linting and formatting with Ruff.

## Setup Instructions

Follow these steps to use this template for your new project:

1.  **Create a New Project from Template**:
    *   Copy the entire `python_project_template/` directory to a new location and rename it to your project's name.
    ```bash
    cp -R python_project_template/ my_new_project/
    cd my_new_project/
    ```

2.  **Set Up a Virtual Environment**:
    *   It's highly recommended to use a virtual environment for managing project dependencies.
    ```bash
    python3 -m venv venv 
    ```
    *   Activate the virtual environment:
        *   On macOS and Linux:
            ```bash
            source venv/bin/activate
            ```
        *   On Windows:
            ```bash
            .\venv\Scripts\activate
            ```

3.  **Install Dependencies**:
    *   This template doesn't come with a `requirements.txt` by default, as it's a base template. You should create one as you add dependencies.
    *   If you have a `requirements.txt` (or will create one):
    ```bash
    pip install -r requirements.txt 
    ```
    *   (Initially, you might just install specific packages you need, e.g., `pip install flask`)

4.  **Set Up Environment Variables**:
    *   Copy the example environment file `.env-example` to `.env`. This file will be ignored by Git and should contain your project-specific configurations and secrets.
    ```bash
    cp .env-example .env
    ```
    *   Open `.env` and fill in the necessary values (e.g., API keys, database credentials, `SECRET_KEY`).

## Development Tools

This template includes several utility scripts located in the `_dev_tools/coding_tools/` directory to aid in development.

1.  **`create_path_tree.py`**:
    *   **Purpose**: Generates an ASCII representation of the project's directory structure.
    *   **How to Run**:
        ```bash
        python3 _dev_tools/coding_tools/create_path_tree.py
        ```
    *   **Output**: This script creates/updates the `file_path_tree.txt` file in the project root. This file is useful for documentation and getting an overview of the project layout.

2.  **`add_path_comment.py`**:
    *   **Purpose**: Automatically adds or updates a path comment (e.g., `"""Path: src/module/file.py."""`) at the beginning of every Python (`.py`) file within the project. This helps in quickly identifying the location of a file within the project structure.
    *   **How to Run**:
        ```bash
        python3 _dev_tools/coding_tools/add_path_comment.py
        ```
    *   **Note**: This script modifies Python files in place.

3.  **`concat_files.py`**:
    *   **Purpose**: Concatenates all Python files from specified directories (currently `src/` and `utils/`) into a single file. It also prepends the project's file tree (from `file_path_tree.txt`) to this concatenated file. This can be useful for creating a single-file submission or for certain analysis tasks.
    *   **How to Run**:
        ```bash
        python3 _dev_tools/coding_tools/concat_files.py
        ```
    *   **Output**: This script creates/updates the `concatenated_code.py` file in the project root.
    *   **Note**: This script will first call `create_path_tree.py` to ensure the file tree is up-to-date.

## Project Structure

The template uses the following directory structure:

*   **`.vscode/`**: Contains VS Code specific settings, including recommendations for extensions and formatter settings (e.g., for Ruff).
*   **`_dev_tools/`**: Houses scripts and tools for development assistance.
    *   **`coding_tools/`**: Contains Python scripts for code management, documentation, etc.
*   **`_project_plan/`**: Intended for project planning documents, roadmaps, and related materials. (Currently empty)
*   **`data/`**: For storing data files.
    *   **`logs/`**: For application logs. `.gitignore` is configured to ignore all logs except `data/logs/log.txt`.
*   **`src/`**: Main source code for your application. (Create your `main.py` or primary application modules here)
*   **`tests/`**: Contains unit tests, integration tests, etc. (Currently empty)
*   **`utils/`**: For utility scripts or modules that can be used across the project. (Currently empty)
*   **`.env-example`**: Example environment variable file.
*   **`.gitignore`**: Specifies intentionally untracked files that Git should ignore.
*   **`concatenated_code.py`**: (Generated) Combined code from `src/` and `utils/`. Ignored by Git.
*   **`file_path_tree.txt`**: (Generated) Text representation of the project structure. Ignored by Git.
*   **`README.md`**: This file.

## Running the Application

*   (This section should be updated based on your project)
*   If your main script is, for example, `src/main.py`, you would typically run it using:
    ```bash
    python3 src/main.py
    ```

## Linting and Formatting

*   This template is set up to use **Ruff** for fast linting and formatting.
*   If you use VS Code, the recommended Python extension will typically pick up Ruff if it's installed in your environment.
*   You can also run Ruff manually from the command line (after installing it: `pip install ruff`):
    ```bash
    ruff check .  # For linting
    ruff format . # For formatting
    ```
*   Configuration for Ruff can be added to `pyproject.toml` or `.ruff.toml` as your project grows. The `.vscode/settings.json` might contain initial settings to integrate Ruff with the editor.

## Contributing

*   (Placeholder for contribution guidelines)
*   If this were an open-source project, this section would detail how others can contribute, coding standards, pull request processes, etc.

---

Happy Coding!
