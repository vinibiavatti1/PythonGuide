"""
Adapter design pattern

* Book: GOF
* Adapter is a structural design pattern that allows objects with incompatible
  interfaces to collaborate
* This is a special object that converts the interface of one object so that
  another object can understand it
"""


# Degree
class DegreeTemperature:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature


# Fahrenheit
class FahrenheitTemperature:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature


# Adapter
class FahrenheitAdapter(FahrenheitTemperature):
    def __init__(self, adaptee):
        super().__init__(adaptee.temperature)

    @property
    def temperature(self):
        return self._temperature * 9 / 5 + 32


# Algorithm
degree = DegreeTemperature(25)
fahrenheit = FahrenheitAdapter(degree)
print(fahrenheit.temperature)
# 77.0
