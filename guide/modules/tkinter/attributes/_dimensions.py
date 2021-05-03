"""
Dimensions

* Various lengths, widths, and other dimensions of widgets can be described in
  many different units
  * If you set a dimension to an integer, it is assumed to be in pixels
  * You can specify units by setting a dimension to a string containing a
    number followed by the character to represent the unity
* Reference:
  * https://www.tutorialspoint.com/python/python_gui_programming.htm
"""
import tkinter as tk


###############################################################################
# Units
###############################################################################


# Dimension units
# * The characters represent each unity for dimension
"""
###############################################################################
Symbol          Description                         Example
###############################################################################
(empty)         Pixels                              '5' or 5
c               Centimenters                        '5c'
i               Inches                              '5i'
m               Millimeters                         '5m'
p               Printer's points (about 1/72")      '5p'
###############################################################################
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
b1 = tk.Button(master=window, text='Pixels (1)', pady=1)
b2 = tk.Button(master=window, text='Centimeters (1c)', pady='1c')
b3 = tk.Button(master=window, text='Inches (1i)', pady='1i')
b4 = tk.Button(master=window, text='Millimeters (1m)', pady='1m')
b5 = tk.Button(master=window, text='P. Points (1p)', pady='1p')


# Set the position of the widget
# * The widget will be automatically adjusted
b1.pack(fill=tk.X)
b2.pack(fill=tk.X)
b3.pack(fill=tk.X)
b4.pack(fill=tk.X)
b5.pack(fill=tk.X)


# Main loop
# * Start the application
window.mainloop()
