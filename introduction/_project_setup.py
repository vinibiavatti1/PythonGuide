"""
Project Setup

* VS Code IDE can be used for Python programming.
* It is recommended to configure the IDE to has the Python linter and other
  features to follow the good practices of Python.
* NOTE: The repository python_project_template contains all you need to start a
  Python project.
"""

###############################################################################
# Create virtual environment
###############################################################################


# Check below to create a new folder with the Python env and set is as default.
"""
1. Create a folder called ".venv" inside the project
2. Access this folder with prompt command line
3. Type $ python -m venv <project-name> to create a new Python environment
4. Select this Python environment to be used in VS Code (Check _venv.py)
5. Set the Python Interpreter of the virtual environment as project default
   interpreter by adding the content below to /.vscode/settings.json:


{
    "python.defaultInterpreterPath":
        "${workspaceFolder}/.venv/Scripts/python.exe"
}
"""


###############################################################################
# Configure Python Linter (PyLama and MyPy)
###############################################################################


# I recommend PyLama to be used as Python Linter, since it has all necessary
# linters pre-configured. You just have to configure it in the settings file
# to define which linter you want to use from PyLama.
# MyPy is a Static Type Checker library that checks the type hints of your code
# and shows possible errors or inconsistencies. It is highly recommended to be
# used to contribute for the quality of the code.
# PyLama: https://github.com/klen/pylama
# MyPy: https://mypy-lang.org/
"""
1. Install PyLama using pip (pip install pylama)
2. Install MyPy using pip (pip install mypy)
2. Open your workspace settings file to configure PyLama and MyPy as the linter
   of your project: (File location: /.vscode/settings.json)
3. Ensure the lines below are set to settings.json file:


{
    "python.linting.enabled": true,
    "python.linting.pylamaEnabled": true,
    "python.linting.mypyEnabled": true
}
"""


# The linters must be configured at pyproject.toml file. Follow the steps below
# to configure the library.
"""
1. Create the pyproject.toml file in the root directory of the project
2. Open the file and configure the content below:


[tool.pylama]
linters = "pycodestyle"

[tool.pylama.linter.pycodestyle]
max_line_length = 79
count = true
statistics = true
ignore = []

[tool.mypy]
strict = true
check_untyped_defs = false
show_error_codes = true
disallow_any_generics = false
disable_error_code = []
"""


###############################################################################
# Configure Rulers (Vertical Line)
###############################################################################


# The PEP8 has defined that all code lines in Python should't exceed 79 chars
# The VSCode rulers (Vertical Line) is recommended to be used to show the limit
# To configure it, follow the next steps:
"""
1. Access: File > Preferences > Settings
2. Type "rulers"
3. In "Rulers" select "Edit in settings.json"
4. Put the 79 value inside the array (PEP8 convention)
5. Save the file


{
    "editor.rulers": [79]
}
"""


###############################################################################
# Editor Config
###############################################################################


# Editor config is a plugin that auto-configure your IDE based on .editorconfig
# file. It is recommended to keep consistence between the projects and to help
# new developers to configure their IDE.
"""
1. Install the "editorconfig" extension
2. In your project, create a file named .editorconfig
3. Put the content bellow in the file: (This is the standard configuration)


root = true

[*]
indent_style = space
indent_size = 4
insert_final_newline = true
trim_trailing_whitespace = true
end_of_line = lf
charset = utf-8

[*.py]
max_line_length = 79

[*.md]
trim_trailing_whitespace = false
"""


###############################################################################
# Configure the launch.json
###############################################################################


# The launch.json file has definitions for VSCode Debug. It is used to
# configure the entry point file of your project, and to set other Debug
# properties.
"""
1. In VSCode, go to "Run and Debug" section located on the left bar
2. Select "create a launch.json file". It will create a file at:
   /.vscode/launch.json
3. In the json file, set the "program" key to the path of the entry point file
   (main.py) file. Example: ${workspaceFolder}/main.py


{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Main",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal"
        }
    ]
}
"""


###############################################################################
# Hidden Files
###############################################################################


# Some files don't need to be present in the project explorer, since these
# files usually does not have any important or valuable content while coding
# in Python. To configure these files to be hidden just follow the next steps:
"""
1. At /.vscode/settings.json file, put the content below:


{
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/__pycache__": true,
        "**/*.pyc": true
    },
}
"""
