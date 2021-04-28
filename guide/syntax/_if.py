"""
if

* Tool to create conditions
* Python supports the usual logical conditions from mathematics:
  * Equals: a == b
  * Not Equals: a != b
  * Less than: a < b
  * Less than or equal to: a <= b
  * Greater than: a > b
  * Greater than or equal to: a >= b
* Python supports chained conditions too:
  * Example: y1 < x < y2
"""


###############################################################################
# Conditions
###############################################################################


# if
x = 5
if x > 3:
    print('Grater')
# Grater


# if in
x = 1
if x in (1, 2, 3):
    print(f'{x} is inside the tuple')
# 1 is inside the tuple


# if is
x = None
if x is None:
    print(f'{x} is None')
# None is None


# if is
x = None
if x is None:
    print(f'{x} is None')
# None is None


# if and
x = 5
if x > 0 and x < 10:
    print(f'{x} is inside the range 0 - 10')
# 5 is inside the range 0 - 10


# if or
x = 5
if x == 0 or x == 5:
    print(f'{x} is 0 or 5')
# 5 is 0 or 5


# if not
x = 10
y = 20
if not x == y:
    print(f'{x} is not equal to {y}')
# 10 is not equal to 20


# if else
x = True
if x:
    print('good')
else:
    print('bad')
# good


# if elif else
x = 3
if x == 1:
    print('one')
elif x == 2:
    print('two')
else:
    print('three')
# three


# if (short hand)
# * NOTE: (PEP8 NOT RECOMENDED)
x = 'a'
if x == 'a': print(True)  # Same line
# True


# if (ternary)
# * NOTE: It needs the else statement always!
x = 'b'
print('a') if x == 'a' else print('b')
# b


# if (tuple ternary)
x = True
y = ('no', 'yes')[x]
print(y)
# yes


# if (chained)
x = 5
if 0 <= x <= 10:
    print(f'{x} is inside range 0 - 10')
# 5 is inside range 0 - 10
