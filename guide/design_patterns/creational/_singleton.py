"""
Singleton design pattern

* Singleton is a creational design pattern that lets you ensure that a class
  has only one instance, while providing a global access point to this instance
* Just like a global variable, the Singleton pattern lets you access some
  object from anywhere in the program
* Nowadays, the Singleton pattern has become so popular that people may call
  something a singleton even if it solves just one of the listed problems
"""


###############################################################################
# Using Meta class
###############################################################################


# Singleton meta class
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances[cls]
        else:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return instance


# Singleton class
class Singleton(metaclass=SingletonMeta):
    pass


# Db Connection extending Singleton
class DBConnection(Singleton):
    pass


# Algorithm
db1 = DBConnection()
db2 = DBConnection()
print(id(db1))  # 2325435530880
print(id(db2))  # 2325435530880 (same id)


###############################################################################
# Using Decorator
###############################################################################


# Singleton decorator
def singleton(cls):
    def wrapper():
        if hasattr(cls, '_instance'):
            return cls._instance
        else:
            cls._instance = cls()
            return cls._instance
    return wrapper


# Singleton class
@singleton
class DbConnection():
    pass


db1 = DbConnection()
db2 = DbConnection()
print(id(db1))  # 2325435530880
print(id(db2))  # 2325435530880 (same id)
