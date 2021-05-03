"""
Toplevel widget

* A top-level window is a window that has an independent existence under the
  window manager. It is decorated with the window manager's decorations, and
  can be moved and resized independently. Your application can use any number
  of top-level windows
  * For any widget w, you can get to its top-level widget using
    w.winfo_toplevel()
* Syntax:
  * tk.Toplevel(option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = tk.Toplevel(master=window).keys()
[print(k) for k in keys]
window.destroy()
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


###############################################################################
# Methods
###############################################################################


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


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = tk.Toplevel(
    master=window
)


# Main loop
# * Start the application
window.mainloop()
