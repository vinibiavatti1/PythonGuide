"""
VS Code configurations

* I recomend to configure the VS Code with the follow configurations to follow
  the PEP 8


# -----------------------------------------------------------------------------
# 1. Configure PEP8


1. File > Preferences > Settings
2. Type "pycodestyle"
3. Mark "Pycodestyle Enabled"
4. Select "Information" for "Pycodestyle Category Severity: E"
5. Select "Information" for "Pycodestyle Category Severity: W"


# -----------------------------------------------------------------------------
# 2. Configure Rulers (vertical line)


1. File > Preferences > Settings
2. Type "rulers"
3. In "Rulers" select "Edit in settings.json"
4. Put 79 inside the array
5. save


# -----------------------------------------------------------------------------
# 3. Editor config


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
max_line_length = 20

[*.md]
trim_trailing_whitespace = false

"""
