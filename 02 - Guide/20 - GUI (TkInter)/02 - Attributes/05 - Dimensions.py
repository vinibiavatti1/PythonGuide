"""
Dimensions

* Dimensions refer to the size and spacing of widgets in a GUI application.
* They can be specified in various ways, including absolute values and relative
  values.
* Relative values are often specified as a fraction of the parent widget's
  size.
* Absolute values are specified in fixed units, such as pixels or inches.
* Integer values are also accepted and are treated as pixels by default.

* The table below shows the available units for specifying dimensions.
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
# Dimensions
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


# Root Window
# * We will create a root window to demonstrate.
window = tk.Tk()
tk.Button(master=window, text='Pixels (1)', pady=1).pack(fill=tk.X)
tk.Button(master=window, text='Centimeters (1c)', pady='1c').pack(fill=tk.X)
tk.Button(master=window, text='Inches (1i)', pady='1i').pack(fill=tk.X)
tk.Button(master=window, text='Millimeters (1m)', pady='1m').pack(fill=tk.X)
tk.Button(master=window, text='P. Points (1p)', pady='1p').pack(fill=tk.X)
window.mainloop()
