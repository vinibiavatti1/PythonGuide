"""
Frame

* The Frame widget is used to create a container for other widgets.
* It can be used to group related widgets together.
"""


###############################################################################
# Import
###############################################################################


# Import
# * We will import tkinter to be used on the examples below.
import tkinter as tk


###############################################################################
# Example
###############################################################################


# Example
# * The example below creates a simple GUI application with the widget.
root = tk.Tk()
frame = tk.Frame(
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
frame = tk.Frame()
[print(k) for k in frame.keys()]
"""
bd
borderwidth
class
relief
background
bg
colormap
container
cursor
height
highlightbackground
highlightcolor
highlightthickness
padx
pady
takefocus
visual
width
"""
