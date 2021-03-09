"""
Facade design pattern

* Facade is a structural design pattern that provides a simplified interface to
  a library, a framework, or any other complex set of classes
* A facade is a class that provides a simple interface to a complex subsystem
  which contains lots of moving parts
"""


# Some operation 1
class Mp4Converter():
    def convert(self, data):
        return data


# Some operation 2
class OggConverter():
    def convert(self, data):
        return data


# Some operation 3
class VideoCompression():
    def compress(self, data):
        return data


# Facade class
class VideoConverterFacade():
    def convert(self, data, format):
        if format == 'mp4':
            data = Mp4Converter().convert(data)
        else:
            data = OggConverter().convert(data)
        data = VideoCompression().compress(data)
        return data


# Algorithm
data = '...'
converter = VideoConverterFacade()  # Easy to call
data = converter.convert(data, 'mp4')
