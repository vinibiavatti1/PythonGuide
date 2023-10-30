"""
Matrix

* Matrices aren't a specific type of data, but a way to organize data using
  collections. Basically, a matrix is a collection of collections
* A matrix can have n dimensions, but the most common is 2 dimensions
* We can use tuples, lists or sets to create a matrices
"""


###############################################################################
# Matrix Datatypes
###############################################################################


# Tuple matrix
# * The example below shows a 2D matrix made with tuples
# * Note that a matrix is the same of a tuple of tuples
x = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)


# List matrix
# * The example below shows a 2D matrix made with lists
# * Note that a matrix is the same of a list of lists
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


# Set matrix
# * The example below shows a 2D matrix made with sets
# * Note that for this case we need to use frozensets, since sets can only
#   hold immutable elements that can be hashed for the sets verification
x = {
    frozenset({1, 2, 3}),
    frozenset({4, 5, 6}),
    frozenset({7, 8, 9}),
}


###############################################################################
# Creating a Matrix
###############################################################################


# Creating a matrix (with comprehension) (XXX recommended XXX)
# * We can create a matrix using comprehension
# * In this example, we will use two comprehensions, one for the first level
#   (rows) and another for the second level (columns)
# * Since we will not use the index of the first comprehension, we can use the
#   underscore (_) to ignore it as convention
x = [[i for i in range(3)] for _ in range(3)]
print(x)
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


# Creating a matrix (with for-each)
# * We can create a matrix using for-each
# * In this example, we will use two for-each, one for the first level (rows)
#   and another for the second level (columns)
x = []
for _ in range(3):
    row = []
    for i in range(3):
        row.append(i)
    x.append(row)
print(x)


###############################################################################
# Matrix Iteration
###############################################################################


# Iterate matrix (with for-each) (XXX recommended XXX)
# * We can iterate a matrix using for-each
x = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)
for row in x:
    for col in row:
        print(col, end=', ')
    print()
# 1, 2, 3,
# 4, 5, 6,
# 7, 8, 9,


# Iterate matrix (with comprehension)
# * We can iterate a matrix using comprehension
# * In this case, we will not store the result, since we are only printing the
#   values
x = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)
[[print(col, end=', ') for col in row] for row in x]
print()
# 1, 2, 3, 4, 5, 6, 7, 8, 9,


# Iterate matrix (with while)
# * We can iterate a matrix using while
# * Its is recommended to use for-each or comprehension instead of while
#   since they are more readable
x = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)
row = 0
while row < len(x):
    col = 0
    while col < len(x[row]):
        print(x[row][col], end=', ')
        col += 1
    print()
    row += 1
# 1, 2, 3,
# 4, 5, 6,
# 7, 8, 9,
