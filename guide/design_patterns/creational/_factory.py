"""
Factory

* In Factory pattern, we create object without exposing the creation logic to
  the client and refer to newly created object using a common interface
"""


# Rect shape
class Retangle:
    pass


# Circ shape
class Circle:
    pass


# Factory to create shapes
class ShapeFactory:
    def create_from_name(self, name):
        if name == 'rect':
            return Retangle()
        elif name == 'circ':
            return Circle()
        else:
            return None


# Algorithm
name = 'rect'
factory = ShapeFactory()
shape = factory.create_from_name(name)
print(type(shape))
# <class '__main__.Retangle'>
