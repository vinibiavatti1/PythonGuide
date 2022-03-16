"""
Project Structure.

* The python project structure can be defined following the single
  responsibility concept.
* The proposal has some optional contents, like configuration files for common
  plugins.
* The __init__.py file was omitted in the representation of a project
  structure for packages.
"""


###############################################################################
# Project Structure
###############################################################################


# Project Structure proposal
"""
###############################################################################
Structure                               Description
###############################################################################
.git                                    Git folder
.venv                                   Python environment folder
.vscode                                 VSCode workspace configuration
scripts                                 Scripts folder
    run_app.ps1                         Powershell script to run the app
    run_code.ps1                        Powershell script to run vscode
    run_freeze.ps1                      Powershell script to run pip freeze
    run_setup.ps1                       Powershell script to run env setup
project                                 Project folder
    constrollers                        Web endpoints/Gui controllers
    decorators                          Python function decorators
    enums                               Enumarations
    errors                              Custom exceptions
    guis                                Graphical user interface files
    models                              Class models
    records                             Preset data
    repositories                        Data persitence functions
    services                            Business rules functions
    utils                               Util functions
    validators                          Data validation functions
    __init__.py                         Python module file.
.editorconfig                           Edtor config file
.gitignore                              Git ignore file
main.py                                 Project entry point
README.md                               Repository documentation
CONTRIBUTING.md                         Contributing documentation
LICENSE.md                              License file
requirements.txt                        Project PIP dependencies
setup.cfg                               General plugin configuration
"""
