"""
PIP (Python Installer Package) Commands

* The PIP module is already installed if you are using Python >= 2.7.9 or
  Python >= 3.4 downloaded from python.org
* PIP can be called using `$ python -m pip` command or just `$ pip` depending
  the Python version (The -m mean "module" and is used to call modules from
  Python)
* Reference: https://$ pip.pypa.io/en/stable/reference/
"""


###############################################################################
# Common Commands
###############################################################################


# PIP List
# * The `pip list` command is used to list the installed packages in the
#   project
# * Use the command `pip freeze` to generate a requirements.txt file format,
#   since the output has a different format (table format)
"""
Syntax:
$ pip list [options]

Input Example:
$ pip list

Output Example:
Package                                         Version
----------------------------------------------- --------
attrs                                           23.1.0
colorama                                        0.4.6
mypy                                            0.991
mypy-extensions                                 0.4.3
pip                                             22.3.1
pycodestyle                                     2.10.0
pydocstyle                                      6.3.0
pylama                                          8.4.1
requests                                        2.31.0
"""


# PIP Install
# * The `pip install` command is used to install new packages or upgrade
#   existing packages
"""
Syntax:
$ pip install [options] <requirement specifier> [package-index-options] ...
$ pip install [options] -r <requirements file> [package-index-options] ...
$ pip install [options] [-e] <vcs project url> ...
$ pip install [options] [-e] <local project path> ...
$ pip install [options] <archive url/path> ...

Input Examples:
$ pip install numpy
$ pip install -r requirements.txt
$ pip install numpy --upgrade
"""


# PIP Uninstall
# * The `pip uninstall` command is used to uninstall packages
"""
Syntax:
$ pip uninstall [options] <package> ...
$ pip uninstall [options] -r <requirements file> ...

Input Example:
$ pip uninstall numpy
"""


# PIP Freeze
# * The `pip freeze` command is used to output installed packages in a text
#   format (requirements.txt format)
# * When performed, the command will generate a list of packages and their
#   version into the terminal, in which it can be saved to a file called
#   requirements.txt.
# * The requirements.txt file can be used to install the same packages into the
#   project
"""
Syntax:
$ pip freeze [options]

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


###############################################################################
# Other Commands
###############################################################################


# PIP Download
# * The `pip download` command does the same resolution and downloading as
#   `pip install`, but instead of installing the dependencies, it collects the
#   downloaded distributions into the directory provided
"""
Syntax:
$ pip download [options] <requirement specifier> [package-index-options] ...
$ pip download [options] -r <requirements file> [package-index-options] ...
$ pip download [options] <vcs project url> ...
$ pip download [options] <local project path> ...
$ pip download [options] <archive url/path> ...

Input Example:
$ pip download numpy
"""


# PIP Show
# * The `pip show` command is used to show infos about one or more installed
#   packages
"""
Syntax:
$ pip show [options] <package> ...

Input Example:
$ pip show requests

Output Example:
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
...
"""


# PIP Cache
# * The `pip cache` command is used to manage the pip cache
# * Sub-commands:
#   * dir: Show the cache directory.
#   * info: Show information about the cache.
#   * list: List filenames of packages stored in the cache.
#   * remove: Remove one or more package from the cache.
#   * purge: Remove all items from the cache.
"""
Syntax:
$ pip cache dir
$ pip cache info
$ pip cache list [<pattern>] [--format=[human, abspath]]
$ pip cache remove <pattern>
$ pip cache purge

Input Example:
$ pip cache dir

Output Example:
c:/.../appdata/local/pip/cache
"""


# PIP Check
# * The `pip check` command is used to verify if the installed packages have
#   compatible dependencies
"""
Syntax:
$ pip check [options]

Input Example:
$ pip check

Output Example:
No broken requirements found.
"""


# PIP Config
# * The `pip config` command is used to manage local and global configurations
#   of pip
# * For example, this command can be used to set other trusted index urls to
#   search for packages
"""
Syntax:
$ pip config [<file-option>] list
$ pip config [<file-option>] [--editor <editor-path>] edit
$ pip config [<file-option>] get name
$ pip config [<file-option>] set name value
$ pip config [<file-option>] unset name
$ pip config [<file-option>] debug

Input Example:
$ pip config set global.index-url https://pypi.org/simple/

Output Example:
Writing to C:/.../AppData/Roaming/pip/pip.ini
"""


# PIP Wheel
# * The `pip wheel` command is used to manage wheel packages
# * Wheel is a built-package format, and offers the advantage of not
#   recompiling your software during every install
# * Wheel packages comes in a ready-to-install format and allows you to skip
#   the build stage required with source distributions
"""
Syntax:
$ pip wheel [options] <requirement specifier> ...
$ pip wheel [options] -r <requirements file> ...
$ pip wheel [options] [-e] <vcs project url> ...
$ pip wheel [options] [-e] <local project path> ...
$ pip wheel [options] <archive url/path> ...

Input Example:
$ pip wheel numpy
"""


# PIP Hash
# * The `pip hash` command is used to compute a hash of a local package archive
# * It can be used to verify the integrity of downloaded packages
"""
Syntax:
$ pip hash [options] <file> ...

Input Example:
$ pip hash ./requirements.txt

Output Example:
./requirements.txt:
--hash=sha256:46b26008ce97fa1d4b26328f3cf8115c02fc3211046f96c08b759e79e401e975
"""


# PIP Debug
# * The `pip debug` command is used to display debug information about the pip
#   module
"""
Syntax:
$ pip debug <options>

Input Example:
$ pip debug

Output Example:
pip version: pip 22.3.1 from C:/.../Lib/site-packages/pip (python 3.11)
sys.version: 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39)
sys.executable: C:/.../python.exe
sys.getdefaultencoding: utf-8
sys.getfilesystemencoding: utf-8
...
"""


# PIP Inspect
# * The `pip inspect` command is used to inspect the content of a Python
#   environment and produce a report in JSON format
"""
Syntax:
$ python -m pip inspect [options]

Input Example:
$ pip inspect

Output Example:
{
    "version": "0",
    "pip_version": "22.3.1",
    "installed": [
        {
            "metadata": {
                "metadata_version": "2.1",
                "name": "aiohttp",
                "version": "3.8.4",
                "summary": "Async http client/server framework (asyncio)",
                "description": "...",
                ...
            }
        }
    ]
}
"""


# PIP Search (Deprecated)
# * The `pip search` command is used to search for packages in PyPI
# * NOTE: This command is deprecated, use the browser search instead
"""
Syntax:
$ pip search [options] <query>

Input Example:
$ pip search "numpy"

Output Example:
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search).
Please use https://pypi.org/search (via a browser) instead.
See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods
for more information.
"""
