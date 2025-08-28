"""
Sizegrip (TTK)

* The TTK Sizegrip widget is used to create a resizable corner grip in a
  window.
* It allows users to resize the window by dragging the grip with the mouse.
* The sizegrip is typically placed in the bottom-right corner of the window.
* It can be customized in terms of its appearance and behavior.
* The sizegrip does not have any interactive elements; it is purely a
  visual aid.
* To create a sizegrip, you can use the `ttk.Sizegrip` class.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
from tkinter import ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
root.geometry('400x300')
sizegrip = ttk.Sizegrip(
    master=root,
)
sizegrip.pack(side=tk.BOTTOM, anchor=tk.SE, padx=1, pady=1)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
sizegrip = ttk.Sizegrip()
[print(k) for k in sizegrip.keys()]
"""
orient
takefocus
cursor
style
class
"""
