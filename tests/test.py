class A:
    def __rtruediv__(self, x):
        return 2


a = A()

b = 5 / a
print(b)
