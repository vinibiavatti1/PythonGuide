"""
Facade

* The Facade pattern provides a simplified interface to a complex subsystem.
* It defines a higher-level interface that makes the subsystem easier to use.
"""


###############################################################################
# Facade
###############################################################################


# MP4 Converter
# * This class represents a subsystem that converts video files to MP4 format.
class MP4Converter:
    def convert(self, data: str) -> None:
        return data + '.mp4'


# OGG Converter
# * This class represents a subsystem that converts video files to OGG format.
class OGGConverter:
    def convert(self, data: str) -> None:
        return data + '.ogg'


# Video Compression
# * This class represents a subsystem that compresses video files.
class VideoCompression:
    def compress(self, data: str) -> None:
        return data.strip('__')


# Video Converter Facade
# * This class is a facade for the video conversion process. It simplifies the
#   interface for clients.
# * In other words, it provides a higher-level interface that makes the
#   subsystem easier to use, without needing to perform each step manually.
class VideoConverterFacade:
    def convert(self, data: str, format: str) -> str:
        data = VideoCompression().compress(data)
        if format == 'mp4':
            data = MP4Converter().convert(data)
        else:
            data = OGGConverter().convert(data)
        return data


# Testing
# * Now, look that to perform a video conversion, the client only needs to call
#   a single method on the facade.
converter = VideoConverterFacade()
data = converter.convert('__video__', 'mp4')
print(data)
# video.mp4
