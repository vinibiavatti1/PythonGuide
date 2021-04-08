class A:
    def __init__(self, name):
        self.__name = name


class B:
    def __init__(self, name):
        self.__name = name

    def test(self, a):
        print(dir(a))
        print(a.__name)  # Invalid access!


a1 = A('a')
b1 = B('b')
b1.test(a1)
