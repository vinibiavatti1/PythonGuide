"""
PIP (Python Installer Package)

* PIP is a package manager for Python that allows you to install, upgrade, and
  remove Python packages.
* PIP is included by default with Python installations starting from version
  3.4.
* You can use PIP to install packages from the Python Package Index (PyPI) or
  from other sources.
* PIP is a command-line tool, and you can use it by running the `pip` command
  in your terminal or command prompt.
* PIP can be used to install packages globally or within a virtual environment.
"""


###############################################################################
# Managing Packages
###############################################################################


# Installing Packages
# * To install a package in the environment, you can use the command below.
# * Make sure to activate the virtual environment before running the install
#   command, otherwise the package will be installed globally.
""" (.venv) $ pip install package_name """


# Upgrading Packages
# * To upgrade a package to the latest version, you can use the command below.
# * Make sure to activate the virtual environment before running the upgrade
#   command, otherwise the package will be upgraded globally.
""" (.venv) $ pip install --upgrade package_name """


# Uninstalling Packages
# * To uninstall a package from the environment, you can use the command below.
# * Make sure to activate the virtual environment before running the uninstall
#   command, otherwise the package will be uninstalled globally.
""" (.venv) $ pip uninstall package_name """


###############################################################################
# Freezing Packages
###############################################################################


# Freezing Requirements
# * To create a requirements file that lists all installed packages and their
#   versions, you can use the command below.
# * This is useful for sharing your environment setup with others.
# * This command will create a requirements.txt file with all installed
#   packages.
""" (.venv) $ pip freeze > requirements.txt """


# Installing Packages (From Requirements File)
# * To install packages listed in a requirements.txt file, you can use the
#   command below.
# * Make sure to activate the virtual environment before running the install
#   command.
""" (.venv) $ pip install -r requirements.txt """
