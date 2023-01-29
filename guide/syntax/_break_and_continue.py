"""
Break and Continue

* Break is an instruction used to interrupt a loop (for or while)
* Continue is an instruction used to process the next cycle of a loop (for or
  while)
* When the loop is interrupted by a break, the else block will not be performed
"""


###############################################################################
# Break
###############################################################################


# Break a while loop
# * The break keyword stops the iteration of the loop
# * In the example, when the variable x gets the 5 value, the loop will be
#   interrupted
x = 0
while x < 10:
    print(x, end=' ')
    if x == 5:
        break
    x += 1
print()
# 0 1 2 3 4 5


# Break a for loop
# * Break can be used to "for" loops too with the same behavior
for x in range(10):
    print(x, end=' ')
    if x == 5:
        break
print()
# 0 1 2 3 4 5


# Break a for loop with else
# * The else block will not be performed when the loop is interrupted
# * In the example below, the "end" word will not be printed
for x in range(10):
    print(x, end=' ')
    if x == 5:
        break
else:
    print('end')
print()
# 0 1 2 3 4 5


###############################################################################
# Continue
###############################################################################


# Continue in a while loop
# * The continue instruction is used to skip the current iteration of a loop
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x, end=' ')
print()
# 1 2 4 5


# Continue in a for loop
# * The continue works the same way to "for" loops
for i in range(5):
    if i == 3:
        continue
    print(i, end=' ')
print()
# 0 1 2 4


# Continue in a for loop iterating a collection
# * The example below is a useful way to test and process each element of a
#   collection
# * The None value will not be processed due to the existent validation inside
#   the loop
collection = ['A', 'B', None, 'D']
for value in collection:
    if value is None:
        continue
    print(value, end=' ')
print()
# A B D
