"""
Matrix Multiplication

* The infix operator used to evaluate matrix multiplications is @
* No builtin datatype has the magic methods to evaluate this operation. We have
  to create a custom object to be used for this operation.
* This operation is equivalent to numpy function: dot(m1, m2)
* PEP465: https://www.python.org/dev/peps/pep-0465/
* The magic methods used to evaluate this operation are:
  * __matmul__: x @ y
  * __rmatmul__: y @ x
  * __imatmul__: x @= y
"""


# Define Matrix Class
# * To use the @ operator, some object must implement the magic methods for
#   matrix multiplication
class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __matmul__(self, other):
        # Multiplication logic...
        return [[19, 22], [43, 50]]


# Using the Matrix Multiplication Infix
# * When the @ operator is used, the magic methods will be called to return the
#   resulted value
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print(m1 @ m2)
# [[19, 22], [43, 50]]
