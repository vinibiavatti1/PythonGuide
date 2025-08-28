"""
Virtual Environment

* Python applications will often use packages and modules that don't come as
  part of the standard library. Applications will sometimes need a specific
  version of a library, because the application may require that a particular
  bug has been fixed or the application may be written using an obsolete
  version of the library's interface.
* You can use virtual environments (venvs) to define a specific version of the
  Python interpreter for each project, and to define which external libraries
  will be applied to each project (Remember that the libraries are installed
  at Python's interpreter folder, and not to the project itself).
* The module used to create and manage virtual environments is called venv.
  venv will usually install the most recent version of Python that you have
  available. If you have multiple versions of Python on your system, you can
  select a specific Python version by running python3 or whichever version you
  want.
"""


###############################################################################
# Virtual Environment
###############################################################################


# Creating a virtual environment
# * To create a virtual environment, decide upon a directory where you want to
#   place it, and run the venv module as a script with the directory path.
# * Usually, the folder is named ".venv"
# * It is recommended to always create a virtual environment for all Python
#   projects.
# * NOTE: If you are using git, remember to add the .venv folder to your
#   .gitignore file, since it doesn't need to be shared.
""" $ python -m venv .venv """


# Activating the virtual environment
# * To activate the virtual environment, run the activate script, located in the
#   Scripts subdirectory of the virtual environment folder (path below).
# * The activation is used to modify the shell's environment so that the
#   Python interpreter and any installed packages are isolated to this
#   virtual environment.
# * For example, if you have a script that requires a specific version of a
#   library, you can install that library in the virtual environment without
#   affecting other projects.
""" $ .venv/Scripts/activate.bat """


# Checking if the virtual environment is activated
# * To ensure that the virtual environment is activated, you can check the
#   shell prompt. It should show the name of the virtual environment
#   (e.g., "(.venv)") before the command prompt.
""" (.venv) $ """


###############################################################################
# VSCode
###############################################################################


# Selecting the interpreter
# * If you are using VSCode, you can select the Python interpreter for your
#   project by following these steps:
#   1. Open the Command Palette (Ctrl + Shift + P) and type
#      "Python: Select Interpreter"
#   2. Choose the interpreter from the virtual environment you created
#   3. To run the Python file with this interpreter, just click in the green
#      play button on the top right, or right click in the file and choose
#      "Run Python File in Terminal"
# * In modern VSCode versions, this selection can be made on the status bar
#   (bottom left corner)
""" Ctrl + Shift + P > Python: Select Interpreter """
