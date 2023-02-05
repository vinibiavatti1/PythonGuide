"""
Protocols

* Protocols (interfaces) in Python are a set of methods that when implemented
  to a class, the class receives some additional behavior
* The additional behaviors usually work to a specific situation
* If the class does't support the behavior for the situation, an exception will
  be raised
* To check if the class implements some protocol, we must check the methods
  that are implemented. This is called (duck typing)
* It is not mandatory to implement all the methods of a protocol to gives to
  the class some custom behavior
* In the list below, we can find a documentation for each Python protocol
* NOTE: The list contains only the standard Python protocols

###############################################################################
Magic Methods                       Trigger(s)
###############################################################################
NOTE: The "x" variable is considered the object that implements the protocol

Arithmetic Operations Protocol
__add__(self, other)                x + y
__sub__(self, other)                x - y
__mul__(self, other)                x * y
__matmul__(self, other)             x @ y
__truediv__(self, other)            x / y
__floordiv__(self, other)           x // y
__mod__(self, other)                x % y
__pow__(self, other[, module])      x ** y, pow(x, y)
__lshift__(self, other)             x << y
__rshift__(self, other)             x >> y
__and__(self, other)                x & y
__xor__(self, other)                x ^ y
__or__(self, other)                 x | y
__divmod__(self, other)             divmod(x, y)

Arithmetic Operations Protocol (Reflected)
__radd__(self, other)               y + x
__rsub__(self, other)               y - x
__rmul__(self, other)               y * x
__rmatmul__(self, other)            y @ x
__rtruediv__(self, other)           y / x
__rfloordiv__(self, other)          y // x
__rmod__(self, other)               y % x
__rpow__(self, other[, modulo])     y ** x, pow(y, x)
__rlshift__(self, other)            y << x
__rrshift__(self, other)            y >> x
__rand__(self, other)               y & x
__rxor__(self, other)               y ^ x
__ror__(self, other)                y | x
__rdivmod__(self, other)            divmod(y, x)

Arithmetic Operations Protocol (Assignments)
__iadd__(self, other)               x += y
__isub__(self, other)               x -= y
__imul__(self, other)               x *= y
__imatmul__(self, other)            x @= y
__itruediv__(self, other)           x /= y
__ifloordiv__(self, other)          x //= y
__imod__(self, other)               x %= y
__ipow__(self, other[, modulo])     x **= y
__ilshift__(self, other)            x <<= y
__irshift__(self, other)            x >>= y
__iand__(self, other)               x &= y
__ixor__(self, other)               x ^= y
__ior__(self, other)                x |= y

Arithmetic Operations Protocol (Unary)
__neg__(self)                       -x
__pos__(self)                       +x
__invert__(self)                    ~x
__abs__(self)                       abs(x)

Arithmetic Operations Protocol (Casting)
__complex__(self)                   complex(x)
__int__(self)                       int(x)
__float__(self)                     float(x)
__index__(self)                     y[x], bin(x), hex(x), oct(x)

Arithmetic Operations Protocol (Truncating)
__round__(self[, ndigits])          round(x, y)
__trunc__(self)                     math.trunc(x)
__floor__(self)                     math.floor(x)
__ceil__(self)                      math.ceil(x)

Attribute Access Protocol
__getattr__(self, name)             x.attr (Called when attr not found)
__getattribute__(self, name)        x.attr
__setattr__(self, name, value)      x.attr = y
__delattr__(self, name)             del x.attr

Awaitable Protocol
__await__(self)                     await MyClass()

Boolean Protocol
__bool__(self)                      bool(x)

Bytes Protocol
__bytes__(self)                     bytes(x)

Callable Protocol
__call__(self, ...)                 x(), x(args)

Class Creation Protocol (Used for Meta Programming)
__init_subclass__(cls)              class MyClass(Subclass):
__prepare__(name, bases, **kwds)    class MyClass(metaclass=Metaclass):

Class Pattern Matching Protocol
__match_args__                      match x: case MyClass(args):

Container Protocol
__len__(self)                       len(x)
__length_hint__(self)               len(x) (Estimated length)
__getitem__(self, key)              x[key]
__setitem__(self, key, value)       x[key] = y
__delitem__(self, key)              del x[key]
__missing__(self, key)              x[key] (When key not found)
__reversed__(self)                  reversed(x)
__contains__(self, item)            y in x

Copy Protocol
__copy__(self)                      copy.copy(x)
__deepcopy__(self, memodict={})     copy.deepcopy(x)

Context Manager Protocol
__enter__(self)                     with x:
__exit__(self, et, ev, traceback)   end of with block

Descriptor Protocol
__get__(self, instance, owner=None) x.attr
__set__(self, instance, value)      x.attr = y
__delete__(self, instance)          del x.attr
__set_name__(self, owner, name)     class MyClass: x = Descriptor()

Directory Protocol
__dir__(self)                       dir(x)

Format Protocol
__format__(self, format_spec)       format(x, y), x.format(y)

Generic Types Protocol (Used for Type hints)
__class_getitem__(cls, key)         x: MyClass[key] = ...

Hashable Protocol
__hash__(self)                      hash(x)

Instance Check Protocol
__instancecheck__(self, instance)   isinstance(x, y)
__subclasscheck__(self, subclass)   issubclass(x, y)

Instance Creation Protocol
__new__(cls, ...)                   x = MyClass()  # Before Creation
__init__(self, ...)                 x = MyClass()  # After Creation
__del__(self)                       Called by GC (Garbage Collector)

Iterator Protocol
__iter__(self)                      iter(x), for y in x:
__next__(self)                      next(x), for y in x: (Cycle)

Iterator Protocol (Asynchronous)
__aiter__(self)                     async iter(x), async for y in x:
__anext__(self)                     async next(x), async for y in x: (cycle)

Pickle Protocol
__getnewargs_ex__(self)             pickle.dump(pkl_file, x, protocol=2)
__getnewargs__(self)                pickle.dump(pkl_file, x, protocol=2)
__getstate__(self)                  pickle.dump(pkl_file, x)
__setstate__(self, state)           data = pickle.load(pkl_file)
__reduce__(self)                    pickle.dumps(x)
__reduce_ex__(self, protocol)       pickle.dumps(x)

Representation Protocol
__repr__(self)                      repr(x)

Rich Comparison Protocol
__lt__(self, other)                 x < y
__le__(self, other)                 x <= y
__eq__(self, other)                 x == y
__ne__(self, other)                 x != y
__gt__(self, other)                 x >= y
__ge__(self, other)                 x > y

String Protocol
__str__(self)                       str(x), print(x), format(x, y)
###############################################################################
"""


###############################################################################
# Protocol Implementation
###############################################################################


# Declaring a class with protocol implementation
# * Since Python follows the concept of duck type programming, there aren't
#   pre-defined interfaces that can be used as a template for some protocol. To
#   implement a protocol, we just need to add the method to our class
# * In this example, the class bellow implements the following protocols:
#   * Instance Creation Protocol
#   * String Protocol
#   * Arithmetic Operations Protocol
#   * Rich Comparison Protocol
class MyClass:

    def __init__(self, val) -> None:
        self.val = val

    def __str__(self):
        return f'Val: {self.val}'

    def __add__(self, other):
        return self.val + other.val

    def __lt__(self, other):
        return self.val < other.val


# Using the protocol behaviors implemented in our class
# * Here, there are some examples of the usage of the implemented protocol
#   methods
x = MyClass(3)
y = MyClass(7)
print(str(x))
print(x + y)
print(x < y)
# Val: 3
# 10
# True
