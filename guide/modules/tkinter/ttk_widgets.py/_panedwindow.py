"""
PanedWindow widget (TTK)

* This is the ttk version of PanedWindow widget from TK
* Syntax:
  * ttk.PanedWindow(parent, option, ...)
* Reference:
  * https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
"""
import tkinter as tk
from tkinter import ttk


###############################################################################
# Parameters
###############################################################################


# keys()
# * The keys method shows all parameters for the widget creation
window = tk.Tk()
window.withdraw()
keys = ttk.PanedWindow(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
orient
width
height
takefocus
cursor
style
class
"""


###############################################################################
# Methods
###############################################################################


# Methods
# * The common methods for the widget are:
"""
add(w[, weight=N])
forget(what)
insert(where, w[, weight=N])
panes()
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
widget = ttk.PanedWindow(
    master=window,
    orient=tk.HORIZONTAL
)
left = ttk.Label(master=widget, text='Left')
right = ttk.Label(master=widget, text='Right')
widget.add(left)
widget.add(right)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
