"""
Operator Module

* The operator module exports a set of efficient functions corresponding to the
  intrinsic operators of Python. For example, operator.add(x, y) is equivalent
  to the expression `x + y`
* The table below shows the relation between the operator and the function in
  the operator module

###############################################################################
Operation               Syntax              Function
###############################################################################
Arithmetic Operations
###############################################################################
Addition                a + b               add(a, b)
Concatenation           seq1 + seq2         concat(seq1, seq2)
Containment Test        obj in seq          contains(seq, obj)
Division                a / b               truediv(a, b)
Floor Division          a // b              floordiv(a, b)
Bitwise And             a & b               and_(a, b)
Bitwise Exclusive Or    a ^ b               xor(a, b)
Bitwise Inversion       ~ a                 invert(a)
Bitwise Or              a | b               or_(a, b)
Exponentiation          a ** b              pow(a, b)
Identity                a is b              is_(a, b)
Not Identity            a is not b          is_not(a, b)
Indexed Assignment      obj[k] = v          setitem(obj, k, v)
Indexed Deletion        del obj[k]          delitem(obj, k)
Indexing                obj[k]              getitem(obj, k)
Left Shift              a << b              lshift(a, b)
Modulo                  a % b               mod(a, b)
Multiplication          a * b               mul(a, b)
Matrix Multiplication   a @ b               matmul(a, b)
Negation (Arithmetic)   - a                 neg(a)
Negation (Logical)      not a               not_(a)
Positive                + a                 pos(a)
Right Shift             a >> b              rshift(a, b)
Slice Assignment        seq[i:j] = values   setitem(seq, slice(i, j), values)
Slice Deletion          del seq[i:j]        delitem(seq, slice(i, j))
Slicing                 seq[i:j]            getitem(seq, slice(i, j))
String Formatting       s % obj             mod(s, obj)
Subtraction             a - b               sub(a, b)
Truth Test              obj                 truth(obj)
Ordering lt             a < b               lt(a, b)
Ordering le             a <= b              le(a, b)
Equality                a == b              eq(a, b)
Difference              a != b              ne(a, b)
Ordering ge             a >= b              ge(a, b)
Ordering gt             a > b               gt(a, b)
###############################################################################
In-place Operations
###############################################################################
Addition                a += b              iadd(a, b)
Concatenation           seq1 += seq2        iconcat(seq1, seq2)
Floor Division          a //= b             ifloordiv(a, b)
Modulo                  a %= b              imod(a, b)
Multiplication          a *= b              imul(a, b)
Matrix Multiplication   a @= b              imatmul(a, b)
Exponentiation          a **= b             ipow(a, b)
Subtraction             a -= b              isub(a, b)
True Division           a /= b              itruediv(a, b)
Floor Division          a //= b             ifloordiv(a, b)
Bitwise And             a &= b              iand(a, b)
Bitwise Or              a |= b              ior(a, b)
Left Shift              a <<= b             ilshift(a, b)
Right Shift             a >>= b             irshift(a, b)
###############################################################################
Lookup Operations
###############################################################################
Attribute Getter        obj.attr            attrgetter(attr)
Item Getter             obj[key]            itemgetter(key)
Method Caller           obj.method(*args)   methodcaller(method, *args)
###############################################################################
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
import operator as op


###############################################################################
# Operators
###############################################################################


# Using operator as argument
# * We can use the operator module to reference the intrinsic operators
# * This is useful when we want to pass an operator as a function argument
# * In the example below, we use the `reduce` function from the `functools`
#   module to sum all elements in a list
import functools
x = functools.reduce(op.add, [1, 2, 3])
print(x)
# 6


###############################################################################
# Lookup Objects
###############################################################################


# Attribute Getter
# * The `attrgetter` function returns a callable object that fetches the given
#   attribute(s) from its operand
# * The example below shows how to use the `attrgetter` function to fetch the
#   'name' attribute from a list of objects, and use it to sort the list
# * We used the `namedtuple` function to create a class that represents a
#   number with a 'value' attribute
# * Syntax: `attrgetter('attribute')`
from collections import namedtuple
Number = namedtuple('Number', 'value')
x = [Number(2), Number(1)]
x.sort(key=op.attrgetter('value'))
print(x)
# [Number(value=1), Number(value=2)]


# Item Getter
# * The `itemgetter` function returns a callable object that fetches the given
#   item(s) from its operand
# * The example below shows how to use the `itemgetter` function to fetch the
#   first element from a list of tuples, and use it to sort the list
# * Syntax: `itemgetter(index)`
x = [(2, 9), (1, 9)]
x.sort(key=op.itemgetter(0))
print(x)
# [(1, 9), (2, 9)]


# Method Caller
# * The `methodcaller` function returns a callable object that calls the given
#   method on its operand
# * The example below shows how to use the `methodcaller` function to call the
#   '__len__' method on a list of strings, and sort the list based on the
#   length of the strings
# * Syntax: `methodcaller('method', *args, **kwargs)`
x = ['aaa', 'a', 'aa']
x.sort(key=op.methodcaller('__len__'))
print(x)
# ['a', 'aa', 'aaa']
