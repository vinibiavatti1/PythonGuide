"""
Car example
"""
# Exception for fuel values
class InvalidFuelValueError(Exception):
    def __init__(self, message):
        self._message = message
    @property
    def message(self):
        return self._message

# Car class
class Car:
    def __init__(self, name, brand, fuel=10):
        self._name = name
        self._brand = brand
        self._fuel = fuel if fuel <= 10 and fuel > 0 else 10
    
    # Properties
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, name):
        self._brand = name

    @property
    def fuel(self):
        return self._fuel

    # Methods
    def accelerate(self):
        if self._fuel > 0:
            self._fuel -= 1
            return True
        return False
    def supply(self, fuel_amount):
        if fuel_amount < 0:
            raise InvalidFuelValueError(f'The fuel needs to be in range 0 to 10')
        elif fuel_amount > 10:
            raise InvalidFuelValueError(f'The fuel needs to be in range 0 to 10')
        self._fuel += fuel_amount
        if self._fuel > 10:
            self._fuel = 10
        return True

# Algorithm
car = Car('Cruze', 'Chevrolet')
for i in range(10):
    car.accelerate()
    print(car.fuel, end=', ')
print()

if not car.accelerate():
    print('The car has no fuel!')

car.supply(5)
if not car.accelerate():
    print('The car has no fuel!')
else:
    print('Car is now moving! Lets travel!!!')

try:
    car.supply(-1)
except InvalidFuelValueError as e:
    print(e.message)