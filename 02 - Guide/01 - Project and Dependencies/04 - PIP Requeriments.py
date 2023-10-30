"""
PIP Requirements

* The PIP requirements is a file that contains all the dependencies of the
  project listed in a specific format
* The format of the requirements file is text, and is commonly named as
  "requirements.txt"
* Usually, this file is put into version control to allows the developers to
  downloads the required packages of the project using pip commands
* A version specifier consists of a series of version clauses, separated by
  commas, example: ~= 0.9, >= 1.0, != 1.3.4.*, < 2.0
* The comparison operator determines the kind of version clause:
  * ~=: Compatible release clause
  * ==: Version matching clause
  * !=: Version exclusion clause
  * <=, >=: Inclusive ordered comparison clause
  * <, >: Exclusive ordered comparison clause
  * ===: Arbitrary equality clause.
"""


###############################################################################
# Create requirements.txt file
###############################################################################


# List project packages
# * Use the command `pip freeze` to generate a list of packages and their
#   version to store into the requirements.txt file
# * Use the second example to store the list into the requirements.txt file
"""
Input Example:
$ pip freeze

Output Example:
attrs==23.1.0
colorama==0.4.6
mypy==0.991
mypy-extensions==0.4.3
pycodestyle==2.10.0
pydocstyle==6.3.0
pylama==8.4.1
requests==2.31.0
"""


# Store project packages into requirements.txt file
# * We can generate the list of the project packages and store it into the
#   requirements.txt file manually, or we can use the command below to do it
#   automatically
"""
Input Example:
$ pip freeze > ./requirements.txt
"""


# Create an empty requirements.txt file
# * We can use the OS common commands to create an empty file
"""
Input Example:
$ type nul > ./requirements.txt
"""


###############################################################################
# Show requirements.txt file
###############################################################################


# Show the content of the file
# * We can use the OS common commands to check the content of the file
"""
Input Example:
$ type ./requirements.txt

Output Example:
attrs==23.1.0
colorama==0.4.6
mypy==0.991
mypy-extensions==0.4.3
pycodestyle==2.10.0
pydocstyle==6.3.0
pylama==8.4.1
requests==2.31.0
"""


###############################################################################
# Install Dependencies from requirements.txt file
###############################################################################


# Install required dependencies
# * To install required dependencies from the requirements.txt file, we can use
#   the `pip install -r requirements.txt` command
# * The "-r" option is used to specify the requirements file
"""
Input Example:
$ pip install -r ./requirements.txt
"""
