"""
PIP requeriments

* The requeriments is a text file that contains all of the dependencies and
  versions to configure some Python project using PIP
* This file can be put into version control
* A version specifier consists of a series of version clauses, separated by
  commas
  * Example: ~= 0.9, >= 1.0, != 1.3.4.*, < 2.0
* The comparison operator determines the kind of version clause:
  * ~=: Compatible release clause
  * ==: Version matching clause
  * !=: Version exclusion clause
  * <=, >=: Inclusive ordered comparison clause
  * <, >: Exclusive ordered comparison clause
  * ===: Arbitrary equality clause.
"""

# Create empty requeriments.txt
""" $ type nul > requeriments.txt """


# Create file with Python dependencies
""" $ pip freeze > requeriments.txt """


# Install requeriments dependencies
""" $ pip install -r requeriments.txt """


# Requeriments.txt format
"""
requests == 2.25.1
pandas >= 0.18.1
numpy <= 1.20.1
matplotlib > 3.0.0, < 3.3.4
"""
