"""
Generators

* Generators in Python can be created in two ways:
  * Generator Functions, by using the "yield" instruction
  * Comprehension Generator, by using the comprehension syntax

Generator Functions (Yield)
* the "yield" instruction is used to declare a function as a generator
* It is like return, but the cursor will stop in the yield position waiting for
  the next() function
* The function continues the execution immediately after the last yield run

Comprehension Generators
* Can be created using parentheses "()" with the comprehension syntax
* The major difference between a list comprehension and a generator expression
  is that a list comprehension produces the entire list while the generator
  expression produces an item only when it is required

Generators vs Collections (Advantages)
* Memory efficiency: Generators generate values one at a time, and don't store
  all values in memory like a list
* Speed: Generators are faster than lists
* Laziness: Generators are lazy, meaning that they only generate values when
  they are needed
"""


###############################################################################
# Generators Functions (Yield)
###############################################################################


# Declare a generator function
# * Any function that contains the yield keyword is a generator function
# * A generator function is a function that generates data for each iteration
# * In a generator function, the cursor will stop at the first "yield"
#   instruction, and will be there until the generator be called with the
#   "next()" function
# * The function below will generate a sequence of [1, 2, 3]
def generator():
    yield 1
    yield 2
    yield 3


# Call a generator function
# * When the generator function is called, it will return a generator object
# * The generator object can be processed by the "next()" function to retain
#   the generated values
generator_object = generator()
x = next(generator_object)
y = next(generator_object)
z = next(generator_object)
print(x, y, z)
# 1 2 3


# Iterate a generator function with "for" loop
# * The "for" loop can be used to iterate over a generator
# * The generator object does not need to be get before "for" call, since the
#   instruction already knows how to handle generators
# * The range() function is an example of a generator
for value in generator():
    print(value, end=' ')
print()
# 1 2 3


# Declare a custom range generator function
# * The implementation below is similar to the implementation of the native
#   "range()" function (but simpler)
# * The reason to use a generator function for this is that we don't need to
#   allocate all data to memory, since the data will be create at runtime for
#   each iteration
def _range(end):
    x = 0
    while x < end:
        yield x
        x += 1


# Call the custom range generator function
# * The example below is the call to the function above
# * The for was used to iterate all generated data
for value in _range(5):
    print(value, end=' ')
print()
# 0 1 2 3 4


###############################################################################
# Stop Iteration Exception
###############################################################################


# Raise a StopIteration exception
# * The StopIteration exception is raised when the end of an iterator is
#   reached. It signals that there are no more elements to be returned by the
#   iterator
# * A "try except" block can be used to handle this exception
# * The example below shows the exception (commented to don't stop the code
#   execution)
"""
generator_object = generator()
next(generator_object)
next(generator_object)
next(generator_object)
next(generator_object)  # Raises StopIteration

Traceback (most recent call last):
  File "_yield_and_generators.py" in <module>
    next(generator_object)
StopIteration
"""


# Handle a StopIteration exception
# * To handle the StopIteration exception, we can use a "try except" block
# * NOTE: The "for" loop already handles the exception and it does not need to
#   be handled manually
generator_object = generator()
try:
    print(next(generator_object), end=' ')
    print(next(generator_object), end=' ')
    print(next(generator_object), end=' ')
    print(next(generator_object), end=' ')  # Raises StopIteration
except StopIteration:
    print('Generation Finished')
# 1 2 3 Generation Finished


###############################################################################
# Generators with Comprehension
###############################################################################


# Declare a generator with the comprehension syntax
# * The "()" parenthesis are used to declare a generator
# * The generator created with the comprehension syntax cannot be restored.
#   Once the generator has been exhausted, it cannot be restarted.
# * NOTE: A tuple with a single element should be defined with a comma as
#   mandatory, otherwise, a generator will be created instead!
#   Example: collection = (1,)
inline_generator = (x for x in range(1, 4))


# Call a generator create with a comprehension syntax
# * Generators created using the comprehension syntax does not need to be
#   instantiated first to be used
# * The comprehension generators are already the generator object
x = next(inline_generator)
y = next(inline_generator)
z = next(inline_generator)
print(x, y, z)
# 1 2 3


# Handle a StopIteration exception from inline generator
# * To handle the StopIteration exception of a comprehension generator, the
#   "try except" block can be used as the same way of function generators
# * In the example below, the "next()" function call for the "inline_generator"
#   will raise the exception cause the generator is already initialized in the
#   example above
try:
    print(next(inline_generator), end=' ')  # Raises StopIteration
except StopIteration:
    print('Generation Finished')
# 1 2 3 Generation Finished


# Comprehension generator as argument
# * The comprehension generator syntax can be used as argument for a function
#   that accepts generator data
# * As arguments, the parenthesis "()" are not required
# * The example below will result to: (0 + 1 + 2 + 3 = 6)
result = sum(x for x in range(4))
print(result)
# 6


# Iterate a comprehension generator
# * The "for" also works to comprehension generators
inline_generator = (x for x in range(1, 4))
for value in inline_generator:
    print(value, end=' ')
print()
# 1 2 3


###############################################################################
# Yield From
###############################################################################


# Create a generator with the "yield from" syntax
# * The "yield from" statement in Python is used when a generator function uses
#   other generator inside (a generator uses other generator)
# * It is used to simplify the code and make it more readable
# * The example below declares a generator function that uses the generator
#   created at the beginning of this module
def other_generator():
    yield from generator()


# Call a generator that uses "yield from" syntax
# * The "other_generator" function will act as the same of the "generator"
#   function
# * The "yield from" syntax is used only to simplify the code inside
generator_object = other_generator()
x = next(generator_object)
y = next(generator_object)
z = next(generator_object)
print(x, y, z)
# 1 2 3


# Example without using the "yield from" syntax
# * The function below will have the same behavior of the "other_generator"
#   function, without using the "yield from" syntax
def another_generator():
    for x in generator():
        yield x


# Call a generator that doesn't use "yield from" syntax
# * The example below will produces the same result of the "other_generator"
#   function
generator_object = another_generator()
x = next(generator_object)
y = next(generator_object)
z = next(generator_object)
print(x, y, z)
# 1 2 3
