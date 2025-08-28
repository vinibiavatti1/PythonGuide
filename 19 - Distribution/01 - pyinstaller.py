"""
PyInstaller

* PyInstaller freezes (packages) Python applications into stand-alone
  executables, under Windows, GNU/Linux, Mac OS X, FreeBSD, Solaris and AIX
* It is a external dependency, so, it needs to be installed by PIP
* The installer will put the pyhton interpreter inside the bundle, and the app
  can be distributed for anyone
* When PyInstaller is executed, it will genereate a spec file:
  * The myscript.spec file contains most of the information provided by the
    options that were specified when pyinstaller (or pyi-makespec) was run with
    the script file as the argument. You typically do not need to specify any
    options when running pyinstaller with the spec file
  * This file can be used by PyInstaller to follow the same way to generate
    the bundle
"""


###############################################################################
# PyInstaller
###############################################################################


# Install PyInstaller
# * To install the PyInstaller, we must use the pip with the command:
""" $ pip install pyinstaller """


# Generate Executable (.exe)
# * To generate a standalone executable, we can use the command below.
# * Usually, PyInstaller creates a bundle with the executable and the python
#   dependencies outside the executable. To include everything inside the
#   executable, we can use the --onefile option.
# * Also, the --noconsole option is useful for GUI applications to prevent
#   a console window from appearing.
""" $ pyinstaller --noconsole --onefile <main>.py """
