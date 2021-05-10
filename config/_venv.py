"""
Virtual Environment

* Python applications will often use packages and modules that don't come as
  part of the standard library. Applications will sometimes need a specific
  version of a library, because the application may require that a particular
  bug has been fixed or the application may be written using an obsolete
  version of the library's interface
* The module used to create and manage virtual environments is called venv.
  venv will usually install the most recent version of Python that you have
  available. If you have multiple versions of Python on your system, you can
  select a specific Python version by running python3 or whichever version you
  want
* The "venv" module has the same purpose of non-native "virtualenv" module
"""


###############################################################################
# Virtual Environment
###############################################################################


# Create a virtual environment
# * To create a virtual environment, decide upon a directory where you want to
#   place it, and run the venv module as a script with the directory path
""" $ python -m venv my-app """


# Activate virtual environment
# * Activating the virtual environment will change your shell's prompt to show
#   what virtual environment you're using, and modify the environment so that
#   running python will get you that particular version and installation of
#   Python
""" $ my-app/Scripts/activate.bat """


# Managing Packages with pip
# * You can install, upgrade, and remove packages for your virtual env using
#   pip. You must activate your environment first to call pip from this env
""" (my-app) $ pip install numpy """


###############################################################################
# VSCode
###############################################################################


# Select environment in VSCode
# * VSCode provides a way to change the Python interpreter for the current
#   project. To do it, you can:
"""
1. Click on the Python interpreter in the booton toolbar or press Ctrl + Shift
   + P and type "Python: Select Interpreter"
2. Enter with the "python.exe" interpreter from the virtual env created
3. To run the Python file with this interpreter, just click in the green play
   button on the top right, or right click in the file and choose "Run Python
   File in Terminal"
"""
