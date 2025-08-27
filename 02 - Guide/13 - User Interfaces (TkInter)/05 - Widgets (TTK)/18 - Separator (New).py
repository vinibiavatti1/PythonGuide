"""
Separator (TTK)

* The TTK Separator widget is used to create a visual divider between
  different sections of a user interface.
* It can be oriented either horizontally or vertically.
* The separator can be customized in terms of its thickness and color.
* It is commonly used in forms, dialogs, and other UI elements to improve
  organization and readability.
* The separator does not have any interactive elements; it is purely a
  visual aid.
* To create a separator, you can use the `ttk.Separator` class.
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
separator = ttk.Separator(
    master=root,
    orient=tk.HORIZONTAL,
)
separator.pack(fill=tk.X, padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
separator = ttk.Separator()
[print(k) for k in separator.keys()]
"""
orient
takefocus
cursor
style
class
"""
