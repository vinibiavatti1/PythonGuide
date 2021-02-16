from abc import ABC, abstractmethod

class Car:
    def __new__(self):
        return 'ABC'
car = Car()
print(car)
exit()

class A:
    a = '1'
a = A()
b = A()
b.a = '2'
print(a.a)
print(b.a)
exit()

x = 1
def func():
    global x
    x = 2
    print(x)
func()
print(x)

class Person(ABC):
    @abstractmethod
    def speak(self, word):
        pass

class Client(Person):
    def speak(self, word):
        print(word)

x = Client()
x.speak('a')