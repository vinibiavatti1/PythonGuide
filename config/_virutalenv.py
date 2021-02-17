"""
Virtualenv

* Virtualenv of python is a specific environment created for a project to
  guarantee that the projects use determinated version of Python, we can create
  a virtual env to configure the correct version for that project, avoiding to
  use the global python
* An "environment" in Python is the context in which a Python program runs
* To create a virtual env, we must need to install the following libs:
  * virtualenv
  * virtualenvwrapper
* After create a virtual env, the python will copy everthing is necessary to
  run Python in that environment.
* Professional Python developers usually create a new env for each python
  project with the same name with the project to allow to manipulate the
  configurations for that env

# -----------------------------------------------------------------------------
# Installing

1. Install command:
$ pip install virtualenv virtualenvwrapper

# -----------------------------------------------------------------------------
# Configuring

1. Create virtual env command:
$ mkvirtualenv <env_name> [-p <python_command>]

2. To exit a virutal env from cmd use:
$ deactivate
"""
