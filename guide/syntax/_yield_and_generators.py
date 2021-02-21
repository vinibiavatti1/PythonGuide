"""
Yield and Generators

Yield
* Is used to define a function as a generator
* It is like return, but the cursor will stop in the yield position waiting for
  the next() function
* The function continues execution immediately after the last yield run

Generators
* Can be created with yield and with list comprehension using () parentheses
* The major difference between a list comprehension and a generator expression
  is that a list comprehension produces the entire list while the generator
  expression produces one item at a time
"""


# -----------------------------------------------------------------------------
# Yield Generators


# Simple yield generator
def gen1():
    yield 1
    yield 2


gen = gen1()
print(next(gen))
print(next(gen))
# print(next(gen))  StopIteration


# Iterate yield generator with for
def squares(start=1, end=10):
    while start != end:
        yield start * start
        start += 1


for square in squares():
    print(square, end=', ')
    # 1, 4, 9, 16, 25, 36, 49, 64, 81,
print()


# Iterate yield generator with next
squares_generator = squares(5, 7)
print(next(squares_generator))
print(next(squares_generator))
# print(next(squares_generator))  StopIteration


# -----------------------------------------------------------------------------
# Generators


# Simple generator
gen = (i for i in range(1, 3))
print(next(gen))
print(next(gen))
# print(next(gen))  StopIteration


# Iterate generator with for
squares = (i*i for i in range(1, 10))
for square in squares:
    print(square, end=', ')
    # 1, 4, 9, 16, 25, 36, 49, 64, 81,
print()


# Iterate generator with next
squares_generator = (i*i for i in range(5, 7))
print(next(squares_generator))
print(next(squares_generator))
# print(next(squares_generator))  StopIteration
