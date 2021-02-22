"""
Matrix

* Matrix is a two-dimensional collection
* Matrix is made by putting a list inside a list
* You can create structures with more dimensions, by putting more collections
  inside the parent collection
"""


# Define matrix
mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(mtx)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Define matrix with comprehension
mtx = [[i for i in range(3)] for _ in range(3)]
print(mtx)
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]


# Define matrix with comprehension (example 1)
mtx = [[i+j for i in range(1, 4)] for j in range(0, 7, 3)]
print(mtx)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Iterate matrix
for y in mtx:
    for x in y:
        print(x, end=', ')
    print()
# 1, 2, 3,
# 4, 5, 6,
# 7, 8, 9,


# Print matrix with comprehension
[[print(x) for x in y] for y in mtx]
# 1 2 3 4 5 6 7 8 9


# Main diagonal
for v in range(len(mtx)):
    print(mtx[v][v], end=', ')
    # 1, 5, 9,
print()


# 3D structure
three_d = [[[i for i in range(3)] for __ in range(3)] for _ in range(3)]
print(three_d)
# [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]],
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]


# Iterate 3D structure
for z in three_d:
    for y in z:
        for x in y:
            print(x, end=', ')
        print()
# 0, 1, 2...
