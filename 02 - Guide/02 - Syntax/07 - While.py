"""
While

* The "while" instruction is used to create a loop by a condition
* When the condition is true, the loop will be performed
* It can be used to iterate collections, create a simple loop, read threads,
  etc.
* It is recommended to use the "for" instruction to iterate collections
* Syntax: while <condition>:
"""


###############################################################################
# While Loop
###############################################################################


# Create a while loop
# * To create a simple loop, we can use the while instruction
# * The loop will be stopped when the condition of the while gets False
x = 0
while x <= 5:
    print(x, end=' ')
    x += 1
print()
# 0 1 2 3 4 5


# Create a while loop with multiple conditions
# * Like the "if" instruction, the while can receive multiple conditions to
#   check if the loop should be performed or not
x = 0
y = 5
while x < 10 and y > 0:
    print(x, y, end=' ')
    x += 1
    y -= 1
print()
# 0 5 1 4 2 3 3 2 4 1


# Create a while loop to iterate a collection
# * The while instruction can be used to iterate a collection
# * The "for" instruction is preferred since the "for" will work with each
#   element of the collection, since the "while" will need a manual index to
#   to select each element from the collection
collection = [1, 2, 3, 4, 5]
index = 0
while index < len(collection):
    print(collection[index], end=' ')
    index += 1
print()
# 1 2 3 4 5


# Create a while infinite loop
# * To create a infinite loop, we can just add the True value to the condition
# * Take care when creating while loops. If you make a mistake, the loop can
#   become infinite and the application will stop to work.
# * Infinite loops are useful to observe threads, events, etc.
"""
while True:
    ...
"""


###############################################################################
# While Loop with Else
###############################################################################


# Create a while loop with else
# * Python has a additional curious syntax. It is the "else" that can also be
#   used to "while" loops.
# * The else block in a while expression is always be executed after the loop
#   terminates normally (without a break)
# * It can be useful to ensure that some code will be performed only if the
#   loop is executed
x = 0
while x < 5:
    print(x, end=' ')
    x += 1
else:
    print('done')
# 0 1 2 3 4 done
