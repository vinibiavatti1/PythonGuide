"""
Named Tuple

* Returns a new tuple subclass named typename
* The function use type() function to create a class at runtime
* Used to define a specified object to be create as a tuple with attributes

* Parameters
  * typename: This is the name of the namedtuple object
  * field_names: This is the second argument to define the field names in the
    namedtuple. We can define them using following formats – 'name age role',
    'name,age,role', or ['name', 'age', 'role'].
  * rename: We can specify rename to True so that invalid fields are renamed to
    their index names. For example, 'name def class' will be renamed to
    'name', '_1', '_2'.
  * defaults: It's used to define default values to the optional parameters.
    Since fields with a default value must come after any fields without a
    default, the defaults are applied to the rightmost parameters. For example,
    if the fieldnames are ['a', 'b', 'c'] and the defaults are (1, 2), then 'a'
    will be a required argument, ‘b' will default to 1, and ‘c' will default to
    2.
  * module: If module is defined, the __module__ attribute of the named tuple
    is set to that value. This parameter was introduced in Python 3.6 release

* Syntax
  * namedtuple(typename, field_names, *, rename, defaults, module)
"""
import collections


# Create with str (Access by index)
Person = collections.namedtuple('Person', 'name, age')
person = Person(name='Vini', age=16)
print(person[0], person[1], sep=', ')
# Vini, 16


# Create with list (Access by name)
Point = collections.namedtuple('Point', ['x', 'y'])
point = Point(x=8, y=14)
print(point.x, point.y, sep=', ')
# 8, 14


# Make
Point = collections.namedtuple('Point', ['x', 'y'])
attributes = [10, 20]
point = Point._make(attributes)
print(point.x, point.y, sep=', ')
# 10, 20


# As dict
Point = collections.namedtuple('Point', ['x', 'y'])
point = Point(x=8, y=14)
print(point._asdict())
# {'x': 8, 'y': 14}


# Rename
Point = collections.namedtuple('Point', ['class', 'def'], rename=True)
print(Point._fields)
# ('_0', '_1')


# Defaults
Point = collections.namedtuple('Point', ['x', 'y'], defaults=[1, 1])
point = Point()
print(point)
# Point(x=1, y=1)
