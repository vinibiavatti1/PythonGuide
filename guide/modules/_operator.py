"""
Operator module

* The operator module exports a set of efficient functions corresponding to the
  intrinsic operators of Python. For example, operator.add(x, y) is equivalent
  to the expression x+y
* This table shows how abstract operations correspond to operator symbols in
  the Python syntax and the functions in the operator module:

###############################################################################
Operation               Syntax              Function
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
"""
import operator as op


# Common return functions
print(op.add(1, 2))  # 3
print(op.concat('a', 'b'))  # ab
print(op.contains('abc', 'b'))  # True
print(op.truediv(5, 3))  # 1.666...
print(op.floordiv(5, 3))  # 1
print(op.and_(7, 5))  # 5
print(op.xor(7, 5))  # 2
print(op.invert(1))  # -2
print(op.or_(7, 5))  # 7
print(op.pow(2, 3))  # 8
print(op.is_(None, None))  # True
print(op.is_not(None, None))  # False
print(op.lshift(1, 1))  # 2
print(op.mod(5, 3))  # 2
print(op.mul(3, 3))  # 9
print(op.neg(1))  # -1
print(op.not_(1))  # False
print(op.pos(-1))  #
print(op.rshift(8, 1))  # 4
print(op.mod('number: %s', 5))  # number: 5
print(op.sub(5, 3))  # 2
print(op.truth(5))  # True
print(op.lt(2, 3))  # True
print(op.le(2, 2))  # True
print(op.eq(1, 1))  # True
print(op.ne(1, 1))  # False
print(op.ge(2, 2))  # True
print(op.gt(3, 1))  # True


# Object manipulation functions
obj = {'name': 'Vini'}
op.setitem(obj, 'age', 27)
op.delitem(obj, 'name')
age = op.getitem(obj, 'age')
print(age, obj)  # 27 {'age': 27}


# Collection manipulation functions
lst = [1, 2, 3, 4, 5]
op.setitem(lst, slice(5, 6), [6, 7])
op.delitem(lst, slice(0, 2))
items = op.getitem(lst, slice(2, 7))
print(items, lst)  # [5, 6, 7] [3, 4, 5, 6, 7]


# Matrix Multiplication
# NOTE: Check _matrix_multiplication.py
