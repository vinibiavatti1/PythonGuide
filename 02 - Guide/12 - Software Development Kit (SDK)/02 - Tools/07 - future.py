"""
Future module

* __future__ is a real module, and serves three purposes:
  * To avoid confusing existing tools that analyze import statements and expect
    to find the modules they're importing
  * To ensure that future statements run under releases prior to 2.1 at least
    yield runtime exceptions (the import of __future__ will fail, because there
    was no module of that name prior to 2.1)
  * To document when incompatible changes were introduced, and when they will
    be — or were — made mandatory. This is a form of executable documentation,
    and can be inspected programmatically via importing __future__ and
    examining its contents

* The future module can enable new language features which are not compatible
  with the current
"""
from __future__ import with_statement
import threading


# Using with statement in different Python versions
# * Enable PEP 343: The "with" Statement
lock = threading.Lock()
with lock:
    print('Running!')
# Running!
