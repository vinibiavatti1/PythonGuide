"""
Magic methods

* Magic methods are not meant to be invoked directly by you, but the invocation
  happens internally from the class on a certain action
* It is also called as "Dunder Methods" (Double Underscores Methods)
* The methods are implemented or overrided in classes
* Example of magic method: __init__()

* Rszalski article: https://rszalski.github.io/magicmethods/
* Tutorialsteacher: https://www.tutorialsteacher.com/python/magic-methods-in-py
                    thon

-------------------------------------------------------------------------------
Magic Method	                    Called when
-------------------------------------------------------------------------------
* NOTE: x represents the object with magic methods

Construction and Initialization
__new__(cls [,...])	                x = MyClass(arg1, arg2)
__init__(self [,...])	            x = MyClass(arg1, arg2)
__del__(self)                       called when an object is GC

Attribute access
__getattr__(self, name)	            self.name  # name doesn't exist
__setattr__(self, name, val)	    self.name = val
__delattr__(self, name)	            del self.name
__getattribute__(self, name)	    self.name

Comparison
__cmp__(self, other)                All bellow operations
__eq__(self, other)	                x == y
__ne__(self, other)	                x != y
__lt__(self, other)	                x < y
__le__(self, other)	                x <= y
__gt__(self, other)                 x > y
__ge__(self, other)	                x >= y

Unary operators
__pos__(self)	                    +x
__neg__(self)	                    -x
__invert__(self)	                ~x

Normal arithmetic operators
__add__(self, other)	            x + y
__sub__(self, other)	            x - y
__mul__(self, other)	            x * y
__floordiv__(self, other)	        x // y
__div__(self, other)	            x / y
__mod__(self, other)	            x % y
__pow__(self, other[, modulo])	    x ** y
__lshift__(self, other)             x << y
__rshift__(self, other)             x >> y
__and__(self, other)                x & y
__or__(self, other)                 x | y
__xor__(self, other)                x ^ y

Reflected arithmetic operators
__radd__(self, other)	            y + x
__rsub__(self, other)	            y - x
__rmul__(self, other)	            y * x
__rfloordiv__(self, other)	        y // x
__rdiv__(self, other)	            y / x
__rmod__(self, other)	            y % x
__rpow__(self, other[, modulo])	    y ** x
__rlshift__(self, other)            y << x
__rrshift__(self, other)            y >> x
__rand__(self, other)               y & x
__ror__(self, other)                y | x
__rxor__(self, other)               y ^ x

Augmented assignment
__iadd__(self, other)	            x += y
__isub__(self, other)	            x -= y
__imul__(self, other)	            x *= y
__ifloordiv__(self, other)	        x //= y
__idiv__(self, other)	            x /= y
__imod__(self, other)	            x %= y
__ipow__(self, other)	            x **= y
__ilshift__(self, other)	        x <<= y
__irshift__(self, other)	        x >>= y
__iand__(self, other)	            x &= y
__ior__(self, other)	            x |= y
__ixor__(self, other)	            x ^= y

Type conversion
__str__(self)	                    str(x)
__bool__(self)	                    bool(x)
__int__(self)	                    int(x)
__float__(self)	                    float(x)
__complex__(self)	                complex(x)
__oct__(self)	                    oct(x)
__hex__(self)	                    hex(x)

Functions
__abs__(self)	                    abs(x)
__round__(self, other)	            round(x)
__floor__(self)	                    math.floor(x)
__ceil__(self)                      math.ceil(x)
__trunc__(self)	                    math.trunc(x)
__divmod__(self, other)             divmod(x)
__repr__(self)	                    repr(x)
__unicode__(self)	                unicode(x)
__format__(self, formatstr)	        x.format()
__hash__(self)	                    hash(x)
__dir__(self)	                    dir(x)
__sizeof__(self)	                sys.getsizeof(x)
__len__(self)                       len(x)
__reversed__(self)                  reversed(x)

Containers control
__getitem__(self, key)	            x[y]
__setitem__(self, key, val)	        x[y] = z
__delitem__(self, key)	            del x[y]
__iter__(self)	                    for value in x
__contains__(self, item)            y in x
__missing__(self, key)              y in x
__index__(self)	                    lst[x]

Callable control
__call__(self [,...])	            x(args)

Copying
__copy__(self)                      copy.copy(x)
__deepcopy__(self, memodict={})     copy.deepcopy(x)

Context Managers
__enter__(self)	                    with x as element:
__exit__(self, exc, val, trace)	    with x as element:

Reflection
__instancecheck__(self, instance)   isinstance(x, y)
__subclasscheck__(self, subclass)   issubclass(x, y)

Pickling
__getnewargs__(self)                pickle.dump(pkl_file, x, protocol=2)
__getstate__(self)                  pickle.dump(pkl_file, x)
__setstate__(self, state)           data = pickle.load(pkl_file)
__reduce__(self)                    pickle.dumps(x)
__reduce_ex__(self)                 pickle.dumps(x)
-------------------------------------------------------------------------------
"""


# Defining magic method
class MagicClass:
    def __init__(self, val):
        self.val = val

    def __gt__(self, other):
        return self.val > other


# Using magic method
mc = MagicClass(5)
print(mc > 4, mc > 6, sep=', ')
# True, False
