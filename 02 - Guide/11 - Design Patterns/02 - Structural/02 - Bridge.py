"""
Bridge design pattern

* Book: GOF
* Bridge is a structural design pattern that lets you split a large class or a
  set of closely related classes into two separate hierarchies—abstraction and
  implementation—which can be developed independently of each other.

           bridge
[Remote]<>--------->[Device]
 |                   |    |
[AdvanceRemote]  [Radio] [Tv]
"""
from abc import ABC, abstractmethod


# Device ABC
class Device(ABC):
    def __init__(self, name):
        self.name = name
        self.volume = 0


# Radio class
class Radio(Device):
    def __init__(self, name):
        super().__init__(name)


# TV class
class Tv(Device):
    def __init__(self, name):
        super().__init__(name)


# Remote class
class Remote:
    def __init__(self, device):
        self.device = device  # <-- Bridge

    def volume_up(self):
        self.device.volume += 1

    def volume_down(self):
        self.device.volume -= 1


# Advance remote
class AdvanceRemote(Remote):
    def mute(self):
        self.device.volume = 0


# Algorithm
radio = Radio('Radio')
remote = Remote(radio)
remote.volume_up()
remote.volume_up()
print(remote.device.volume)
# 2

tv = Tv('Tv')
remote = AdvanceRemote(tv)
remote.volume_up()
remote.mute()
print(remote.device.volume)
# 0
