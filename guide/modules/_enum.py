"""
Enum module

* An enumeration is a set of symbolic names (members) bound to unique, constant
  values. Within an enumeration, the members can be compared by identity, and
  the enumeration itself can be iterated over
* The enum module provides an way to create classes as enums
"""
from enum import Enum, unique


###############################################################################
# Enum
###############################################################################


# Create Enum
# * To create an Enum, the class must use the Enum class as base class
# * The keys of the Enum are defined as class variables
class Colors(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# Access key
# * To access the key, just access the class variable from the class
print(type(Colors.RED))
print(Colors.RED)
# <enum 'Colors'>
# Colors.RED


# Access key by name
# * The enum class can be accessed as a dict using the name of the key as the
#   dict key
key = Colors['BLUE']
print(key)
# Colors.BLUE


# Access key by value
# * The value of the key can be used to access that
key = Colors(2)
print(key)
# Colors.GREEN


# Iterate by keys
# * The Enum class provides an ways to iterate by the keys inside the Enum
for color in Colors:
    print(color, end=', ')
print()
# Colors.RED, Colors.GREEN, Colors.BLUE,


# Key properties
# * Each enum key has the name and value properties to access the key data
# * NOTE: You can set the value as a tuple to define more data to the enum key
print(Colors.RED.name, Colors.RED.value, sep=', ')
# RED, 1


# Check instance
# * The isinstance keyword can be used to check if the key is from enum
print(isinstance(Colors.RED, Colors))
# True


# Compare enum keys
# * The is operator can be used to comparte the keys
print(Colors.RED is Colors.RED)
# True


###############################################################################
# Unique
###############################################################################


# Unique
# * The @unique decorator can be used to define that the Enum class cannot have
#   duplicate values for the keys
"""
@unique
class Numbers(Enum):
    ONE = 1
    TWO = 2
    THREE = 2

ValueError: duplicate values found in <enum 'Numbers'>: THREE -> TWO
"""
