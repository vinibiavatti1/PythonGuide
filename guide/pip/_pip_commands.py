"""
PIP commands

* pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4
  downloaded from python.org
* Reference: https://$ pip.pypa.io/en/stable/reference/
"""


# PIP install
# * Install packages
"""
$ pip install [options] <requirement specifier> [package-index-options] ...
$ pip install [options] -r <requirements file> [package-index-options] ...
$ pip install [options] [-e] <vcs project url> ...
$ pip install [options] [-e] <local project path> ...
$ pip install [options] <archive url/path> ...

Example: $ pip install numpy
Example: $ pip install -r requeriments.txt
"""


# PIP download
# * Download packages
"""
$ pip download [options] <requirement specifier> [package-index-options] ...
$ pip download [options] -r <requirements file> [package-index-options] ...
$ pip download [options] <vcs project url> ...
$ pip download [options] <local project path> ...
$ pip download [options] <archive url/path> ...

Example:
$ pip download numpy
"""


# PIP unistall
# * Uninstall packages
"""
$ pip uninstall [options] <package> ...
$ pip uninstall [options] -r <requirements file> ...

Example:
$ pip uninstall numpy
"""


# PIP freeze
# * Output installed packages in requirements format
"""
$ pip freeze [options]

Example:
$ pip freeze
"""


# PIP list
# * List installed packages, including editables
"""
$ pip list [options]

Example:
$ pip list
"""


# PIP show
# * Show information about one or more installed packages
"""
$ pip show [options] <package> ...

Example:
$ pip show numpy
"""


# PIP search
# * Search for PyPI packages whose name or summary contains <query>
"""
$ pip search [options] <query>

Example:
$ pip search numpy
"""


# PIP cache
# * Inspect and manage $ pip’s wheel cache
"""
$ pip cache dir
$ pip cache info
$ pip cache list [<pattern>] [--format=[human, abspath]]
$ pip cache remove <pattern>
$ pip cache purge
"""


# PIP check
# * Verify installed packages have compatible dependencies
"""
$ pip check [options]
"""


# PIP config
# * Manage local and global configuration
"""
$ pip config [<file-option>] list
$ pip config [<file-option>] [--editor <editor-path>] edit
$ pip config [<file-option>] get name
$ pip config [<file-option>] set name value
$ pip config [<file-option>] unset name
$ pip config [<file-option>] debug
"""


# PIP wheel
# * Build Wheel archives for your requirements and dependencies
# * NOTE: Wheel is a built-package format, and offers the advantage of not
#   recompiling your software during every install
"""
$ pip wheel [options] <requirement specifier> ...
$ pip wheel [options] -r <requirements file> ...
$ pip wheel [options] [-e] <vcs project url> ...
$ pip wheel [options] [-e] <local project path> ...
$ pip wheel [options] <archive url/path> ...
"""


# PIP hash
# * Compute a hash of a local package archive
"""
$ pip hash [options] <file> ...
"""


# PIP debug
# * Display debug information
"""
$ pip debug <options>
"""
