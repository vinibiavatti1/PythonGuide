"""
Type class

* Type has't the first letter capitalized, but this is a class, not a function!

The type() class has two different forms:
 - type(object)
 - type(name, bases, dict)

if a single object is passed to type(), the function returns its type.
If three parameters are passed to type(), it returns a new class object (type will become a metaclass).
"""
# type(object)
# In this way, type will just return the datetype of the parameter
type_1 = type(1)
type_2 = type(3.5)
type_3 = type('Hello world')
print(type_1, type_2, type_3, sep=', ') # <class 'int'>, <class 'float'>, <class 'str'>
print()

# type(name, bases, dict)
# The use case for type(name, bases, dict) is when you want to dynamically generate classes at runtime (type as metaclass)
class Animal():
    pass
clz = type('Horse', (Animal,), {'name': "Sansão"}) # Horse class is generated at runtime
print(clz) # <class '__main__.Horse'>

# The type of the type
print(type(type)) # <class 'type'> This is a class, not a function
def fn(): pass
print(type(fn)) # <class 'function'>