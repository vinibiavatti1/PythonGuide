"""
Scale widget (TTK)

* This is the ttk version of Scale widget from TK
* Syntax:
  * ttk.Scale(parent, option, ...)
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
keys = ttk.Scale(master=window).keys()
[print(k) for k in keys]
window.destroy()
"""
command
variable
orient
from
to
value
length
state
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
get()
set(newValue)
"""


###############################################################################
# Example
###############################################################################


# Create the window
# * The window will be created to put the button inside
window = tk.Tk()


# Create the widget
# * The widget will be created and put inside the window
variable = tk.DoubleVar()
variable.set(5.)
widget = ttk.Scale(
    master=window,
    variable=variable,
    from_=0,
    to=10
)


# Set the position of the widget
# * The widget will be automatically adjusted
widget.pack()


# Main loop
# * Start the application
window.mainloop()
