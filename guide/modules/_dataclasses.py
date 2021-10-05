"""
Dataclasses (PEP 557)

* This module provides a decorator and functions for automatically adding
  generated special methods such as __init__() and __repr__() to user-defined
  classes. It was originally described in PEP 557
* To use dataclasses resources, the module dataclasses must be imported
"""
from dataclasses import (
    dataclass,
    field,
    InitVar,
)


###############################################################################
# Dataclass
###############################################################################


# Dataclass decorator
# * The dataclass decorator is used to mark some class as dataclass, giving to
#   this class pre configurations set for the fields, and some auto generated
#   methods
# * For dataclasses, the fields are defined as classfields. These class fields
#   will be used to create the class structure
@dataclass
class Person:
    name: str
    age: int


# Dataclass instance
# * The dataclass already defines a contructor and other methods
person = Person('Vini', 27)
print(repr(person))
# Person(name='Vini', age=27)


###############################################################################
# Fields Configuration
###############################################################################


# Field method
# * We can set some configuratons for the fields, to control the usage of it.
#   For example, we can determinate if the field will be present in the
#   contructor, or set the default value for this
@dataclass
class People:
    name: str
    age: int = field(default=18, kw_only=True)
    identifier: int = field(init=False, default=0)
    other: str = field(init=False, default='', repr=False)


# Instance
# * The instance of the above class would be:
people_1 = People('Vini', age=28)
people_2 = People('Ana')
print(people_1, people_2, sep="\n")
# People(name='Vini', age=28, identifier=0)
# People(name='Ana', age=18, identifier=0)


###############################################################################
# Init-Only Variables
###############################################################################


# InitVar
# * If a field is an InitVar, it is considered a pseudo-field called an
#   init-only field
# * it is not returned by the module-level fields() function
# * Init-only fields are added as parameters to the generated __init__() method
#   and are passed to the optional __post_init__() method. They are not
#   otherwise used by dataclasses.
@dataclass
class Vehicle:
    name: str
    generate_id: InitVar[bool] = False
    id: str = field(default=None, kw_only=True)

    # __post_init__ magic methos is used for this case. All of the InitVar
    # variables are passed as arguments for this method, and can used to
    # control the initialization of the object
    def __post_init__(self, generate_id: bool) -> None:
        if generate_id:
            self.id = 'random'


# Instance
# * The instance of the above class would be:
vehicle_1 = Vehicle('Cruze', id='001')
vehicle_2 = Vehicle('Focus', generate_id=True)
print(vehicle_1, vehicle_2, sep="\n")
# Vehicle(name='Cruze', id='001')
# Vehicle(name='Focus', id='random')
