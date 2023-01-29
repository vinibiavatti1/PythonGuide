"""
Variables

* Variables store data to the memory
* The name of the variable or constant must not be any of Python's keywords
* Scalars variables are variables represented with just one value
* Collections variables are variables represented with some collections
  containing scalar values
* Python does not have constants since there is no way to create a read only
  variable. Because of this, we use uppercase to show the variables that are
  represented as constants.
* The examples use the variable name "x", but any name can be given to the
  variable
* The datatypes are:
  * Text Type: str
  * Numeric Types: int, float, complex
  * Sequence Types: list, tuple, range
  * Mapping Type: dict
  * Set Types: set, frozenset
  * Boolean Type: bool
  * Binary Types: bytes, bytearray, memoryview
  * None Type: NoneType
"""


###############################################################################
# Declarations (Boolean Type)
###############################################################################


# Declare a variable (bool)
# * Python has a simple syntax to declare variables
# * The example below shows how to create a boolean (True or False) variable
# * The boolean values must be defined capitalized
x = True
x = False


###############################################################################
# Declarations (Numeric Types)
###############################################################################


# Declare a variable (int)
# * The example below declares a variable with an integer value
# * Negative numbers are also allowed
# * The underscore "_" can be use to identify bigger numbers.
#   * Example: (x=100_000) will be equivalent to (x=100000)
x = 1
x = -5
x = 100_000_000


# Declare a variable (float)
# * The example below declares a variable with a float value
# * The last examples are a short way with the zero omitted
x = 3.0
x = 4.892
x = 3.  # 3.0
x = .5  # 0.5


# Declare a variable (complex)
# * The example below declares a variable with a complex value
# * The "j" char is used to represent the imaginary number
x = 2j


# Declare a variable using hexadecimal format (0x)
# * Python supports the hexadecimal format (base 16) to define integer
#   variables
# * The "0x" prefix is used to define a hexadecimal integer
x = 0x1A9C  # 6812
x = 0xFFF   # 4095
x = 0x0     # 0


# Declare a variable using octal format (0o)
# * Python supports the octal format (base 8) to define integer variables
# * The "0o" prefix is used to define an octal integer
x = 0o123  # 83
x = 0o7    # 7
x = 0o0    # 0


###############################################################################
# Declarations (Text Type)
###############################################################################


# Declare a variable (string)
# * The example below declares a variable with a string value
# * The char ' and " can be used to declare a string
# * Multiline strings can be defined by using ''' or """ char pattern
x = 'Hello World'


# Declare a variable (multiline string)
# * Multiline strings can be defined by using ''' or """ char pattern
x = '''This is an
example of a text
with multiple
lines'''


###############################################################################
# Declarations (Sequence Types)
###############################################################################


# Declare a variable (list)
# * A list can contain multiple values
# * The list can be iterable using the "for" instruction, or using the "iter(),
#   next()" functions
# * The [ and ] chars are used to create a list
# * The last example creates an empty list
# * The list() function can be used to create an empty list
x = [1, 2, 3]
x = [True, 'Hi', 2j]
x = [1]
x = []
x = list()


# Declare a variable (tuple)
# * A tuple is similar to a list, but it is immutable (cannot change the values
#   inside)
# * The ( and ) chars are used to create a list
# * NOTE: To create a tuple with a single value, we must use the comma ","
#   after the value, otherwise, a generator will be created instead (last
#   example)
# * The tuple() function can be used to create an empty tuple
x = (1, 2, 3)
x = (True, 'Hi', 2j)
x = (1,)
x = ()
x = tuple()


# Declare a variable (range)
# * The range is used to create a generator of a sequence of numbers
# * Only integer values are allowed
# * The range() builtin function is used to define ranges
# * It can be iterated by using "for" or "iter() next()"
x = range(10)
x = range(5, 10)
x = range(5, 10, 2)


###############################################################################
# Declarations (Mapping Type)
###############################################################################


# Declare a variable (dict)
# * The examples below shows how to create a dictionary
# * The dict is used to create a mapper (key -> value)
# * The { and } are used to define a dict
# * The dict() function can be used also to create a dict
x = {'name': 'Vini'}
x = {'name': 'Vini', 'level': 5, 'active': True}
x = dict(name='Vini', level=5)
x = {}


###############################################################################
# Declarations (Set Types)
###############################################################################


# Define a variable (set)
# * The set is a collection that cannot has duplicated values
# * The set itself will parse the values to contain only unique values
# * The { and } are used to define a set. NOTE: The format of the value will
#   indicate if the value is a dictionary, or a set
# * To create a empty set, the "set()" function must be used, otherwise, the
#   variable will become a dictionary
x = {1, 2, 3}
x = {True, 'Hi', 2j}
x = set()


# Define a variable (frozenset)
# * The frozenset is similar to the set, but it is immutable
# * To create a frozenset, the "frozenset()" function must be used
# * A set must be passed as an argument to the frozenset, and the set will be
#   converted to a frozenset
x = frozenset({1, 2, 3})
x = frozenset({True, 'Hi', 2j})
x = frozenset()


###############################################################################
# Declarations (None Type)
###############################################################################


# Define a null pointer variable (None)
# * To define a variable with a null pointer, the "None" type can be used
# * The None value must be defined capitalized
x = None


###############################################################################
# Declarations (Binary Types)
###############################################################################


# Define a variable (bytes)
# * To define a variable that store bytes, we can use the "b" prefix to a
#   string type
# * The first example stores the value "蓏콯" of UTF-16 format
# * The "bytes()" function can be used to define a variable of bytes type
# * The difference of bytes to bytearray is that bytes contains an immutable
#   value while bytearray is mutable
x = b'\xcf\x84o\xcf'
x = b'Hello World'
x = b''
x = bytes('Hello World', 'utf-8')
x = bytes(5)  # b'\x00\x00\x00\x00\x00'


# Define a variable (bytearray)
# * Similar to bytes, but it is mutable
# * The "bytearray()" function can be used to define a variable of bytearray
#   type
x = bytearray(b'\xcf\x84o\xcf')
x = bytearray('Hello World', 'utf-8')
x = bytearray()
x = bytearray(5)  # b'\x00\x00\x00\x00\x00'


###############################################################################
# Inline Declarations
###############################################################################


# Declare multiple variables (inline)
# * We can declare multiple variable in the same line using the syntax below
# * The expression (x, y, z = 1, 2, 3) will result to: x = 1, y = 2, z = 3
x, y, z = 1, 2, 3
x, y = 'Hello', 'World'


# Declare multiple variables with the same value (inline)
# * To create multiple variables containing the same value inline, we can use
#   the syntax below
# * The expression (x = y = z = 1) will result to: x = 1, y = 1, z = 1
x = y = z = 1
x = y = 'Hello World'
