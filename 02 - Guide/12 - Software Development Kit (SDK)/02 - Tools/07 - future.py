"""
Future module

* The `__future__` module is used to enable features that are not available in
  the current Python version
"""


###############################################################################
# Importing New Features
###############################################################################


# Importing a new feature
# * We can use the `__future__` module to enable features that are not
#   available in the current Python version
# * In the example below, we enable the `with_statement` feature
# * NOTE: This feature is already available in the current Python version, it
#   is used here as an example only
# * The `threading.Lock` class is only used as example here to demonstrate the
#   `with` statement behavior
from __future__ import with_statement
from threading import Lock
with Lock():
    print('With statement is available')
# With statement is available
