"""
Top Level

* The Toplevel widget is used to create a new window that is separate from the
  main application window.
* It can be used to create dialog boxes, pop-up windows, or any other type of
  window that needs to be independent from the main window.
* The Toplevel widget is a child of the main window and can be used to display
  additional information or gather input from the user.
* It can be customized with its own title, size, and other properties, just
  like the main window.
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
label1 = tk.Label(
    master=root,
    text="Root Window"
)
label1.pack(padx=50, pady=50)
top_level = tk.Toplevel(
    master=root
)
label2 = tk.Label(
    master=top_level,
    text="Top Level Window"
)
label2.pack(padx=50, pady=50)
root.mainloop()


###############################################################################
# Parameters & Methods
###############################################################################


# Keys
# * The `keys` method shows all parameters for the widget creation.
top_level = tk.Toplevel()
[print(k) for k in top_level.keys()]
"""
bd
borderwidth
class
menu
relief
screen
use
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


# Methods
# * The common methods for the widget are:
"""
aspect(nmin, dmin, nmax, dmax)
deiconify()
geometry(newGeometry=None)
iconify()
lift(aboveThis=None)
lower(belowThis=None)
maxsize(width=None, height=None)
minsize(width=None, height=None)
overrideredirect(flag=None)
resizable(width=None, height=None)
state(newstate=None)
title(text=None)
transient(parent=None)
withdraw()
"""
