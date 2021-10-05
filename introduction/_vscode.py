"""
VS Code configurations

* VS Code IDE can be used for Python programming
* It is recommended to configure the IDE to has the PEP8 linter, Python linter,
  and other features to follow the good practicies of Python
* NOTE: The repository python_project_template contains all you need to start a
  Python project withou need to configure everything
"""

###############################################################################
# Create virtual environment
###############################################################################


# Create a new folder with the Python env
"""
1. Create a folder called ".venv" inside the project
2. Access this folder with prompt command line
3. Type $ python -m venv <project-name> to create a new Python environment
4. Select this Python environment to be used in VS Code (Check _venv.py)
"""


###############################################################################
# Configure Python Code Style (PEP8)
###############################################################################


# The pycodestyle is a python package that works as a lint to validate the PEP8
# convetions into the source code
"""
1. Install pycodestyle using pip (pip install pycodestyle)
2. In VSCode, access File > Preferences > Settings
3. Type "pycodestyle"
4. Mark "Pycodestyle Enabled"
5. Select "Information" for "Pycodestyle Category Severity: E"
6. Select "Information" for "Pycodestyle Category Severity: W"
"""


###############################################################################
# Configure Python Linter (pylint)
###############################################################################


# The pylint is a python package that validates the source code finding syntax
# and semantic errors
"""
1. Install pylint using pip (pip install pylint)
2. In VSCode, access File > Preferences > Settings
3. Type "pylint"
4. Mark "Python linting Enabled"
"""


###############################################################################
# Configure Rulers (vertical line)
###############################################################################


# Configure the vertical line to show the limit of the line of 79 characters
"""
1. Access File > Preferences > Settings
2. Type "rulers"
3. In "Rulers" select "Edit in settings.json"
4. Put the 79 value inside the array (PEP8 convention)
5. Save the file
"""


###############################################################################
# Editor config
###############################################################################


# Install the Editor config plugin to keep the editor configurations in a file
"""
1. Install the "editorconfig" extension
2. In your project, create a file named .editorconfig
3. Put the content bellow in the file:

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


# The launch.json is a file that configures the python to run the environment
"""
1. Go to "Run and Debug" section in the left bar
2. Select "create a launch.json file"
3. In the json, set the "program" key to the path of the main.py file
   * Example: ${workspaceFolder}/main.py

An example of configuration can be used like below:

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
