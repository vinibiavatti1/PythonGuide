"""
Type class

* Type has't the first letter capitalized, but this is a class, not a function!
* if a single object is passed to type(), the function returns its type
* If three parameters are passed to type(), it returns a new class object
  (type will become a metaclass)
* Type is used as default as metaclass for created classes
* The isinstance() built-in function is recommended for testing the type of an
  object, because it takes subclasses into account

Syntax forms: type(object)
              type(name, bases, dict)

"""


# type(object)
# * In this way, type will just return the datetype of the parameter
type_1 = type(1)
type_2 = type(3.5)
type_3 = type('Hello world')
print(type_1, type_2, type_3, sep=', ')
# <class 'int'>, <class 'float'>, <class 'str'>
print()


# type(name, bases, dict)
# * The use case for type(name, bases, dict) is when you want to dynamically
#   generate classes at runtime (type as metaclass)
class Animal():
    pass


clz = type('Horse', (Animal,), {'name': "Sansão"})
print(clz)
# <class '__main__.Horse'>


# The type of the type
print(type(type))
# <class 'type'> This is a class, not a function
