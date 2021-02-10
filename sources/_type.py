"""
Type keyword

The type() function has two different forms:
 - type(object)
 - type(name, bases, dict)

if a single object is passed to type(), the function returns its type.
If three parameters are passed to type(), it returns a new type object.
"""
# type(object)
# In this way, type will just return the datetype of the parameter
type_1 = type(1)
type_2 = type(3.5)
type_3 = type('Hello world')
print(type_1, type_2, type_3, sep='\n')

# type(name, bases, dict)
# The use case for type(name, bases, dict) is when you want to dynamically generate classes at runtime
class Animal():
    pass
clz = type('Horse', (Animal,), {'name': "Sansão"}) # Horse class is generated at runtime
print(clz)