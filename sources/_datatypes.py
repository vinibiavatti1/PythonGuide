"""
Datatypes examples

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""
# Datatypes
x = 'Hello World'        # str
x = 1                    # int
x = 3.5                  # float
x = 1j                   # complex (Create imaginary numbers)
x = range(5)             # range
x = [1, 2, '3']          # list
x = (1, 2, '3')          # tuple
x = {1, 2, '3'}          # set
x = {'age': 26}          # dict
x = frozenset({1, 2, 3}) # frozenset
x = True                 # bool
x = b'Hello World'       # bytes
x = bytearray(5)         # bytearray
x = memoryview(bytes(5)) # memoryview

# Casting
x = str('Hello World')   # str
x = int(1)               # int
x = float(3.5)           # float
x = complex(1j)          # complex (Create imaginary numbers)
x = range(5)             # range
x = list((1, 2, '3'))    # list
x = tuple((1, 2, '3'))   # tuple
x = set((1, 2, '3'))     # set
x = dict(age=26)         # dict
x = frozenset((1, 2, 3)) # frozenset
x = bool(5)              # bool
x = bytes(5)             # bytes
x = bytearray(5)         # bytearray
x = memoryview(bytes(5)) # memoryview