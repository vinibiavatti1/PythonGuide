"""
Mode7

* Mode 7 is a graphics mode on the Super NES video game console that allows a
  background layer to be rotated and scaled on a scanline-by-scanline basis to
  create many different effects
* The most famous of these effects is the application of a perspective effect
  on a background layer by scaling and rotating the background layer in this
  manner. This transforms the background layer into a two-dimensional
  horizontal texture-mapped plane that trades height for depth. Thus, an
  impression of three-dimensional graphics is achieved
"""
import tkinter
from tkinter import PhotoImage
from PIL import Image
import os
import sys


###############################################################################
# Constants
###############################################################################


# Util constants
EXAMPLE_TILE = os.path.join(sys.path[0], '../resources/tile.jpg')
DEFAULT_RGB = (0, 0, 0)


###############################################################################
# Classes
###############################################################################


# Mode7 SNES logic class
class Mode7:
    def __init__(self, width, height, image):
        """
        Construct a mode 7 processor
        """
        self.width = width
        self.height = height
        self.half_width = width // 2
        self.half_height = height // 2
        self.image = image
        self.image_data = image.load()
        self.image_width, self.image_heigth = self.image.size
        self.pixels = None
        self.reset_pixels()

    def reset_pixels(self):
        """
        Reset pixel array to initial state
        """
        size = self.width * self.height
        self.pixels = [DEFAULT_RGB for _ in range(size)]

    def get_pixes(self):
        """
        Returns the pixel array
        """
        return self.pixels

    def process_mode7(self):
        """
        Process mode7 logic and generates the pixel array
        """
        z = self.half_height * -1
        for y in range(self.height):
            zz = abs(z)
            if zz == 0:
                zz = 1
            zy = ((y / zz) * 8) % self.image_heigth
            for x in range(self.width):
                xx = x - self.half_width
                xx = abs(xx)
                zx = ((xx / zz) * 8) % self.image_width
                pixel = self.rgb_to_hex(self.image_data[zx, zy])
                self.pixels[self.width * y + x] = pixel
            z += 1

    def render(self):
        """
        Render the pixel array using tkinter
        """
        tk = tkinter.Tk()
        screen = tkinter.Canvas(tk, width=self.width, height=self.height)
        photo = PhotoImage(width=self.width, height=self.height)
        for y in range(self.height):
            for x in range(self.width):
                pixel = self.pixels[self.width * y + x]
                photo.put(pixel, (x, y))
        screen.create_image(0, 0, image=photo, anchor="nw")
        screen.pack()
        tk.mainloop()

    def rgb_to_hex(self, rgb, alpha=True):
        """
        Converts RGB to HEX
        """
        if alpha:
            r, g, b, _ = rgb
        else:
            r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'


###############################################################################
# Algorithm
###############################################################################


# Main
def main():
    image = Image.open(EXAMPLE_TILE)
    mode7 = Mode7(800, 600, image)
    mode7.process_mode7()
    mode7.render()


# Init
if __name__ == '__main__':
    main()
