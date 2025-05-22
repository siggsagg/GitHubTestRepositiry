# Makefile for python_project_template

# Define phony targets (targets that are commands, not files)
.PHONY: help setup tree add-paths concat lint format all-dev-tools run

# Default target executed when 'make' is run without arguments
.DEFAULT_GOAL := help

# Variables for paths and commands
PYTHON_INTERPRETER := python3
DEV_TOOLS_DIR := _dev_tools/coding_tools
REQUIREMENTS_FILE := requirements.txt
MAIN_APP_SCRIPT := src/main.py

# Ruff commands
RUFF := ruff

help:
	@echo "Available commands for MyProject:"
	@echo ""
	@echo "  setup          - Install project dependencies from $(REQUIREMENTS_FILE)"
	@echo "  tree           - Generate file_path_tree.txt using $(DEV_TOOLS_DIR)/create_path_tree.py"
	@echo "  add-paths      - Add path comments to Python files using $(DEV_TOOLS_DIR)/add_path_comment.py"
	@echo "  concat         - Concatenate Python files into concatenated_code.py using $(DEV_TOOLS_DIR)/concat_files.py"
	@echo "  lint           - Lint the project using $(RUFF) check ."
	@echo "  format         - Format the project using $(RUFF) format ."
	@echo "  all-dev-tools  - Run all development tools (tree, add-paths, concat)"
	@echo "  run            - Run the main application ($(MAIN_APP_SCRIPT))"
	@echo ""
	@echo "Usage: make [target]"
	@echo "Example: make setup"

setup:
	@echo "Installing project dependencies from $(REQUIREMENTS_FILE)..."
	$(PYTHON_INTERPRETER) -m pip install -r $(REQUIREMENTS_FILE)
	@echo "Dependencies installed."

tree:
	@echo "Generating file path tree..."
	$(PYTHON_INTERPRETER) $(DEV_TOOLS_DIR)/create_path_tree.py
	@echo "File path tree generated in file_path_tree.txt."

add-paths:
	@echo "Adding path comments to Python files..."
	$(PYTHON_INTERPRETER) $(DEV_TOOLS_DIR)/add_path_comment.py
	@echo "Path comments added."

concat:
	@echo "Concatenating Python files..."
	$(PYTHON_INTERPRETER) $(DEV_TOOLS_DIR)/concat_files.py
	@echo "Files concatenated into concatenated_code.py."

lint:
	@echo "Linting the project with Ruff..."
	$(RUFF) check .
	@echo "Linting complete."

format:
	@echo "Formatting the project with Ruff..."
	$(RUFF) format .
	@echo "Formatting complete."

all-dev-tools: tree add-paths concat
	@echo "All development tools executed."

run:
	@echo "Running the main application ($(MAIN_APP_SCRIPT))..."
	$(PYTHON_INTERPRETER) $(MAIN_APP_SCRIPT)
	@echo "Application finished."

# Note: The 'run' target assumes 'src/main.py' exists and is executable.
# If 'ruff' or 'python3' are not in PATH, users may need to specify full paths or install them.
