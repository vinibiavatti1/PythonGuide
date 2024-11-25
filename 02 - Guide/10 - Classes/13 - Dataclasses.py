"""
Dataclasses

* The dataclasses module provides a decorator and functions for automatically
  adding special methods such as __init__() and __repr__() to user-defined
  classes.
* This can be used to simplify the creation of classes that are mostly used to
  store data.
* This concept is known as "record classes" or "data classes" in other
  laguages.
* The Dataclasses was originally described in PEP 557.
* Below there is a table with the purpose for some common function from the
  module.

###############################################################################
Function        Purpose
###############################################################################
@dataclass      Decorator that defines a class as a dataclass
field()         Function used to configure the fields of the dataclass
fields()        Function used to get the fields of the dataclass
###############################################################################
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
from dataclasses import (
    dataclass,
    field,
    fields,
)


###############################################################################
# Creating a Dataclass
###############################################################################


# Creating a Dataclass
# * To create a dataclass, we need to use the dataclass decorator frpm the
#   dataclasses module
# * This decorator will add some special methods to the class, like
#   `__init__` and `__repr__` methods.
# * The class attributes are defined as class fields, and will be used to
#   create the class structure
@dataclass
class Person:
    name: str
    age: int


# Creating an instance of the Dataclass
# * After creating the dataclass, we can create an instance of it
# * The dataclass works as a normal class, but with some special methods
x = Person('John', 50)
print(x)
# Person(name='John', age=50)


###############################################################################
# Dataclass Configuration (Representation)
###############################################################################


# Configuring Dataclass (Representation)
# * When defining a dataclass, we can configure some behaviors of the class
# * These configurations are set into the decorator as parameters
# * The `repr` parameter is used to configure if the class will implement the
#   representation method (__repr__)
@dataclass(repr=False)
class Person:
    name: str
    age: int


# Creating an instance of the Dataclass
# * When the representation is disabled, the object will not be shown when we
#   print it
x = Person('John', 50)
print(x)
# <__main__.Person object at ...>


###############################################################################
# Dataclass Configuration (Equality)
###############################################################################


# Configuring Dataclass (Equality)
# * The `eq` parameter is used to configure if the class will implement the
#   equality methods (__eq__, __ne__)
@dataclass(eq=False)
class Person:
    name: str
    age: int


# Comparing two instances of the Dataclass
# * When the equality is disabled, the object will not implement the __eq__
#   method
x = Person('John', 50)
y = Person('John', 50)
print(x == y)
# False


###############################################################################
# Dataclass Configuration (Ordering)
###############################################################################


# Configuring Dataclass (Ordering)
# * The `order` parameter is used to configure if the class will implement the
#   ordering methods (__lt__, __le__, __gt__, __ge__)
@dataclass(order=True)
class Value:
    value: int


# Comparing two instances of the Dataclass
# * Sinbce the ordering is enabled, the objects can be compared using the
#   comparison operators
x = Value(10)
y = Value(20)
print(x < y)
# True


###############################################################################
# Dataclass Configuration (Hash)
###############################################################################


# Configuring Dataclass (Safe Hash)
# * When defining a dataclass, the routine will automatically implement the
#   __hash__ method based on the `eq` and `frozen` parameters
# * Depending on the configuration, the object will implement the __hash__
#   method. If `frozen` is enabled, the object will always implement the
#   __hash__ method
@dataclass(frozen=True)
class Person:
    name: str
    age: int


# Accessing the __hash__ method
# * Since ``eq` or `frozen` are enabled, the object will implement the __hash__
#   method
x = Person('John', 50)
print(hash(x))
# 8730000000000


# Configuring Dataclass (Unsafe Hash)
# * The `unsafe_hash` parameter is used to force the implementation of the
#   __hash__ method
# * Even if `eq` or `frozen` are disabled, the object will implement the
#   __hash__ method if `unsafe_hash` is enabled
@dataclass(unsafe_hash=True)
class Person:
    name: str
    age: int


# Accessing the __hash__ method
# * Since the unsafe hash is enabled, the object will implement the __hash__
#   method
x = Person('John', 50)
print(hash(x))
# 8730000000000


###############################################################################
# Dataclass Configuration (Frozen)
###############################################################################


# Configuring Dataclass (Frozen)
# * The `frozen` parameter is used to configure if the object will be immutable
# * When the object is immutable, the fields cannot be changed after the object
#   is created
# * It also enables the __hash__ method
@dataclass(frozen=True)
class Person:
    name: str
    age: int


# Mutating the object
# * When the object is immutable, an error will be raised if we try to change
#   the fields
"""
x = Person('John', 50)
x.age = 60

dataclasses.FrozenInstanceError: cannot assign to field 'age'
"""


###############################################################################
# Dataclass Configuration (Match Arguments)
###############################################################################


# Configuring Dataclass (Match Arguments)
# * The `match_args` parameter is used to configure if the object will create
#   the __match_args__ method to be used by the match statement
# * This parameter is True by default
@dataclass(match_args=False)
class Person:
    name: str
    age: int


# Using the match statement
# * When the match_args is enabled, the object can be used in the match
#   statement
x = Person('John', 50)
match x:
    case Person(name='John', age=50):
        print('Matched')
    case _:
        print('Not matched')
# Matched


###############################################################################
# Dataclass Configuration (Keyword-Only Arguments)
###############################################################################


# Configuring Dataclass (Keyword-Only Arguments)
# * The `kw_only` parameter is used to configure if the object will accept only
#   keyword arguments in the constructor
# * This parameter is False by default
@dataclass(kw_only=True)
class Person:
    name: str
    age: int


# Creating an instance of the Dataclass
# * When the keyword-only arguments are enabled, we need to pass the arguments
#   as keywords in the constructor
x = Person(name='John', age=50)
print(x)
# Person(name='John', age=50)


###############################################################################
# Dataclass Configuration (Slots)
###############################################################################


# Configuring Dataclass (Slots)
# * The `slots` parameter is used to configure if the object will use slots
#   instead of a dictionary to store the attributes
# * This is useful to reduce the memory usage of the object
@dataclass(slots=True)
class Person:
    name: str
    age: int


# Accessing the __slots__ attribute
# * When the slots are enabled, the object will have the `__slots__` attribute,
#   and the `__dict__` attribute will not be available
x = Person('John', 50)
print(x.__slots__, hasattr(x, '__dict__'))
# ('name', 'age') False


###############################################################################
# Dataclass Configuration (Weakref Slot)
###############################################################################


# Configuring Dataclass (Weakref Slot)
# * The `weakref_slot` parameter is used to configure the `__slots__` to have
#   the `__weakref__` attribute
# * This is useful when we want to create weak references to the object using
#   the weakref module. If the `weakref_slot` is disable, the creation of weak
#   references by the weakref module will raise an error
# * It is mandatory to have the `slots` parameter enabled to use the
#   `weakref_slot`
@dataclass(slots=True, weakref_slot=True)
class Person:
    name: str
    age: int


# Checking if the weakref_slot is enabled
# * When the weakref_slot is enabled, the `__weakref__` attribute will be
#   present in the `__slots__` attribute
x = Person('John', 50)
print(x.__slots__)
# ('name', 'age', '__weakref__')


# Importing the weakref module
# * To create a weak reference to the object, we need to import the weakref
#   module
import weakref


# Creating a weak reference
# * When the `weakref_slot` is enabled for a dataclass, we can create weak
#   references to the object using the `weakref.ref` function
# * If the `weakref_slot` is disabled, an error will be raised
x = Person('John', 50)
y = weakref.ref(x)
print(y)
# <weakref at ...; to 'Person' at ...>


###############################################################################
# Field Configuration (Default)
###############################################################################


# Configuring Field (Default)
# * We can configure the fields of the dataclass using the `field` function
# * This function can be imported from the dataclasses module
# * This method allows us to set some configurations for the field, like the
#   default value
# * In the example below, we set the default value for the age field
@dataclass
class Person:
    name: str
    age: int = field(default=50)


# Creating an instance of the Dataclass
# * When a field has a default value, we can create an instance without
#   passing this field as a parameter
x = Person('John')
print(x)
# Person(name='John', age=50)


###############################################################################
# Field Configuration (Default Factory)
###############################################################################


# Configuring Field (Default Factory)
# * The `default_factory` parameter is used to set a function that will be
#   called to provide the default value for the field
# * In the example below, we set a lambda function to provide the default value
@dataclass
class Person:
    name: str
    age: int = field(default_factory=lambda: 50)


# Creating an instance of the Dataclass
# * When a field has a default factory, the function will be called to provide
#   the default value
x = Person('John')
print(x)
# Person(name='John', age=50)


# Configuring Field (Default Factory - Collections)
# * To determine the default value for a field as a collection, we can use the
#   `default_factory` parameter as well
# * In the example below, we set the default value as an empty list
@dataclass
class Person:
    name: str
    prefessions: list = field(default_factory=list)


# Creating an instance of the Dataclass
# * In this example, the professions field will be an empty list
x = Person('John')
print(x)
# Person(name='John', prefessions=[])


###############################################################################
# Field Configuration (Initialization)
###############################################################################


# Configuring Field (Initialization)
# * We can configure the field to not be initialized in the __init__ method
# * By default, all fields are initialized in the constructor
# * In this case, the field will not be present in the constructor
# * This behavior is useful when we want to compute the value of the field by
#   the `__post_init__` method
@dataclass
class Person:
    name: str
    age: int = field(init=False)


# Creating an instance of the Dataclass
# * When a field is not initialized, we need to set the value for it in the
#   class definition
# * NOTE: If the field is not set, an error will be raised since the dataclass
#   will not initialize it
x = Person('John')
x.age = 50
print(x)
# Person(name='John', age=50)


###############################################################################
# Field Configuration (Representation)
###############################################################################


# Configuring Field (Representation)
# * We can configure the field to not be present in the representation of the
#   object
# * By default, all fields are present in the representation
@dataclass
class Person:
    name: str
    age: int = field(repr=False)


# Creating an instance of the Dataclass
# * When a field is not present in the representation, it will not be shown
#   when we print the object
x = Person('John', 50)
print(x)
# Person(name='John')


###############################################################################
# Field Configuration (Hash Calculation)
###############################################################################


# Configuring Field (Hash Calculation)
# * We can configure the field to be used in the hash of the object
# * The parameter accepts three values: True: Explicitly include the field in
#   the hash calculation; False: Explicitly exclude the field from the hash
#   calculation; None: Use the default behavior, which typically includes the
#   field in the hash calculation unless the field is mutable (e.g., lists,
#   dictionaries)
# * In the example below, the field `age` would be used to calculate the hash,
#   however, we configured it to not be used
# * NOTE: To enable hash for the class, we set the `unsafe_hash` to True
@dataclass(unsafe_hash=True)
class Person:
    name: str
    age: int = field(hash=False)


# Creating an instance of the Dataclass
# * The age field will not be used to calculate the hash of the object
# * Even with different ages, the hash will be the same
x = Person('John', 50)
y = Person('John', 85)
print(hash(x), hash(y))
# 8730000000000 8730000000000


###############################################################################
# Field Configuration (Comparison)
###############################################################################


# Configuring Field (Comparison)
# * We can configure the field to be used in the comparison of the object
# * The comparison of the object can be done using the `==` operator, or by
#   using the `__eq__` method
# * The parameter accepts three values: True: Explicitly include the field in
#   the comparison; False: Explicitly exclude the field from the comparison;
#   None: Use the default behavior, which typically includes the field in the
#   comparison unless the field is mutable (e.g., lists, dictionaries)
# * In the example below, the field would not be used in the comparison
@dataclass
class Person:
    name: str
    age: int = field(compare=False)


# Comparing two instances of the Dataclass
# * We will create two instances of the dataclass to compare them
# * Even with different ages, the equality will be True
x = Person('John', 50)
y = Person('John', 85)
print(x == y)
# True


###############################################################################
# Field Configuration (Metadata)
###############################################################################


# Configuring Field (Metadata)
# * The `metadata` parameter is used to set some metadata for the field
# * The metadata is a dictionary which accepts any key-value pair
@dataclass
class Person:
    name: str
    age: int = field(metadata={'description': 'The age of the person'})


# Accessing metadata (from class)
# * To access the metadata, we can use the `fields` function from the
#   dataclasses module
x = fields(Person)
print(x[1].metadata)
# {'description': 'The age of the person'}


# Accessing metadata (from instance)
# * The same `fields` function can be used to access the metadata from an
#   instance
x = Person('John', 50)
y = fields(x)
print(y[1].metadata)
# {'description': 'The age of the person'}


###############################################################################
# Field Configuration (Keyword-Only Arguments)
###############################################################################


# Configuring Field (keyword-only)
# * The `kw_only` parameter is used to configure if the field will be a keyword
#   only argument in the constructor
# * This parameter is False by default
@dataclass
class Person:
    name: str
    age: int = field(kw_only=True)


# Creating an instance of the Dataclass
# * When some field is keyword-only, we need to pass it as a keyword in the
#   constructor
x = Person('John', age=50)
print(x)
# Person(name='John', age=50)


###############################################################################
# Class Variables
###############################################################################


# Importing ClassVar type
# * To define a class variable in a dataclass, we need to use the `ClassVar`
#   type from the typing module
from typing import ClassVar


# Defining a Class Variable
# * The class variable is shared between all instances of the class, instead of
#   being unique for each instance
# * This is one of the few cases where we need to use a type hint to define a
#   behavior
@dataclass
class Person:
    name: str
    age: int
    min_age: ClassVar[int] = 0


# Accessing the Class Variable
# * The class variable can be accessed using the class name
print(Person.min_age)
# 0


###############################################################################
# Post Init
###############################################################################


# Defining a Post Init Method
# * The `__post_init__` method is used to control the initialization of the
#   object
# * This is useful when we have some fields that are not initialized in the
#   constructor, and we need to compute the value of it
# * In this example, we will define a variable that will be computed after the
#   initialization of the object
@dataclass
class Person:
    name: str
    surname: str
    full_name: str = field(init=False)

    def __post_init__(self) -> None:
        self.full_name = f'{self.name} {self.surname}'


# Accessing the Computed Field
# * The full_name field will be computed after the object is created, and will
#   be available to access
x = Person('John', 'Doe')
print(x.full_name)
# John Doe
