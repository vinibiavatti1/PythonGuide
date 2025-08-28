"""
Frame (TTK)

* This is the TTK (Themed Tkinter) version of the Frame widget.
* It provides a more modern look and feel compared to the classic Tkinter
  version.
* The Frame widget is used to create a container for other widgets.
* It can be used to group related widgets together.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk
import tkinter.ttk as ttk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
frame = ttk.Frame(
    master=root,
    relief=tk.GROOVE,
    width=200,
    height=200,
    borderwidth=2
)
frame.pack(padx=20, pady=20)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
frame = ttk.Frame()
[print(k) for k in frame.keys()]
"""
borderwidth
padding
relief
width
height
takefocus
cursor
style
class
"""
