"""
If
"""


# If
x = 5
if x > 3:
    print('>')
    # >


# If in
tpl = (1, 2, 3)
if 1 in tpl:
    print('in')
    # in


# If is
x = []
y = []
if x is not y:
    print('is not')
    # is not


# If not
x = 10
y = 20
if not x == y:
    print('not equal')
    # not equal


# If with logical operators
x = 10
y = 5
if x == 10 and y > 3:
    print(True)
    # True


# If else
x = True
if x:
    print('good')
    # good
else:
    print('bad')


# If elif else
x = 3
if x == 1:
    print('one')
elif x == 2:
    print('two')
else:
    print('three')
    # three


# If Short hand (PEP8 NOT RECOMENDED)
x = 'a'
if x == 'a': print(True)  # Same line


# Ternary if
# NOTE: It needs the else statement!
x = 'b'
print('a') if x == 'a' else print('b')
# b


x = True
y = 'yes' if x else 'no'
print(y)
# yes


# If ternaty (with tuple)
x = True
y = ('no', 'yes')[x]
print(y)
# yes
