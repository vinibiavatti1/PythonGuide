"""
Datatypes

* Datatypes are the classification or categorization of data items.
* The datetype will determine the way the data is stored and what operations
  can be performed on that data.
* Below are the datatypes in Python:
###############################################################################
Datatype    Category  Example
###############################################################################
str         Text      'Hello World'
int         Numeric   1
float       Numeric   3.5
complex     Numeric   1j
list        Sequence  [1, 2, '3']
tuple       Sequence  (1, 2, '3')
range       Sequence  range(5)
dict        Mapping   {'age': 26}
set         Set       {1, 2, '3'}
frozenset   Set       frozenset({1, 2, 3})
bool        Boolean   True
bytes       Binary    b'Hello World'
bytearray   Binary    bytearray(5)
memoryview  Binary    memoryview(bytes(5))
NoneType    Null      None
###############################################################################
"""


###############################################################################
# Datatypes
###############################################################################


# Datatypes
# * Datatypes are the type of data that can be stored in a variable
# * Below we are assigning different datatypes to the variable `x`
x = 'Hello World'         # str
x = 1                     # int
x = 3.5                   # float
x = 1j                    # complex
x = range(5)              # range
x = [1, 2, '3']           # list
x = (1, 2, '3')           # tuple
x = {1, 2, '3'}           # set
x = {'age': 26}           # dict
x = frozenset({1, 2, 3})  # frozenset
x = True                  # bool
x = b'Hello World'        # bytes
x = bytearray(5)          # bytearray
x = memoryview(bytes(5))  # memoryview
x = None                  # NoneType


# Using class constructors
# * We can also use class constructors to create datatypes
x = str('Hello World')    # str
x = int(1)                # int
x = float(3.5)            # float
x = complex(1j)           # complex
x = range(5)              # range
x = list((1, 2, '3'))     # list
x = tuple((1, 2, '3'))    # tuple
x = set((1, 2, '3'))      # set
x = dict(age=26)          # dict
x = frozenset((1, 2, 3))  # frozenset
x = bool(5)               # bool
x = bytes(5)              # bytes
x = bytearray(5)          # bytearray
x = memoryview(bytes(5))  # memoryview
x = None                  # NoneType
