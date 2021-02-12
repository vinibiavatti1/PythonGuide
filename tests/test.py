from abc import ABC, abstractmethod

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
    pass

x = Client()
x.speak('a')

a = as2 as asdjo w01

print asd